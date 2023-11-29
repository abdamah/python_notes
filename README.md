# What is Programming?

Programming is the process of designing and building executable computer programs to accomplish a specific task or solve a particular problem. It involves creating a set of instructions that a computer can interpret and execute to perform a desired function. Programmers, also known as developers or software engineers, use programming languages to communicate with computers and create software.

## Key Aspects of Programming

1. **Algorithm Design:** Programmers need to plan and design algorithms, which are step-by-step procedures or formulas for solving problems. These algorithms serve as the foundation for the program.

2. **Syntax and Semantics:** Programming languages have specific rules (syntax) and meanings (semantics) that must be followed. The programmer writes code using the correct syntax and ensures that the code's semantics align with the intended logic.

3. **Debugging:** Identifying and fixing errors or bugs in the code is a crucial part of programming. Debugging involves systematically tracing through the code to find and resolve issues.

4. **Data Structures:** Choosing and implementing appropriate data structures (such as arrays, linked lists, and trees) is essential for efficient information storage and retrieval.

5. **Logic and Control Flow:** Programming involves defining the logical flow of a program, determining how it will respond to different inputs or conditions, and controlling the execution of instructions.

6. **Testing:** Programmers must test their code to ensure it functions as intended. This involves running the program with various inputs to check for correctness and identifying and fixing any errors.

7. **Documentation:** Writing documentation is important for communicating how the program works, its purpose, and how to use it. This helps other developers understand and maintain the code.

8. **Collaboration:** In many cases, programming is a collaborative effort, with multiple developers working on different aspects of a project. Version control systems and collaborative tools facilitate teamwork.

Programming can be done using a variety of programming languages, each with its own syntax and features. Some popular programming languages include Python, Java, JavaScript, C++, and many others. The choice of language often depends on the specific requirements of the project.

# Fundamentals of Programming

### 1. Variables and Data Types

- **Variables:** Containers for storing data values. The data type of a variable determines what kind of data it can hold.
- **Data Types:** Examples include integers, floating-point numbers, characters, and strings.

### 2. Control Flow

- **Conditional Statements:** If statements, switch statements. These allow the program to make decisions based on certain conditions.
- **Loops:** For loops, while loops. These allow the program to repeat a certain block of code.

### 3. Functions

- A block of code that performs a specific task.
- Functions can be reusable and help in modularizing code.

### 4. Arrays and Lists

- Collections of data. Arrays (in some languages) have a fixed size, while lists can dynamically adjust.
- Elements in an array or list are accessed by their index.

### 5. Input/Output

- Ways to interact with the user or the external world.
- Reading input from the keyboard, displaying output on the screen, file I/O, etc.

### 6. Operators

- Symbols that perform operations on variables and values.
- Examples include +, -, \*, /, % (modulo), == (equality), != (not equal), etc.

### 7. Comments

- Lines in the code that are ignored by the computer but provide information to the human reader.
- Good comments make code more understandable.

### 8. Error Handling

- Techniques for gracefully handling errors and exceptions.
- This includes try-catch blocks in languages that support them.

### 9. Object-Oriented Programming (OOP)

- Concepts like classes and objects.
- Encapsulation, inheritance, and polymorphism are key principles.

### 10. Algorithmic Thinking

- Developing step-by-step procedures or formulas for solving problems.
- Understanding algorithms is fundamental to efficient programming.

### 11. Debugging

- The process of finding and fixing errors in the code.
- Tools and techniques for effective debugging.

### 12. Version Control

- Tools like Git to manage and track changes in the codebase.
- Collaboration and code management are facilitated by version control.

### 13. Basic Understanding of Memory and Performance

- Understanding how memory is allocated and deallocated.
- Awareness of basic performance considerations.

### 14. Software Development Life Cycle (SDLC)

- Understanding the different stages of software development, from requirements gathering to deployment and maintenance.

### 15. Problem-Solving Skills

- The ability to break down a problem into smaller parts and systematically solve them.

These fundamentals are applicable to most programming languages, although syntax and some features may vary. Once you grasp these basics, you can apply them to learn and work with specific programming languages and frameworks.

# C Programming

### Overview

C i`s a general-purpose, procedural programming language developed at Bell Labs in the early 1970s by` **Dennis Ritchie**. `Known for its efficiency, performance, and low-level capabilities`, C has had a significant impact on the development of many other programming languages.

### Key Features

