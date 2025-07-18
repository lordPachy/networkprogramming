#include <stdio.h>
#include <stdint.h>

struct addrinfo {
    int ai_flags; // AI_PASSIVE, AI_CANONNAME, etc.
    int ai_family; // AF_INET, AF_INET6, AF_UNSPEC
    int ai_socktype; // SOCK_STREAM, SOCK_DGRAM
    int ai_protocol; // use 0 for "any"
    size_t ai_addrlen; // size of ai_addr in bytes
    struct sockaddr *ai_addr; // struct sockaddr_in or _in6
    char *ai_canonname; // full canonical hostname

    struct addrinfo *ai_next; // linked list, next node
};

struct sockaddr {
    unsigned short sa_family; // address family, AF_xxx
    char sa_data[14]; // 14 bytes of protocol address
};

struct in_addr {
    uint32_t s_addr; // that's a 32-bit int (4 bytes)
};

struct sockaddr_in {
    short int sin_family; // Address family, AF_INET
    unsigned short int sin_port; // Port number
    struct in_addr sin_addr; // Internet address
    unsigned char sin_zero[8]; // Same size as struct sockaddr
};


struct sockaddr_in6 {
    uint16_t sin6_family; // address family, AF_INET6
    uint16_t sin6_port; // port, Network Byte Order
    uint32_t sin6_flowinfo; // IPv6 flow information
    struct in6_addr sin6_addr; // IPv6 address
    uint32_t sin6_scope_id; // Scope ID
};

struct in6_addr {
    unsigned char s6_addr[16]; // IPv6 address
};

struct sockaddr_storage {
    sa_family_t ss_family; // address family
    // all this is padding, implementation specific, ignore it:
    char __ss_pad1[_SS_PAD1SIZE];
    int64_t __ss_align;
    char __ss_pad2[_SS_PAD2SIZE];
};

typedef unsigned short sa_family_t;

int main () {
    // IPv4:
    struct sockaddr_in ip4addr;
    int s;
    
    ip4addr.sin_family = AF_INET;
    ip4addr.sin_port = htons(3490);
    inet_pton(AF_INET, "10.0.0.1", &ip4addr.sin_addr);
    
    s = socket(PF_INET, SOCK_STREAM, 0);
    bind(s, (struct sockaddr*)&ip4addr, sizeof ip4addr);

    return 0;
}