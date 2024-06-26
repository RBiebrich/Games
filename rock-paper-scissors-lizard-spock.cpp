// This program will allow the user to play Rock Paper Scissor Lizard Spock against the computer

#include <iostream>
#include <stdlib.h>

int main() {

  srand (time(NULL));

  int computer = rand() % 5 + 1;

  int user = 0;

  std::cout << "====================\n";
  std::cout << "rock paper scissors lizard spock!\n";
  std::cout << "====================\n";
  
  std::cout << "1) ✊\n";
  std::cout << "2) ✋\n";
  std::cout << "3) ✌️\n";
  std::cout << "4) Lizard\n";
  std::cout << "5) Spock\n";

  std::cout << "shoot! ";
  std::cin >> user;
  std::cout << "Computer: " << computer << "\n";

  //ROCK
  if (computer == 1){
    switch(user) {
      case 1:
        std::cout << "It's a tie!\n";
        break;

      case 2:
        std::cout << "You win!\n";
        break;

      case 3:
        std::cout << "Computer wins!\n";
        break;

      case 4:
        std::cout << "Computer wins!\n";
        break;

      case 5:
        std::cout << "You win!\n";
        break;
    }
  }

  //PAPER
  if (computer == 2){
    switch(user) {
      case 1:
        std::cout << "Computer wins!\n";
        break;

      case 2:
        std::cout << "It's a tie!\n";
        break;

      case 3:
        std::cout << "You win!\n";
        break;

      case 4:
        std::cout << "You win!\n";
        break;

      case 5:
        std::cout << "Computer wins!\n";
        break;
    }
  }

  //SCISSORS
  if (computer == 3){
    switch(user) {
      case 1:
        std::cout << "You win!\n";
        break;

      case 2:
        std::cout << "Computer wins!\n";
        break;

      case 3:
        std::cout << "It's a tie!\n";
        break;

      case 4:
        std::cout << "Computer wins!\n";
        break;

      case 5:
        std::cout << "You win!\n";
        break;
    }
  }

  //LIZARD
  if (computer == 4){
    switch(user) {
      case 1:
        std::cout << "You win!\n";
        break;

      case 2:
        std::cout << "Computer wins!\n";
        break;

      case 3:
        std::cout << "You win!\n";
        break;

      case 4:
        std::cout << "It's a tie!\n";
        break;

      case 5:
        std::cout << "Computer wins!\n";
        break;
    }
  }

  //SPOCK
  if (computer == 5){
    switch(user) {
      case 1:
        std::cout << "Computer wins!\n";
        break;

      case 2:
        std::cout << "You win!\n";
        break;

      case 3:
        std::cout << "Computer wins!\n";
        break;

      case 4:
        std::cout << "You win!\n";
        break;

      case 5:
        std::cout << "It's a tie!\n";
        break;
    }
  }
}