1. **Procedural Language:**

   - C follows a top-down design approach, breaking problems into smaller procedures or functions.

2. **Low-Level Manipulation:**

   - Provides low-level access to memory, suitable for system programming and operating systems development.

3. **Structured Programming:**

   - Supports structured programming constructs for organized and maintainable code.

4. **Efficiency and Performance:**

   - Known for high performance, allowing direct manipulation of hardware through pointers.

5. **Portability:**

   - Highly portable, with compilers available for a wide range of systems.

6. **Extensibility:**

   - Easily extended through libraries, serving as the foundation for other programming languages.

7. **Standard Libraries:**

   - Provides standard libraries (e.g., `<stdio.h>`, `<stdlib.h>`) for common operations.

8. **Syntax:**

   - Simple syntax with a small set of keywords, operators, and constructs.

9. **Pointers:**

   - Enables efficient memory management and data manipulation through direct memory address manipulation.

10. **Community and Legacy:**
    - Strong and active community; C has influenced many modern programming languages.

### Applications

C is widely used in various domains:

- System Programming
- Embedded Systems
- Game Development
- Application Development

## Learning C

Learning C provides a solid foundation for understanding computer architecture, memory management, and programming concepts applicable to a broad range of languages.

### Explanation

- **Header files:** Include necessary header files at the beginning of your program.

- **Macros and constants:** Define macros or constants that are used throughout the program.

- **Function prototypes:** Declare function prototypes before the `main` function.

- **Global variables:** Declare global variables that need to be accessed by multiple functions.

- **Main function:** The entry point of the program. Declare local variables, write the main logic, and make function calls.

- **Function definitions:** Implement the functions declared in the prototypes.

## C Program Structure

### Description

This document outlines a basic structure for a C program.

### Code

```c
// Header files
#include <stdio.h>  // Standard Input/Output functions
// Add any other necessary header files

// Macros and constants
#define MAX_SIZE 100  // Example macro for maximum size

// Function prototypes
void exampleFunction();  // Example function prototype
// Add prototypes for other functions used in the program

// Global variables
int globalVariable;  // Example global variable

// Main function
int main() {
    // Variable declarations
    int localVariable;  // Example local variable

    // Code statements

    // Function calls
    exampleFunction();

    return 0;  // Indicates successful program execution
}

// Function definitions
void exampleFunction() {
    // Function body
    printf("This is an example function.\n");
    // Function implementation
}
// Define other functions used in the program
```

### Explanation

- **Header files:** Include necessary header files at the beginning of your program.

- **Macros and constants:** Define macros or constants that are used throughout the program.

- **Function prototypes:** Declare function prototypes before the `main` function.

- **Global variables:** Declare global variables that need to be accessed by multiple functions.

- **Main function:** The entry point of the program. Declare local variables, write the main logic, and make function calls.

- **Function definitions:** Implement the functions declared in the prototypes.
- **Comment**: Used to explain code snippets that used inside program and also to describe code functionalities.

```c
#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}
```

## Variable in C

In C programming, a **variable** is a named location in memory that is used to store data. Variables are fundamental elements in programming, allowing manipulation and handling of data within programs. Each variable has a specific data type, which dictates the type of data it can hold and the operations that can be performed on it.

To declare a variable in C, you use the following **syntax**:

```c
data_type variable_name;
int age
```

After declaring a variable, you can assign a value to it using the assignment operator (=). Here's an example:

```c
int age;      // Declaration
age = 25;     // Assignment
```

Alternatively, you can combine declaration and assignment in a single line:

```c
int age = 25; // Declaration and assignment
```

In this example, int is the data type (integer), and age is the variable name.

Variables serve various purposes, such as _performing calculations, storing user input, and influencing the flow of a program_. Understanding how to declare and use variables is fundamental to
writing C programs.

## Function in C

In C programming, a **function** is a self-contained block of code that performs a specific task. Functions are essential for modularizing code, improving readability, and facilitating code reuse. In C, a program typically consists of one or more functions.

The basic syntax for declaring and defining a function in C is as follows:

```c
return_type function_name(parameters) {
    // Function body
    // Code to perform the specified task
    return value; // Optional return statement
}
```

### Function Declaration

Here can be declared function prototype that specifies the function signature.

##### Function Prototype in C

In C programming, a function prototype is a declaration that provides information about a function before its actual implementation or definition.

### Syntax

```c
return_type function_name(parameter_type1, parameter_type2, ...);
```

