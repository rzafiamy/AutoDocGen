#include "helpers.h"

// Simple insertion sort for simplicity
void sort(double *data, int size) {
    for (int i = 1; i < size; i++) {
        double key = data[i];
        int j = i - 1;

        while (j >= 0 && data[j] > key) {
            data[j + 1] = data[j];
            j = j - 1;
        }
        data[j + 1] = key;
    }
}
