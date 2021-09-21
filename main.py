from Account import Account

michaelAccount = Account( 12345, "Michael Miller" )
alvaroAccount = Account( 22222, "Alvaro Sanchez" )
julieAccount = Account( 54321, "Julie Sanders" )

#michaelAccount.withdraw( 100.0 )
michaelAccount.deposit( 1000.0 )
#michaelAccount.printInfo()
#michaelAccount.withdraw( 500.0 )
#michaelAccount.printInfo()

Account.changeBankName( "The Coding Dojo Bank" );
print( Account.allBankAccounts )

Account.printAllAccountsInfo()

result = Account.doesAccountHasMoreThan1000( michaelAccount )
print( result )