### Return Type

Specifies the type of value that the function returns. It can be `int`, `float`, `void` (for functions that don't return a value), or other data types.

### Function Name

The name of the function, which is used to call it from other parts of the program.

### Parameters

Input values that the function can use during its execution. Parameters are optional, and a function can have none or multiple parameters.

### Function Body

The block of code within curly braces `{}` that defines what the function does.

### Return Value

An optional statement that returns a value from the function to the calling code. The return type in the function declaration should match the type of the value being returned.

## Variable Scope in C

In C programming, the scope of a variable refers to the region of the program where the variable is visible and can be accessed. There are two main types of variable scope:

### 1. Global Scope

- Variables declared outside of any function or block have global scope.
- Global variables are accessible throughout the entire program, from the point of declaration to the end of the program.
- They can be used in any function, including the `main` function and other user-defined functions.

  ```c
  #include <stdio.h>

  // Global variable with global scope
  int globalVariable = 10;

  int main() {
      // Accessing the global variable in the main function
      printf("Global Variable inside main: %d\n", globalVariable);
      return 0;
  }
   printf("Global Variable outside main: %d\n", globalVariable);
  ```

### 2. Local Scope

Variables declared inside a function or a block have local scope. Local variables are only accessible within the function or block where they are declared. They are not visible to other functions or blocks in the program.

```c
#include <stdio.h>

int main() {
    // Local variable with local scope
    int localVariable = 5;

    // Accessing the local variable within the main function
    printf("Local Variable: %d\n", localVariable);

    return 0;
}

prinftf("Local variable outside main: %d\n", localVariable); // error
```

## Types of Functions in C

In C programming, functions are classified into different types based on their characteristics and return types. Here are the main types of functions:

### 1. Standard Library Functions

- These functions are provided by the C Standard Library.
- Examples include functions for input/output (`printf`, `scanf`), mathematical operations (`sqrt`, `sin`), memory management (`malloc`, `free`), and more.
- They are accessible by including the relevant header files.

### 2. User-Defined Functions

- Functions created by the programmer to perform specific tasks.
- They enhance code modularity and reusability.
- Defined using the `function_name` syntax with a specified return type, function body, and parameters.

```c
 // Example of a user-defined function
   int add(int a, int b) {
       return a + b;
   }
```

## C programm Statements

In the context of the C programming language, a program statement is a basic unit of execution that expresses an action to be carried out. These statements are combined to form a complete C program. Here are some common types of C program statements:

```c
// Declaration Statements
int age;
float salary;

// Assignment Statements
age = 25;
salary = 50000.75;

// Arithmetic Statements
int sum = a + b;

// Conditional Statements
if (x > 0) {
    // code to be executed if x is greater than 0
} else {
    // code to be executed if x is not greater than 0
}

// While loop
int i = 0;
while (i < 10) {
    // code to be repeated while i is less than 10
    i++;
}

//Do while loop
int i = 0;
do {
    // code to be repeated at least once
    i++;
} while (i < 10);


// Loop Statements
for (int i = 0; i < 10; i++) {
    // code to be repeated 10 times
}

// Function Call Statements
result = add(a, b);

// Input/Output Statements
printf("Enter your age: ");
scanf("%d", &age);

// Switch Statement
switch (day) {
    case 1:
        // code for Monday
        break;
    case 2:
        // code for Tuesday
        break;
    // other cases
    default:
        // code for other days
}

// Break and Continue Statements
for (int i = 0; i < 10; i++) {
    if (i == 5) {
        break; // exit the loop when i is 5
    }
    // code inside the loop
}
```

## String in C

C programming, strings are typically represented as arrays of character.

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Declaration and Initialization of a String
char greeting[] = "Hello, World!";

// Outputting a String
printf("Message: %s\n", greeting);

// String Length
int length = strlen(greeting);
printf("Length of the string: %d\n", length);

// Concatenating Strings
char name[] = "John";
char message[50];
strcpy(message, "Hello, ");
strcat(message, name);
printf("%s\n", message);

// Comparing Strings
char str1[] = "apple";
char str2[] = "orange";
int result = strcmp(str1, str2);
if (result == 0) {
    printf("Strings are equal\n");
} else if (result < 0) {
    printf("%s comes before %s\n", str1, str2);
} else {
    printf("%s comes after %s\n", str1, str2);
}

// Inputting a String
char input[50];
printf("Enter your name: ");
scanf("%s", input);
printf("Hello, %s!\n", input);
    return 0;
}

