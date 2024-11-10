#include <iostream>
using namespace std;	

// Recursive Approach
int fibonacci_recursive(int n, int& count) 
{
  count++;
  if (n <= 1) 
  {
    return n;
  } else 
  {
    return fibonacci_recursive(n-1, count) + fibonacci_recursive(n-2, count);
  }
}

// Iterative Approach
int fibonacci_iterative(int n, int& count) 
{
  count++;
  if (n <= 1) 
  {
    return n;
  }

  int a = 0;
  int b = 1;

  for (int i = 2; i <= n; i++) 
  {
    count++;
    int temp = a + b;
    a = b;
    b = temp;
  }
  return b;
}


int main() 
{
  int n;
  cout << "Enter the value of n: ";
  cin >> n;

  int count_recursive = 0;
  int result_recursive = fibonacci_recursive(n, count_recursive);
  cout << "Fibonacci number using recursive approach: " << result_recursive <<endl;
  cout << "Step count for recursive approach: " << count_recursive <<endl;

  int count_iterative = 0;
  int result_iterative = fibonacci_iterative(n, count_iterative);
  cout << "Fibonacci number using iterative approach: " << result_iterative <<endl;
  cout << "Step count for iterative approach: " << count_iterative <<endl;

  return 0;
}
