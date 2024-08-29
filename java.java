import java.util.Scanner;

public class ATM {
    public static void main(String[] args) {
        
        double balance = 0.00;
        Scanner scanner = new Scanner(System.in);
        int choice;

        do {
            
            System.out.println("Welcome to the ATM!");
            System.out.println("1. Check Balance");
            System.out.println("2. Deposit Money");
            System.out.println("3. Withdraw Money");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();

            
            switch (choice) {
                case 1:
                    
                    System.out.println("Your current balance is: " + balance + " pesos");
                    break;
                case 2:
                    
                    System.out.print("Enter amount to deposit: ");
                    double depositAmount = scanner.nextDouble();
                    if (depositAmount > 0) {
                        balance += depositAmount;
                        System.out.println(depositAmount + " pesos deposited successfully.");
                    } else {
                        System.out.println("Invalid deposit amount.");
                    }
                    break;
                case 3:
                    
                    System.out.print("Enter amount to withdraw: ");
                    double withdrawAmount = scanner.nextDouble();
                    if (withdrawAmount > 0 && withdrawAmount <= balance) {
                        balance -= withdrawAmount;
                        System.out.println(withdrawAmount + " pesos withdrawn successfully.");
                    } else if (withdrawAmount > balance) {
                        System.out.println("Insufficient balance.");
                    } else {
                        System.out.println("Invalid withdrawal amount.");
                    }
                    break;
                case 4:
                    System.out.println("Thank you for using the ATM. Goodbye!");
                    break;
                default:
                    
                    System.out.println("Invalid choice. Please try again.");
                    break;
            }

            System.out.println();

        } while (choice != 4);

        scanner.close();
    }
}