```
- *Strings are terminated with '\0' specifier.*

## Arrays in C

In C programming, an array is a collection of elements of the same data type, stored in contiguous memory locations. It provides a way to group related data under a single name and allows efficient manipulation of a large set of data.

### Declaration and Initialization

To declare an array in C, you specify the data type of its elements and the array's name, followed by its size in square brackets. Here's an example of declaring an integer array named `numbers` with a size of 5:
```c
int numbers[5];
```
### Accessing Elements

Individual elements in an array are accessed using their index. The index starts at 0 for the first element and goes up to `size - 1` for the last element. 

For example, to access the first element of the `numbers` array:

```c
int firstElement = numbers[0];
```

### Multi-dimensional Arrays

C supports multi-dimensional arrays, allowing you to create arrays of arrays. For instance, a 2D array can be declared as follows:

```c
int matrix[3][3] = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};
```

```c
// Declaration and Initialization of an Array
int numbers[5] = {1, 2, 3, 4, 5};

// Accessing Array Elements
printf("First element: %d\n", numbers[0]);
printf("Second element: %d\n", numbers[1]);

// Modifying Array Elements
numbers[2] = 10;

// Iterating Through an Array
printf("Array elements: ");
for (int i = 0; i < 5; i++) {
    printf("%d ", numbers[i]);
}
printf("\n");

// Multi-dimensional Array
int matrix[3][3] = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};

// Accessing Elements in a Multi-dimensional Array
printf("Element at matrix[1][2]: %d\n", matrix[1][2]);

// String as an Array of Characters
char word[] = "Hello";

// Accessing Characters in a String
printf("First character: %c\n", word[0]);

// Inputting Elements into an Array
int inputArray[3];
for (int i = 0; i < 3; i++) {
    printf("Enter element %d: ", i + 1);
    scanf("%d", &inputArray[i]);
}

// Displaying Inputted Array
printf("Inputted elements: ");
for (int i = 0; i < 3; i++) {
    printf("%d ", inputArray[i]);
}
printf("\n");

```

## Pointer in C
In C programming, a pointer is a **variable that stores the memory address of another variable**. It allows you to indirectly manipulate the data at the memory location it points to. Pointers are powerful and versatile, enabling more efficient memory management and access to data structures.

**Example**:

```c
#include <stdio.h>

int main() {
    // Declare a variable
    int num = 42;

    // Declare a pointer variable
    int *ptr;

    // Assign the address of 'num' to the pointer
    ptr = &num;

    // Access the value through the pointer
    printf("Value of num: %d\n", *ptr);

    // Modify the value through the pointer
    *ptr = 99;

    // Check the updated value
    printf("Updated value of num: %d\n", num);

    return 0;
}
```

### Explanation

- `int num = 42;`: Declare an integer variable named `num` and initialize it with the value 42.
- `int *ptr;`: Declare an integer pointer variable named `ptr`.
- `ptr = &num;`: Assign the memory address of `num` to the pointer `ptr`.
- `printf("Value of num: %d\n", *ptr);`: Access the value pointed to by `ptr` using the dereference operator (`*`) and print it.
- `*ptr = 99;`: Modify the value at the memory location pointed to by `ptr`.
- `printf("Updated value of num: %d\n", num);`: Print the updated value of `num`.


## Class Storages in C

In the context of the C programming language, the term "storage class" r**efers to a set of keywords that define the scope (visibility) and lifetime (duration) of variables**. C has four storage classes: ``auto, register, static, and extern``. Here's a brief overview of each:

1. ``auto``:

- This is the *default storage class for local variables*.
- Variables declared as ``auto`` are created when the block containing their declaration is **entered** and destroyed when the block is **exited**.
- The use of auto is **optional**, as it is the default behavior.

**Example**:
```c
void exampleFunction() {
    auto int x; // 'auto' is optional
    // 'x' is a local variable with automatic storage duration
}
```
2. ``register``:

- The ``register`` keyword suggests to the compiler that a variable should be stored in a **register** for faster access.
- However, the compiler is not obligated to honor this suggestion, as modern compilers are often adept at optimizing register usage without explicit hints

**Example**:
```c
register int count; // Compiler hint to use a register for 'count'
```

3. ``static``:

- Variables declared as ``static`` within a function retain their values between function calls.
- When used at the global level, static variables are only visible within the file where they are declared.
- It is often used for variables that need to persist their values *across function calls while maintaining a limited scope*.

**Example**:
```c
void exampleFunction() {
    static int y = 0; // 'y' retains its value between function calls
}
```

4. ``extern``:

The ``extern`` keyword is used to declare a variable or function that is defined in another file.
It tells the compiler that the actual definition of the variable or function exists elsewhere.
This is crucial for linking multiple source files together.

**Example**:
```c
extern int globalVar; // Declaration of a variable defined in another file
```
These *storage classes provide a level of control over how variables are stored in memory, how long they persist, and where they can be accessed*. They are essential for managing memory efficiently and controlling the visibility and lifespan of variables in a C program.

## Struct in C

In C, a struct **(short for structure)** is a composite data type that allows you to group together variables of different types under a single name. It enables you to create a custom data type that can hold related pieces of information. The individual variables within a struct are called members or fields.

Here's the basic syntax for defining a struct in C:

```c
struct StructName {
    // Member variables (fields)
    datatype1 member1;
    datatype2 member2;
    // ... additional members
};
```
Here's a simple example of a struct representing a point in two-dimensional space:

```c
#include <stdio.h>

