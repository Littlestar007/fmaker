#include <stdio.h>

// 函数原型声明
void swap(int *a, int *b);

int main() {
    int x = 10;
    int y = 20;

    printf("Before swap: x = %d, y = %d\n", x, y);
    swap(&x, &y); // 调用swap函数交换x和y的值
    printf("After swap: x = %d, y = %d\n", x, y);

    return 0;
}

// 交换两个整数的函数
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}
