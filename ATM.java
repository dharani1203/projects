public class ATM {
    private int balance;
    private int pin = 1234;
    
    public ATM(int balance,int pin){
        this.balance=balance;
        this.pin=pin;
    }

    public void displayMenu(){
        System.out.println("1. Check balance");
        System.out.println("2: Deposit");
        System.out.println("3: withdraw");
        System.out.println("4: Change pin");
        System.out.println("5: Exit");
    }

    public void deposit (int amount){
        balance+=amount;
    }

    public void withdraw(int amount){
        if(balance<amount){
            System.out.println("Insufficient Funds!");
            return;
        }
        balance-=amount;

    }

    public int getbalance(){
        return balance;
    }

    public boolean validatePin(int pin){
        return this.pin==pin;
    }

    public void changePin(int newPin){
        pin = newPin;
        System.out.println("Pin Changed");
    }
        



    public static void main(String[] args) {
        ATM atm = new ATM(1000, 1234);
        atm.displayMenu();
        System.out.print("enter the pin:");
        int pin = Integer.parseInt(System.console().readLine());
        if(atm.validatePin(pin)){
            int option = 0;
            while(option!=5){
                atm.displayMenu();
                option = Integer.parseInt(System.console().readLine());
                switch (option) {
                    case 1:
                        System.out.println("Balance:" +atm.getbalance());
                        break;
                    case 2:
                        System.out.println("enter amount: ");
                        int amount = Integer.parseInt(System.console().readLine());
                        atm.deposit(amount);
                        break;

                    case 3:
                        System.out.println("enter amount: ");
                        amount = Integer.parseInt(System.console().readLine());
                        atm.withdraw(amount);
                        break;

                    case 4:
                        System.out.println("enter New pin: ");
                        int newPin = Integer.parseInt(System.console().readLine());
                        atm.changePin(newPin);
                        break;

                    case 5:
                        System.out.println("Thank You for using ATM!");
                        break;

                    default:
                        break;


            }
        }
    }
        else{
        System.out.println("You have entered Entered Invalid pin!");
        }

    }

}