// Define a struct named Point to represent a 2D point with x and y coordinates
struct Point {
    int x;
    int y;
};

int main() {
    // Declare a variable of type Point
    struct Point p1;

    // Initialize the values of the struct members
    p1.x = 10;
    p1.y = 20;

    // Access and print the values
    printf("Point coordinates: (%d, %d)\n", p1.x, p1.y);

    return 0;
}
```

- The `struct Point` is defined to have two members, `x` and `y`, both of type `int`.
- In the `main` function, a variable `p1` of type `struct Point` is declared.
- The members of `p1` (`x` and `y`) are accessed and modified as needed.
- Structs are useful for organizing related pieces of data into a single unit, providing a way to encapsulate and manage complex data structures in C.


## Enum in C
In C, an enum (short for enumeration) is a user-defined data type that consists of a set of named integer constants. Enums provide a way to create named integer values, which makes the code more readable and self-explanatory. Each named constant in an enumeration is called an enumerator.

Here's the basic syntax for defining an enum in C:

```c
enum EnumName {
    // List of enumerators
    enumerator1,
    enumerator2,
    // ... additional enumerators
};
```

Here's a simple example of an enum representing different colors:
```c 
#include <stdio.h>

// Define an enum named Color to represent different colors
enum Color {
    RED,
    GREEN,
    BLUE
};

int main() {
    // Declare a variable of type Color
    enum Color myColor = RED;

    // Use a switch statement to perform actions based on the color
    switch (myColor) {
        case RED:
            printf("The color is Red.\n");
            break;
        case GREEN:
            printf("The color is Green.\n");
            break;
        case BLUE:
            printf("The color is Blue.\n");
            break;
        default:
            printf("Unknown color.\n");
    }

    return 0;
}
```

In this example:

- The `enum Color` defines an enumeration with three enumerators: `RED`, `GREEN`, and `BLUE`.
- A variable `myColor` of type `enum Color` is declared and initialized with the value `RED`.
- A `switch` statement is used to perform actions based on the value of `myColor`.
- Enums are useful when you want to represent a set of named integer constants, providing a more meaningful and expressive way to work with such constants in your code.


## Memory Management in C:

Memory management in C involves the allocation and deallocation of memory during program execution. In C, programmers have direct control over memory, and they must explicitly request and release memory as needed. The primary mechanisms for memory management in C include dynamic memory allocation functions like **malloc**, **calloc**, **realloc**, and **free**.

Here are the key concepts related to memory management in C:
1. Static Memory Allocation:

-- **Definition**: Memory for variables is allocated during compile-time.

**Example**:
```c
int staticArray[10];  // Static allocation of an integer array
```

2. Dynamic Memory Allocation
**Functions**:

- ``malloc``: Allocates a specified number of bytes of memory.
- ``calloc``: Allocates a specified number of blocks of memory, each with a specified number of bytes.
- ``realloc``: Changes the size of a previously allocated block of memory.
- Example:

```c
int *dynamicArray;
dynamicArray = (int *)malloc(10 * sizeof(int));  // Allocating an integer array dynamically
```

### Freeing Memory
**Function**:

``free``: Deallocates the memory previously allocated by malloc, calloc, or realloc.
**Example**:
```c
free(dynamicArray);  // Deallocating the dynamically allocated memory
```

### Memory Leak
*Definition*: Occurs when allocated memory is not deallocated, leading to a gradual loss of available memory.

**Example**:
```c
// Memory leak example
int *leakedMemory = (int *)malloc(sizeof(int));
// Memory not freed
```

### Memory Management Best Practices
- Always free dynamically allocated memory using free when it is no longer needed.
- Check the return value of memory allocation functions to ensure successful allocation.
- Avoid using uninitialized or freed memory.

Here's a simple example demonstrating dynamic memory allocation and deallocation in C:

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    // Dynamic memory allocation for an integer array
    int *dynamicArray = (int *)malloc(5 * sizeof(int));

    if (dynamicArray == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    // Assigning values to the dynamically allocated array
    for (int i = 0; i < 5; i++) {
        dynamicArray[i] = i * 2;
    }

    // Printing the values
    for (int i = 0; i < 5; i++) {
        printf("%d ", dynamicArray[i]);
    }

    // Freeing the dynamically allocated memory
    free(dynamicArray);

    return 0;
}
```
This program dynamically allocates memory for an integer array, assigns values to the array, prints the values, and then frees the allocated memory. Proper memory management is crucial to prevent memory leaks and ensure efficient use of system resources.

