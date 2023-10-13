from functools import reduce

class transaction(object):
    def __init__(self, left, right, loss_of_profit, merge_flag):
        self.left = left
        self.right = right
        self.loss_of_profit = loss_of_profit
        self.merge_flag = merge_flag

    def __str__(self):
        return str(self.left) + " " + str(self.right) + " " + str(self.loss_of_profit) + " " + str(self.merge_flag)
    

class Solution(object):
    def maxProfit(self, k, prices):
        trans = self.getTransactions(prices)
        total_profit = sum([t.right - t.left for t in trans])
        m = len(trans)
        if m == 0:
            return 0
        while m > k:
            (i_min, t_min) = min(enumerate(trans), key=lambda elem: elem[1].loss_of_profit)
            total_profit = total_profit - t_min.loss_of_profit
            
            if t_min.merge_flag:
                t_min.right = trans[i_min + 1].right
                del trans[i_min + 1]
                m = m - 1
                if i_min > 0:
                    self.setMergeAndProfitLoss(trans[i_min - 1], t_min)
                if i_min < m - 1:
                    self.setMergeAndProfitLoss(t_min, trans[i_min + 1])
                if i_min == m - 1:
                    t_min.loss_of_profit = t_min.right - t_min.left
                    t_min.merge_flag = False
            else:
                del trans[i_min]
                m = m - 1
                if i_min > 0 and i_min < m:
                    self.setMergeAndProfitLoss(trans[i_min - 1], trans[i_min])
                if i_min == m:
                    t_last = trans[m - 1]
                    t_last.loss_of_profit = t_last.right - t_last.left
                    t_last.merge_flag = False
        return total_profit
    
    def getTransactions(self, prices):
        #compute rising sections of the prices list
        n = len(prices)
        rising = [False] * n
        for i in range(n - 1):
            rising[i] = prices[i + 1] > prices[i]

        #compute the first and last price of upward slopes in the price list
        trans = []
        i = 0
        l = r = -1
        prev_rising = False
        while i < n:
            if rising[i] and not prev_rising:
                l = i
                prev_rising = True
            elif not rising[i] and prev_rising:
                r = i 
                trans.append(transaction(prices[l], prices[r], 0, False))
                prev_rising = False
            i = i + 1 

        #compute whether a transaction should be deleted or merged to the right for the smallest loss of profit
        m = len(trans)
        for i in range(m - 1):
            self.setMergeAndProfitLoss(trans[i], trans[i + 1])
        if m > 0:
            #the last transaction doesn't have a right neighbour so it can't be merged
            trans[m-1].loss_of_profit = trans[m-1].right - trans[m-1].left
            trans[m-1].merge_flag = False
        return trans
    
    def setMergeAndProfitLoss(self, t1, t2):
        l_1 = t1.left
        r_1 = t1.right
        l_2 = t2.left
        r_2 = t2.right
        if l_1 < l_2 and r_1 < r_2:
            t1.merge_flag = True
            old_profit = r_1 - l_1 + r_2 - l_2
            new_profit = r_2 - l_1
            t1.loss_of_profit = old_profit - new_profit
        else:
            t1.merge_flag = False
            t1.loss_of_profit = r_1 - l_1
        