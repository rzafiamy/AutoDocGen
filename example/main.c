#include "stats.h"
#include <stdio.h>

int main() {
    double data[] = {12.0, 15.5, 18.7, 11.3, 14.2};
    int size = sizeof(data) / sizeof(data[0]);

    double m = mean(data, size);
    double md = median(data, size);
    double sd = std_dev(data, size, m);

    printf("Mean: %.2f\n", m);
    printf("Median: %.2f\n", md);
    printf("Standard Deviation: %.2f\n", sd);

    return 0;
}
