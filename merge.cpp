

#include <cstdint>
#include <iostream>

using namespace std;
uint64_t merge(uint8_t a, uint8_t b) {
    uint64_t result = a;
    result <<= 8;
    result |= b;
    return result;
}

