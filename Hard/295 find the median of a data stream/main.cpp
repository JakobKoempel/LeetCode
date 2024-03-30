#include <queue>
#include <stdio.h>


class MedianFinder {
public:
    MedianFinder() {
        median = 0;
    }
    
    void addNum(int num) {
        int left_count = left_half.size();
        int right_count = right_half.size();
        if (((float) num) >= median){
            if (left_count == right_count){
                right_half.push(num);
                median = right_half.top();
            }
            else if (left_count == right_count + 1){
                right_half.push(num);
                median = ((float) left_half.top() + (float) right_half.top()) / 2;
            }
            else if (left_count + 1 == right_count){
                right_half.push(num);
                left_half.push(right_half.top());
                right_half.pop();
                median = ((float) left_half.top() + (float) right_half.top()) / 2;
            }
            else{
                printf("error num >= median");
            }
        }
        else{
            if(left_count == right_count){
                left_half.push(num);
                median = left_half.top();
            }
            else if (left_count + 1 == right_count){
                left_half.push(num);
                median = ((float) left_half.top() + (float) right_half.top()) / 2;
            }
            else if(left_count == right_count + 1){
                left_half.push(num);
                right_half.push(left_half.top());
                left_half.pop();
                median = ((float) left_half.top() + (float) right_half.top()) / 2;
            }
            else{
                printf("error num < median");
            }
        }
    }
    
    double findMedian() {
        return median;
    }
private:
    std::priority_queue<int> left_half;
    std::priority_queue<int, std::vector<int>, std::greater<int>> right_half;
    float median;

};

int main(){
    MedianFinder m;
    m.addNum(-1);
    printf("%f", m.findMedian());
    m.addNum(-2);
    printf("%f", m.findMedian());
    m.addNum(-3);
    printf("%f", m.findMedian());
    m.addNum(-4);
    printf("%f", m.findMedian());
    m.addNum(-5);
    printf("%f", m.findMedian());
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * float param_2 = obj->findMedian();
 */