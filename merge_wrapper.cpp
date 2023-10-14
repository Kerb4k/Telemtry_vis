#include <pybind11/pybind11.h>
#include <cstdint>

uint64_t merge(uint64_t a, uint64_t b) {
    uint64_t result = a;
    result <<= 8;
    result |= b;
    return result;
}

float signal_message(uint64_t message, int start, int length, float factor) {
    //takes all bits from start for a length of a message and multiplies by factor
    uint64_t mask = 0;
    for (int i = 0; i < length; i++) {
        mask <<= 1;
        mask |= 1;
    }
    mask <<= start;
    uint64_t masked_message = message & mask;
    masked_message >>= start;
    return masked_message * factor;
}



namespace py = pybind11;

PYBIND11_MODULE(merge_module, m) {
    m.doc() = "pybind11 merge module"; // optional module docstring
    m.def("merge", &merge, "A function which merges two uint8_t values into a uint64_t value");
    m.def("signal_message", &signal_message, "A function which takes a message and returns a float");
}
