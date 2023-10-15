#include <pybind11/pybind11.h>
#include <cstdint>
#include <iostream>


uint64_t merge(uint64_t a, uint64_t b) {
    uint64_t result = a;
    result <<= 8;
    result |= b;
    return result;
}

float signal_message(uint64_t message, int start, int length, int message_len, float factor) {    
    start = 64 - message_len * 8 + start;
    message = message >> (64 - start + length);
  
    uint64_t mask = 0;
    for (int i = 0; i < length; i++) {
         mask <<= 1;  // shift the mask left by one bit
        mask |= 1;   // set the least significant bit to 1
    }
  
    uint64_t masked_message = message & mask;

    return masked_message * factor;

}



namespace py = pybind11;

PYBIND11_MODULE(merge_module, m) {
    m.doc() = "pybind11 merge module"; // optional module docstring
    m.def("merge", &merge, "A function which merges two uint8_t values into a uint64_t value");
    m.def("signal_message", &signal_message, "A function which takes a message and returns a float");
}
