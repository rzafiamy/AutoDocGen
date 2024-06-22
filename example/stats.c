#include "stats.h"
#include "helpers.h"
#include <math.h>

double mean(double *data, int size) {
    double sum = 0;
    for (int i = 0; i < size; i++) {
        sum += data[i];
    }
    return sum / size;
}

double median(double *data, int size) {
    sort(data, size);  // Assuming sort is implemented in helpers.c
    if (size % 2 == 0) {
        return (data[size / 2 - 1] + data[size / 2]) / 2;
    } else {
        return data[size / 2];
    }
}

double std_dev(double *data, int size, double mean) {
    double sum_sq_diff = 0;
    for (int i = 0; i < size; i++) {
        sum_sq_diff += pow(data[i] - mean, 2);
    }
    return sqrt(sum_sq_diff / size);
}
