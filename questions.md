# Questions

## Question 1

What is the time complexity of the following C program?

```c
#include <stdio.h>

#define MAXN 100

int main() {
    int n = 0, i = 0, j = 0;
    int mat[MAXN][MAXN];

    fscanf(stdin, "%d", &n);

    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            fscanf(stdin, "%d", &mat[i][j]);
        }
    }

    for (i = 0; i < n; i++) {
        mat[i][0] *= 2;
    }
}
```
The time complexity of this C program is O(n^2).\
The main function contains a nested loop to read integers from the standard input and populate the matrix by rows (fixing each row and iterating over the columns). The external loop body is executed n times, incrementing index i from 0 to n-1 (when i==n the for condition is no longer satisfied). The internal loop body (a single instruction, O(1)) is also executed n times, incrementing index j from 0 to n-1 (when j==n the for condition is no longer satisfied). Therefore, the nested loop complexity is O(n^2).\
A final for loop is executed to multiply the elements of the first column of the matrix by 2. This loop body (a single instruction, O(1)) is executed n times (the index i value is reset to 0 and then incremented until i==n).
Considering that, the complexity of this loop is O(n).\
The overall time complexity is O(n^2)+O(n) which simplifies to O(n^2).


## Question 2

What is a memory leak? Explain how to correctly free memory after a dynamic
memory allocation in C

In a C program, a memory leak occurs when the program allocates memory dinamically but fails in deallocating it when is no longer needed.This can lead to a situation in which the majority of the available memory becomes allocated and so the application and the entire system may crash.\
Memory leaks in C primarily occur when dynamically allocated memory isn't deallocated after its usage (with a corresponding free() call), when pointers to allocated memory are lost making deallocation impossible, or when programs terminate before memory can be properly released.\
To correctly handle dynamic memory in C, each allocation must be associated to a deallocation using the function free(). A good practice and the freed pointer should be set to null in order to avoid accidental usage of a dandling pointer.

## Question 3

What is an abstract method in OOP? How is it used?

In Object Oriented Programming (OOP) an abstract method is a function declared in an abstract class without any implementation. This idea is strongly connected to class inheritance, a fundamental concept in OOP that allows a class (subclass) to inherit properties and methods from another class (base class).\
The idea of building an abstract class that includes abstract methods is forcing its subclasses (classes that extend it) to have their own implementation of the abstract method, establishing a common interface.

## Question 4

How is `systemd` used in most Linux systems?

`systemd` is a software suite of basic building blocks for a Linux system. Its core component the system and service manager, a process that runs as PID 1 during boot and starts the rest of the system.\
In other words, this process is responsable of handling processes' booting, service lifecycle, resource control, logging, device management, user sessions, and network configuration.

## Question 5

What is a `git rebase`?

`git rebase` is a git command that is used to perform rebasing: moving or combining a sequence of commits to a new base commit.\
Git offers two main ways to integrate changes from one branch to another: the merge and the rebase. With the rebase command, you can take all the changes that were committed on one branch and replay them on a different branch rewriting its commit history.\
At a high level, immagine we want to rebase branch b2 on branch b1. The `git rebase` command works by finding the common ancestor between b1 and b2 (the last shared commit between the two branches), temporarily removing all commits made on b2, moving b2 base to the current tip of b1 and finally reappling the saved commits on top of the updated b1.
