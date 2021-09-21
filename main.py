from Account import Account
from User import User

michaelUser = User( "Michael", "Miller", 30 )
alvaroUser = User( "Alvaro", "Sanchez", 35 )

michaelAccount = Account( 12345, michaelUser )
alvaroAccount = Account( 22222, alvaroUser )

michaelAccount.deposit( 10000.0 )
alvaroAccount.deposit( 1000.0 )

michaelAccount.transfer( alvaroAccount, 2000.0 )

Account.printAllAccountsInfo()


#michaelAccount.withdraw( 100.0 )
#michaelAccount.deposit( 1000.0 )
#michaelAccount.printInfo()
#michaelAccount.withdraw( 500.0 )
#michaelAccount.printInfo()

#michaelAccount.withdraw( 100.0 ).deposit( 1000.0 ).printInfo()
#michaelAccount.withdraw( 500.0 ).printInfo()

#Account.changeBankName( "The Coding Dojo Bank" );
#print( Account.allBankAccounts )

#Account.printAllAccountsInfo()

#result = Account.doesAccountHasMoreThan1000( michaelAccount )
#print( result )