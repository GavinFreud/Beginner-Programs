#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    int secret, guess;
    srand(time(NULL));
    
    secret = rand() % 10 + 1;
    do{
      cout << "Guess the number between 1 and 10: ";
      cin >> guess;
      if(guess != secret){
         cout << "Sorry! Try again!";
      }
    }while(secret != guess);
    cout << "Congrats!";
}
