class Account:
    bankName = "Coding Dojo Bank"
    allBankAccounts = []

    def __init__( self, accountNum, owner ):
        self.accountNum = accountNum
        self.owner = owner
        self.balance = 0.0
        Account.allBankAccounts.append( self )

    def withdraw( self, amount ):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print( "We cannot process your withdrawal." )
            print( f"You currently have {self.balance}." )
            print( f"And you are trying to withdraw {amount}." )

    def deposit( self, amount ):
        self.balance += amount

    def printInfo( self ):
        print( f"Account owner: {self.owner}." )
        print( f"Account number: {self.accountNum}." )
        print( f"Account balance: {self.balance}." )

    @classmethod
    def changeBankName( cls, newName ):
        cls.bankName = newName
    
    @classmethod
    def printAllAccountsInfo( cls ):
        for account in cls.allBankAccounts:
            print( account.bankName )
            account.printInfo()

    @staticmethod
    def doesAccountHasMoreThan1000( account ):
        if( account.balance >= 1000 ):
            return True
        else:
            return False