## File I/O in C

**File I/O (Input/Output)** in C is a way to handle reading from and writing to files. The standard library provides functions for file I/O operations in C, and the most commonly used ones are declared in the ``stdio.h`` header file.

Here's a basic overview of how file I/O works in C:

### Opening a File:
To open a file, you can use the ``fopen`` function. It takes two arguments: the name of the file and the mode in which you want to open the file *(read, write, append, etc.)*.
**Example**:
```c
#include <stdio.h>

int main() {
    FILE *filePointer;

    // Open a file for writing ("w" mode)
    filePointer = fopen("example.txt", "w");

    if (filePointer == NULL) {
        printf("Error opening the file.\n");
        return 1;
    }

    // Perform operations on the file

    // Close the file when done
    fclose(filePointer);

    return 0;
}
```

### Writing to a File:
To write to a file, you can use functions like ``fprintf`` or fputc. 
**Example**:
```c
#include <stdio.h>

int main() {
    FILE *filePointer;

    filePointer = fopen("example.txt", "w");

    if (filePointer == NULL) {
        printf("Error opening the file.\n");
        return 1;
    }

    fprintf(filePointer, "Hello, File I/O!");

    fclose(filePointer);

    return 0;
}
```

### Reading from a File:
To read from a file, you can use functions like fscanf or ``fgetc``. 
**Example**:

```c
#include <stdio.h>

int main() {
    FILE *filePointer;
    char buffer[100];

    filePointer = fopen("example.txt", "r");

    if (filePointer == NULL) {
        printf("Error opening the file.\n");
        return 1;
    }

    fscanf(filePointer, "%s", buffer);

    printf("Read from file: %s\n", buffer);

    fclose(filePointer);

    return 0;
}
```

### Closing a File:
Always remember to close the file using the ``fclose`` function when you are done with it.
```c
fclose(filePointer);
```
These are just basic examples, and there are many other file I/O functions available in the C standard library for more advanced operations. *Additionally, error checking is important to ensure that file operations are successful*.


# Object-Oriented Programming (OOP)

Object-Oriented Programming (OOP) is a programming paradigm that organizes code into reusable units called **objects**. These objects are instances of **classes**, which serve as blueprints or templates for creating objects. OOP is based on four main principles:

### 1. Encapsulation
Encapsulation involves bundling data (attributes) and methods (functions) that operate on the data into a single unit, called a **class**. This helps in hiding the internal details of an object and exposing only what is necessary.

### 2. Inheritance
Inheritance allows a class (subclass or derived class) to inherit properties and behaviors from another class (superclass or base class). This promotes code reuse and establishes a relationship between the classes, creating a hierarchy.

### 3. Polymorphism
Polymorphism allows objects of different classes to be treated as objects of a common base class. This enables more generic and flexible code, as different classes can be used interchangeably if they adhere to a common interface.

### 4. Abstraction
Abstraction involves simplifying complex systems by modeling classes based on the essential properties and behaviors they share. It allows developers to focus on the relevant details of an object while ignoring the irrelevant ones.

