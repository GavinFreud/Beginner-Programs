#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    int secret, guess;
    int count = 0;
    srand(time(NULL));
    cout << "You have 3 tries to guess the number! Good luck!" << endl;
    secret = rand() % 10 + 1;
    do {
      count++;
      //if(count == 3){
      //  cout << "Sorry! Try again next time!" << endl;
      //  return 0;
      //}
      cout << "Guess the number between 1 and 10: ";
      cin >> guess;
      if(count == 3){
        cout << "Sorry! Try again next time!" << endl;
        return 0;
      }
      if(guess != secret){
         cout << "Sorry! Try again!" << endl;
      }

    }while(secret != guess);
    cout << "Congrats You got it in " << count << " tries!" << endl;
    return 0;
}
