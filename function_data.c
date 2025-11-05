#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#if defined(_WIN32) || defined(_WIN64)
  #define EXPORT __declspec(dllexport)
#else
  #define EXPORT
#endif

EXPORT double *x_array(){
    double *x_arr = malloc(10000* sizeof(double));
    if (!x_arr)
    {
        perror("malloc failed");
        exit(EXIT_FAILURE);
    }
    for (int i = 0; i < 10000; i++)
    {
        x_arr[i] = i * 0.01;
    }
    return x_arr;
}

EXPORT double *y_array(){
    double *y_arr = malloc(10000* sizeof(double));
    if (!y_arr)
    {
        perror("malloc failed");
        exit(EXIT_FAILURE);
    }
    for (int i = 0; i < 10000; i++)
    {
        // Trying Different Functions
        // y_arr[i] = (i * 0.01)*(i*0.01); // x^2
        // y_arr[i] = sin(i*0.01); // sinx
        // y_arr[i] = pow(i*0.01,2.712821282); // e^x
        // y_arr[i] = i*0.01; // x
        y_arr[i] = log(i*0.01); // lnx
        // y_arr[i] = cos(i*0.01); // cosx
    }
    return y_arr;
}

EXPORT void free_array(double* arr) {
    free(arr);
}