These principles help in creating modular, maintainable, and scalable code. OOP is widely used in software development and is supported by many programming languages, including Java, C++, Python, and others. It provides a way to structure code that mirrors real-world entities and relationships, making it easier to understand and manage complex systems.

## Encapsulation

### Classed and Objects
In Python, a class is a code template for creating objects. Objects have member variables and have behavior associated with them in the form of methods. Essentially, a class is a blueprint for objects, and objects are instances of classes.

#### 1. Class Definition:
A class is defined using the ``class`` keyword, followed by the class name and a colon. The body of the class contains ``attributes`` (variables) and ``methods`` (functions).

**Example**:
```c
class MyClass:
    # class attributes and methods go here
```

#### 2. Attributes:
Attributes are *variables that store data*. They are defined within the class and represent the characteristics or properties of the objects created from that class.

**Example**:
```c
class Person:
    def __init__(self, name):
        self.name = name  # attribute
```

#### 3. Methods:
Methods are* functions defined within a class* that perform operations on the class's attributes or provide functionality related to the class.

**Example**:
```c
class Person:
  def __init__(self, name):
    self.name = name
  
  def say_hi(self):
    return f"Hi!, {self.name} "
```

#### 4. Object Instantiation:
Objects are *instances of a class*. To create an object, you instantiate the class by calling the class name as if it were a function.

**Example**:
```c
abdallah = Person("Abdallah")  # Creating an instance of the Person class
```

#### 5. Constructor (__init__ method):
The __init__ method is a`` special method`` (aka magic method) that gets called when an object is created. It is used to *initialize the attributes of the object*.

**Example**:
```c
class Person:
  def __init__(self, name):
    self.name = name
  
  def say_hi(self):
    return f"Hi!, {self.name} "
```

#### 6. Self:
`self` is a reference to the instance of the class. It is the first parameter in every method of a class and is used to refer to the instance's attributes and methods.

**Example**:
```c
class Person:
  def __init__(self, name):
    self.name = name
  
  def say_hi(self):
    return f"Hi!, {self.name} "
```

Classes provide a way to *structure and organize code* in an object-oriented manner, promoting code reusability and maintainability. They are a fundamental concept in object-oriented programming **(OOP)**.


## Inheritance
Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (subclass or derived class) to inherit the attributes and methods of another class (superclass or base class). This promotes code reuse and the creation of a hierarchy of classes.

n Python, you can implement inheritance using the following syntax:
```c
class BaseClass:
    # attributes and methods of the base class go here

class DerivedClass(BaseClass):
    # additional attributes and methods specific to the derived class go here
```

Here's a more detailed explanation of inheritance in Python:

### 1. Base Class (Superclass):

- The base class is the class whose attributes and methods are inherited by another class.
- It's also referred to as the superclass or parent class.
- It serves as a general template that can be extended or specialized by other classes.

**Example**:
```c
class Person:
    def __init__(self, name):
        self.name = name

    def walk(self):
        pass
```

### 2. Derived Class (Subclass):

- The derived class is the class that ``inherits from another class``.
- It's also referred to as the subclass or child class.
- It can have its *own additional attributes and methods while also inheriting those from the base class*.

**Example**:
```c
class Teacher(Person):  # Teacher is a subclass of Person
    def __init__(self, name, profession):
        super().__init__(name) # call super class constructor.
        self.profession = profession

    def walk(self):
        return "Teacher Walk!"

    def teach(self):
     return "Teach programming"
```

### 3. Method Overriding:

- The derived class can *provide its own implementation for a method that is already defined in the base class*.
- This is known as **method overriding.**

**Example**:
```c
class Teacher(Person):  # Teacher is a subclass of Person
    def __init__(self, name, profession):
        super().__init__(name) # call super class constructor.
        self.profession = profession

    def walk(self): # Method overriding. This method was defined in Person class and here is overrided.
        return "Teacher Walk!" 

    def teach(self):
     return "Teach programming"
```

### 4. super() Function:

The`` super()`` function is used to ``call a method from the base class``.
It's commonly used in the *constructor (__init__ method)* of the derived class to `initialize the attributes from the base class`.

**Example**:
```c
class Child(BaseClass):
    def __init__(self, attribute1, attribute2):
        super().__init__(attribute1)
        self.attribute2 = attribute2
```

Inheritance facilitates the creation of a hierarchy of classes, allowing for the reuse of code and the establishment of relationships between classes. It's a powerful mechanism that promotes code organization and modularity in object-oriented programming.


## Polymorphism
Polymorphism is a key concept in object-oriented programming (OOP) **that allows objects of different types to be treated as objects of a common type**. It enables flexibility and extensibility in code by allowing a single interface (method or function) to be used for different types of objects.
There are two main types of polymorphism in Python: 
- compile-time polymorphism (aka **method overloading**) and 
- runtime polymorphism (aka **method overriding**).

### 1. Compile-time Polymorphism (Method Overloading):
Compile-time polymorphism involves **defining multiple methods in the same class with the same name but different parameter lists.** The method to be called is *determined at compile time based on the number and types of arguments passed.*

**Example**:
```c
class Math:
    def add(self, x, y=0):
        return x + y

math_obj = Math()
result1 = math_obj.add(5)
result2 = math_obj.add(3, 7)

print(result1)  # Output: 5
print(result2)  # Output: 10
```

In this example, the add method is **overloaded with two versions**. One that takes one argument and another that takes two. *The appropriate version is selected based on the number of arguments provided*.

### 2. Runtime Polymorphism (Method Overriding):
Runtime polymorphism involves defining a method in the **superclass and providing a specific implementation in the subclass**. The method in the subclass overrides the method with the same name in the superclass.

**Example**:
```c
class Person:
  def __init__(self, name):
      self.name = name

  def walk(self):
      return f"Person can walk!"

class Teacher(Person):  # Teacher is a subclass of Person
    def __init__(self, name, profession):
        super().__init__(name) # call super class constructor.
        self.profession = profession

    def walk(self):
        return f"Teacher {self.name} Walk!"

    def teach(self):
     return f" {self.name} {self.profession} programming"


person = Person("Ahmed")
teacher = Teacher("Ahmed", "Teaching")

print(person.walk()) # Person can walk!
print(teacher.walk()) # Teacher Ahmed Walk!
```
Polymorphism in Python simplifies code and makes it more flexible. It allows for the creation of generic code that can work with objects of different types, **promoting code reusability and modularity**.


## Abstraction

Abstraction is a fundamental concept in object-oriented programming (OOP) **that involves simplifying complex systems by modeling classes based on the essential properties and behaviors they share**. The goal of abstraction is to provide a *clear and concise representation of the essential features of an object while ignoring or abstracting away the non-essential details*.

In Python, abstraction is achieved through the use of classes and interfaces.*Here are some key aspects of abstraction in Python:*

### 1. Classes:

- lasses serve as a way to abstract and model real-world entities in a program.
- A class defines attributes (data) and methods (functions) that encapsulate the behavior of the object it represents.
- By using classes, you can create instances (objects) that exhibit the same behavior and share common attributes.

```c
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f" {3.14 *  self.radius**2:.2f}"
```

In this example, ``Shape`` is an abstract class with a method area that is meant to be `overridden` by its subclasses, such as ``Circle``.

### 2. Abstract Methods:

- **Abstract methods** are methods declared in an abstract class that have **no implementation in the abstract class itself**.
- *Subclasses must provide concrete implementations for abstract methods*

```c
from abc import ABC, abstractmethod

class Shape(ABC):  # Subclassing ABC (Abstract Base Class)
    @abstractmethod
    def area(self):
        pass
```

In this example, ``Shape`` is an abstract class, and ``area`` is an **abstract method**. Classes that inherit from ``Shape`` must provide a concrete **implementation** for the ``area`` method.


### 3. Interfaces:

- In Python, **interfaces** are often represented using **abstract classes** with **abstract methods**.
- An *interface defines a contract that implementing classes must adhere to*.

```c
from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def bio(self):
        pass

class Person(Printable):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bio(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Instantiate Person object
abdallah = Person("Abdallah", 23)

# Call bio method
abdallah.bio()
```

Here,`` Printable`` is an interface with an a**bstract method bio**. The Person class implements the ``Printable`` interface by providing a *concrete implementation* for **bio**.

Abstraction in Python allows developers to focus on the essential aspects of an object, **promoting clarity, modularity, and maintainability in the code**. It also supports the creation of generic code that can work with different objects as long as they adhere to a common interface or abstract class.


## Author:
- **Abdallah Mahmoud** 
- Facebook : [Aballah Riig](https://www.facebook.com/abdallahriig)
- LinkedIn: [Abdallah Mahmoud](https://www.linkedin.com/in/abdallahmahmud/)