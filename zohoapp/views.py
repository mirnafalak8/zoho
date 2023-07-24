import base64
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.utils.text import capfirst
from django.contrib.auth.models import User,auth
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.views import View
from .forms import EmailForm
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse



# Create your views here.
def index(request):

    return render(request,'index.html')



def register(request):
   
    if request.method=='POST':

        first_name=capfirst(request.POST['fname'])
        last_name=capfirst(request.POST['lname'])
        username=request.POST['uname']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email1']
        phone = request.POST['phone']

      
        if password==cpassword:  #  password matching......
            if User.objects.filter(username=username).exists(): #check Username Already Exists..
                messages.info(request, 'This username already exists!!!!!!')
                return redirect('register')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email)
                
                user.save()
                u = User.objects.get(id = user.id)

                company_details(contact_number = phone, user = u).save()
    
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            print("Password is not Matching.. ") 
            return redirect('register')   
        return redirect('register')

    return render(request,'register.html')

def login(request):
        
    if request.method == 'POST':
        
        email_or_username = request.POST['emailorusername']
        password = request.POST['password']
        print(password)
        user = authenticate(request, username=email_or_username, password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            # .........................................................
            user=request.user        
            account_info = [{"user": user, "account_type": "Expense","account_name":"Advertising and Marketing","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"Your expenses on promotional, marketing and advertising activities like banners, web-adds, trade shows, etc. are recorded in advertising and marketing account.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Other Current Assets","account_name":"Advance Tax","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"Any tax which is paid in advance is recorded into the advance tax account. This advance tax payment could be a quarterly, half yearly or yearly payment","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Expense","account_name":"Automobile Expense","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"Transportation related expenses like fuel charges and maintenance charges for automobiles, are included to the automobile expense account.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Expense","account_name":"Bad Debt","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"Any amount which is lost and is unrecoverable is recorded into the bad debt account.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Expense","account_name":"Bank Fees and Charges","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":" Any bank fees levied is recorded into the bank fees and charges account. A bank account maintenance fee, transaction charges, a late payment fee are some examples.","watchlist":"","create_status":"default","status":"active"},
            
            {"user": user, "account_type": "Expense","account_name":"Consultant Expense","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"Charges for availing the services of a consultant is recorded as a consultant expenses. The fees paid to a soft skills consultant to impart personality development training for your employees is a good example.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Cost Of Goods Sold","account_name":"Cost of Goods Sold","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"An expense account which tracks the value of the goods sold.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Expense","account_name":"Credit Card Charges","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":" Service fees for transactions , balance transfer fees, annual credit fees and other charges levied on a credit card are recorded into the credit card account.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Expense","account_name":"Depreciation Expense","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"Any depreciation in value of your assets can be captured as a depreciation expense.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Expense","account_name":"Depreciation Expense","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"Any depreciation in value of your assets can be captured as a depreciation expense.","watchlist":"","create_status":"default","status":"active"},

            {"user": user, "account_type": "Income","account_name":"Discount","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"Any reduction on your selling price as a discount can be recorded into the discount account.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Equity","account_name":"Drawings","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"The money withdrawn from a business by its owner can be tracked with this account.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Other Current Assets","account_name":"Employee Advance","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"Money paid out to an employee in advance can be tracked here till it's repaid or shown to be spent for company purposes","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Other Current Liability","account_name":"Employee Reimbursements","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"This account can be used to track the reimbursements that are due to be paid out to employees.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Other Expense","account_name":"Exchange Gain or Loss","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"Changing the conversion rate can result in a gain or a loss. You can record this into the exchange gain or loss account.","watchlist":"","create_status":"default","status":"active"},

            {"user": user, "account_type": "Fixed Asset","account_name":"Furniture and Equipment","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"Purchases of furniture and equipment for your office that can be used for a long period of time usually exceeding one year can be tracked with this account.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Income","account_name":"General Income","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"A general category of account where you can record any income which cannot be recorded into any other category","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Income","account_name":"Interest Income","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"A percentage of your balances and deposits are given as interest to you by your banks and financial institutions. This interest is recorded into the interest income account.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Stock","account_name":"Inventory Asset","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"An account which tracks the value of goods in your inventory.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Expense","account_name":"IT and Internet Expenses","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"Money spent on your IT infrastructure and usage like internet connection, purchasing computer equipment etc is recorded as an IT and Computer Expense","watchlist":"","create_status":"default","status":"active"},

            {"user": user, "account_type": "Expense","account_name":"Janitorial Expense","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"All your janitorial and cleaning expenses are recorded into the janitorial expenses account.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Income","account_name":"Late Fee Income","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"Any late fee income is recorded into the late fee income account. The late fee is levied when the payment for an invoice is not received by the due date","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Expense","account_name":"Lodging","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"Any expense related to putting up at motels etc while on business travel can be entered here.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Expense","account_name":"Meals and Entertainment","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"Expenses on food and entertainment are recorded into this account.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Expense","account_name":"Office Supplies","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"All expenses on purchasing office supplies like stationery are recorded into the office supplies account.","watchlist":"","create_status":"default","status":"active"},

            {"user": user, "account_type": "Other Current Liability","account_name":"Opening Balance Adjustments","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"This account will hold the difference in the debits and credits entered during the opening balance.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Equity","account_name":"Opening Balance Offset","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"This is an account where you can record the balance from your previous years earning or the amount set aside for some activities. It is like a buffer account for your funds.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Income","account_name":"Other Charges","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"Miscellaneous charges like adjustments made to the invoice can be recorded in this account.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Expense","account_name":"Other Expenses","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":" Any minor expense on activities unrelated to primary business operations is recorded under the other expense account.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Equity","account_name":"Owner's Equity","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"The owners rights to the assets of a company can be quantified in the owner's equity account.","watchlist":"","create_status":"default","status":"active"},

            {"user": user, "account_type": "Cash","account_name":"Petty Cash","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"It is a small amount of cash that is used to pay your minor or casual expenses rather than writing a check.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Expense","account_name":"Postage","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"Your expenses on ground mails, shipping and air mails can be recorded under the postage account.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Other Current Assets","account_name":"Prepaid Expenses","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"An asset account that reports amounts paid in advance while purchasing goods or services from a vendor.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Expense","account_name":"Printing and Stationery","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":" Expenses incurred by the organization towards printing and stationery.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Expense","account_name":"Rent Expense","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"The rent paid for your office or any space related to your business can be recorded as a rental expense.","watchlist":"","create_status":"default","status":"active"},

            {"user": user, "account_type": "Expense","account_name":"Repairs and Maintenance","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"The costs involved in maintenance and repair of assets is recorded under this account.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Equity","account_name":"Retained Earnings","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"The earnings of your company which are not distributed among the share holders is accounted as retained earnings.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Expense","account_name":"Salaries and Employee Wages","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"Salaries for your employees and the wages paid to workers are recorded under the salaries and wages account.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Income","account_name":"Sales","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":" The income from the sales in your business is recorded under the sales account.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Income","account_name":"Shipping Charge","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"Shipping charges made to the invoice will be recorded in this account.","watchlist":"","create_status":"default","status":"active"},

            {"user": user, "account_type": "Other Liability","account_name":"Tag Adjustments","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":" This adjustment account tracks the transfers between different reporting tags.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Other Current Liability","account_name":"Tax Payable","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"The amount of money which you owe to your tax authority is recorded under the tax payable account. This amount is a sum of your outstanding in taxes and the tax charged on sales.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Expense","account_name":"Telephone Expense","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"The expenses on your telephone, mobile and fax usage are accounted as telephone expenses.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Expense","account_name":"Travel Expense","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":" Expenses on business travels like hotel bookings, flight charges, etc. are recorded as travel expenses.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Expense","account_name":"Uncategorized","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"This account can be used to temporarily track expenses that are yet to be identified and classified into a particular category.","watchlist":"","create_status":"default","status":"active"},

            {"user": user, "account_type": "Cash","account_name":"Undeposited Funds","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"Record funds received by your company yet to be deposited in a bank as undeposited funds and group them as a current asset in your balance sheet.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Other Current Liability","account_name":"Unearned Revenue","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"A liability account that reports amounts received in advance of providing goods or services. When the goods or services are provided, this account balance is decreased and a revenue account is increased.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Equity","account_name":"Capital Stock","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":" An equity account that tracks the capital introduced when a business is operated through a company or corporation.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Long Term Liability","account_name":"Construction Loans","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"An expense account that tracks the amount you repay for construction loans.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Expense","account_name":"Contract Assets","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"An asset account to track the amount that you receive from your customers while you're yet to complete rendering the services.","watchlist":"","create_status":"default","status":"active"},

            {"user": user, "account_type": "Expense","account_name":"Depreciation And Amortisation","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"An expense account that is used to track the depreciation of tangible assets and intangible assets, which is amortization.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Equity","account_name":"Distributions","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"An equity account that tracks the payment of stock, cash or physical products to its shareholders.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Equity","account_name":"Dividends Paid","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"An equity account to track the dividends paid when a corporation declares dividend on its common stock.","watchlist":"","create_status":"default","status":"active"},

            {"user": user, "account_type": "Other Current Liability","account_name":"GST Payable","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Other Current Liability","account_name":"Output CGST","credit_no":"","sub_account":"on","parent_account":"GST Payable","bank_account_no":"","currency":"","account_code":"","description":"","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Other Current Liability","account_name":"Output IGST","credit_no":"","sub_account":"on","parent_account":"GST Payable","bank_account_no":"","currency":"","account_code":"","description":"","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Other Current Liability","account_name":"Output SGST","credit_no":"","sub_account":"on","parent_account":"GST Payable","bank_account_no":"","currency":"","account_code":"","description":"","watchlist":"","create_status":"default","status":"active"},

            {"user": user, "account_type": "Equity","account_name":"Investments","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"An equity account used to track the amount that you invest.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Cost Of Goods Sold","account_name":"Job Costing","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"An expense account to track the costs that you incur in performing a job or a task.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Cost Of Goods Sold","account_name":"Labor","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"An expense account that tracks the amount that you pay as labor.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Cost Of Goods Sold","account_name":"Materials","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"An expense account that tracks the amount you use in purchasing materials.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Expense","account_name":"Merchandise","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"An expense account to track the amount spent on purchasing merchandise.","watchlist":"","create_status":"default","status":"active"},

            {"user": user, "account_type": "Long Term Liability","account_name":"Mortgages","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"An expense account that tracks the amounts you pay for the mortgage loan.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Expense","account_name":"Raw Materials And Consumables","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"An expense account to track the amount spent on purchasing raw materials and consumables.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Other Current Assets","account_name":"Reverse Charge Tax Input but not due","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"The amount of tax payable for your reverse charge purchases can be tracked here.","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Other Current Assets","account_name":"Sales to Customers (Cash)","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Cost Of Goods Sold","account_name":"Subcontractor","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":" An expense account to track the amount that you pay subcontractors who provide service to you.","watchlist":"","create_status":"default","status":"active"},

            {"user": user, "account_type": "Other Current Assets","account_name":"GST TCS Receivable","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Other Current Assets","account_name":"GST TDS Receivable","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"","watchlist":"","create_status":"default","status":"active"},

            {"user": user, "account_type": "Other Current Assets","account_name":"Input Tax Credits","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Other Current Assets","account_name":"Input CGST","credit_no":"","sub_account":"on","parent_account":"Input Tax Credits","bank_account_no":"","currency":"","account_code":"","description":"","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Other Current Assets","account_name":"Input IGST","credit_no":"","sub_account":"on","parent_account":"Input Tax Credits","bank_account_no":"","currency":"","account_code":"","description":"","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Other Current Assets","account_name":"Input SGST","credit_no":"","sub_account":"on","parent_account":"Input Tax Credits","bank_account_no":"","currency":"","account_code":"","description":"","watchlist":"","create_status":"default","status":"active"},

            {"user": user, "account_type": "Other Current Liability","account_name":"TDS Payable","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Other Current Assets","account_name":"TDS Receivable","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"","watchlist":"","create_status":"default","status":"active"},
            {"user": user, "account_type": "Expense","account_name":"Transportation Expense","credit_no":"","sub_account":"","parent_account":"","bank_account_no":"","currency":"","account_code":"","description":"An expense account to track the amount spent on transporting goods or providing services.","watchlist":"","create_status":"default","status":"active"},




            ]
            print(account_info[0])
            print(account_info[1])

            for account in account_info:
                print(account)
                if not Chart_of_Account.objects.filter(account_name=account['account_name']).exists():
                    new_account = Chart_of_Account(user=account['user'],account_name=account['account_name'],account_type=account['account_type'],credit_no=account['credit_no'],sub_account=account['sub_account'],parent_account=account['parent_account'],bank_account_no=account['bank_account_no'],currency=account['currency'],account_code=account['account_code'],description=account['description'],watchlist=account['watchlist'],create_status=account['create_status'],status=account['status'])
                    new_account.save()

            

            return redirect('base')
           
        else:
            return redirect('/')
        

    return render(request, 'register.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='login')
def base(request):
   
       
    if not Unit.objects.filter(unit='BOX').exists():
            Unit(unit='BOX').save()
    if not Unit.objects.filter(unit='UNIT').exists():
            Unit(unit='UNIT').save()
    if not Unit.objects.filter(unit='LITRE').exists():
            Unit(unit='LITRE').save()

    if not Sales.objects.filter(Account_name='General Income').exists():
            Sales(Account_type='INCOME',Account_name='General Income',Account_desc='salesincome').save()
    if not Sales.objects.filter(Account_name='Intrest Income').exists():
            Sales(Account_type='INCOME',Account_name='Intrest Income',Account_desc='salesincome').save()
    if not Sales.objects.filter(Account_name='Late fee Income').exists():
            Sales(Account_type='INCOME',Account_name='Late fee Income',Account_desc='salesincome').save()
    if not Sales.objects.filter(Account_name='Discount Income').exists():
            Sales(Account_type='INCOME',Account_name='Discount Income',Account_desc='salesincome').save()
    if not Sales.objects.filter(Account_name='Other Charges').exists():
            Sales(Account_type='INCOME',Account_name='Other Charges',Account_desc='salesincome').save()
    if not Sales.objects.filter(Account_name='Shipping Charge').exists():
            Sales(Account_type='INCOME',Account_name='Shipping Charge',Account_desc='salesincome').save()


    if not  Purchase.objects.filter(Account_name='Advertising & Marketing').exists():
            Purchase(Account_type='EXPENCES',Account_name='Advertising & Markting',Account_desc='Advertsing Exp').save()
    if not Purchase.objects.filter(Account_name='Debit Charge').exists():
            Purchase(Account_type='EXPENCES',Account_name='Debit Charge',Account_desc='Debited Exp').save()
    if not Purchase.objects.filter(Account_name='Labour Charge').exists():
            Purchase(Account_type='EXPENCES',Account_name='Labour Charge',Account_desc='Labour Exp').save()
    if not Purchase.objects.filter(Account_name='Raw Meterials').exists():
            Purchase(Account_type='EXPENCES',Account_name='Raw Meterials',Account_desc='Raw Meterials Exp').save()

    company = company_details.objects.get(user = request.user)
    context = {
                'company' : company
            }
    return render(request,'loginhome.html',context)


@login_required(login_url='login')
def view_profile(request):

    company = company_details.objects.get(user = request.user)
    context = {
                'company' : company
            }
    return render(request,'profile.html',context)

@login_required(login_url='login')
def edit_profile(request,pk):

    company = company_details.objects.get(id = pk)
    user1 = User.objects.get(id = company.user_id)

    if request.method == "POST":

        user1.first_name = capfirst(request.POST.get('f_name'))
        user1.last_name  = capfirst(request.POST.get('l_name'))
        user1.username = request.POST.get('uname')
        # pat.age = request.POST.get('age')
        # pat.address = capfirst(request.POST.get('address'))
        # pat.gender = request.POST.get('gender')
        # user1.email = request.POST.get('email')
        # pat.email = request.POST.get('email')
        # pat.contact_num = request.POST.get('cnum')
        # #fkey1= request.POST.get('doc')
        # #pat.doctor = doctor.objects.get(id = fkey1)
        # if len(request.FILES)!=0 :
        #     doc.profile_pic = request.FILES.get('file')


        company.save()
        user1.save()
        return redirect('view_profile')

    context = {
        'company' : company,
        'user1' : user1,
    }
    context = {
                'company' : company,
            }
    return render(request,'edit_profile.html',context)

@login_required(login_url='login')
def itemview(request):
    viewitem=AddItem.objects.all()
    return render(request,'item_view.html',{'view':viewitem})


@login_required(login_url='login')
def additem(request):
    unit=Unit.objects.all()
    sale=Sales.objects.all()
    purchase=Purchase.objects.all()
    
    


  
    
        



    accounts = Purchase.objects.all()
    account_types = set(Purchase.objects.values_list('Account_type', flat=True))

    
    account = Sales.objects.all()
    account_type = set(Sales.objects.values_list('Account_type', flat=True))
    
    

    return render(request,'additem.html',{'unit':unit,'sale':sale,'purchase':purchase,
               
                            "account":account,"account_type":account_type,"accounts":accounts,"account_types":account_types,
                            
                            })

@login_required(login_url='login')
def add_account(request):
    if request.method=='POST':
        Account_type  =request.POST['acc_type']
        Account_name =request.POST['acc_name']
        Account_desc =request.POST['acc_desc']
       
        acc=Purchase(Account_type=Account_type,Account_name=Account_name,Account_desc=Account_desc)
        acc.save()                 
        return redirect("additem")
        
    return render(request,'additem.html')


@login_required(login_url='login')
def add(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            radio=request.POST.get('radio')
            if radio=='tax':
    
                
                inter=request.POST['inter']
                intra=request.POST['intra']
                type=request.POST.get('type')
                name=request.POST['name']
                unit=request.POST['unit']
                sel_price=request.POST.get('sel_price')
                sel_acc=request.POST.get('sel_acc')
                s_desc=request.POST.get('sel_desc')
                cost_price=request.POST.get('cost_price')
                cost_acc=request.POST.get('cost_acc')      
                p_desc=request.POST.get('cost_desc')
                u=request.user.id
                us=request.user
                history="Created by" + str(us)
                user=User.objects.get(id=u)
                unit=Unit.objects.get(id=unit)
                sel=Sales.objects.get(id=sel_acc)
                cost=Purchase.objects.get(id=cost_acc)
                ad_item=AddItem(type=type,Name=name,p_desc=p_desc,s_desc=s_desc,s_price=sel_price,p_price=cost_price,unit=unit,
                            sales=sel,purchase=cost,user=user,creat=history,interstate=inter,intrastate=intra
                                )
                
            else:
                                                  
                type=request.POST.get('type')
                name=request.POST['name']
                unit=request.POST['unit']
                sel_price=request.POST.get('sel_price')
                sel_acc=request.POST.get('sel_acc')
                s_desc=request.POST.get('sel_desc')
                cost_price=request.POST.get('cost_price')
                cost_acc=request.POST.get('cost_acc')      
                p_desc=request.POST.get('cost_desc')
                u=request.user.id
                us=request.user
                history="Created by" + str(us)
                user=User.objects.get(id=u)
                unit=Unit.objects.get(id=unit)
                sel=Sales.objects.get(id=sel_acc)
                cost=Purchase.objects.get(id=cost_acc)
                ad_item=AddItem(type=type,Name=name,p_desc=p_desc,s_desc=s_desc,s_price=sel_price,p_price=cost_price,unit=unit,
                            sales=sel,purchase=cost,user=user,creat=history,interstate='none',intrastate='none'
                                )
                ad_item.save()
            ad_item.save()
           
            return redirect("itemview")
    return render(request,'additem.html')



@login_required(login_url='login')
def edititem(request,id):
    pedit=AddItem.objects.get(id=id)
    p=Purchase.objects.all()
    s=Sales.objects.all()
    u=Unit.objects.all()

    accounts = Purchase.objects.all()
    account_types = set(Purchase.objects.values_list('Account_type', flat=True))
    

    
    account = Sales.objects.all()
    account_type = set(Sales.objects.values_list('Account_type', flat=True))
    
    return render(request,'edititem.html',{"account":account,"account_type":account_type,'e':pedit,'p':p,'s':s,'u':u,"accounts":accounts,"account_types":account_types})


@login_required(login_url='login')
def edit_db(request,id):
        if request.method=='POST':
            edit=AddItem.objects.get(id=id)
            edit.type=request.POST.get('type')
            edit.Name=request.POST['name']
            unit=request.POST['unit']
            edit.s_price=request.POST['sel_price']
            sel_acc=request.POST['sel_acc']
            edit.s_desc=request.POST['sel_desc']
            edit.p_price=request.POST['cost_price']
            cost_acc=request.POST['cost_acc']        
            edit.p_desc=request.POST['cost_desc']
            
            
            edit.unit=Unit.objects.get(id=unit)
            edit.sales=Sales.objects.get(id=sel_acc)
            edit.purchase=Purchase.objects.get(id=cost_acc)
            edit.save()
            return redirect('itemview')

        return render(request,'edititem.html')


@login_required(login_url='login')
def detail(request,id):
    user_id=request.user
    items=AddItem.objects.all()
    product=AddItem.objects.get(id=id)
    history=History.objects.filter(p_id=product.id)
    print(product.id)
    
    
    context={
       "allproduct":items,
       "product":product,
       "history":history,
      
    }
    
    return render(request,'demo.html',context)


@login_required(login_url='login')
def Action(request,id):
    user=request.user.id
    user=User.objects.get(id=user)
    viewitem=AddItem.objects.all()
    event=AddItem.objects.get(id=id)
    

    print(user)
    if request.method=='POST':
        action=request.POST['action']
        event.satus=action
        event.save()
        if action == 'active':
            History(user=user,message="Item marked as Active ",p=event).save()
        else:
            History(user=user,message="Item marked as inActive",p=event).save()
    return render(request,'item_view.html',{'view':viewitem})

@login_required(login_url='login')
def cleer(request,id):
    dl=AddItem.objects.get(id=id)
    dl.delete()
    return redirect('itemview')


@login_required(login_url='login')
def add_unit(request):
    if request.method=='POST':
        unit_name=request.POST['unit_name']
        Unit(unit=unit_name).save()
        return redirect('additem')
    return render(request,"additem.html")


@login_required(login_url='login')
def add_sales(request):
    if request.method=='POST':
        Account_type  =request.POST['acc_type']
        Account_name =request.POST['acc_name']
        Acount_code =request.POST['acc_code']
        Account_desc =request.POST['acc_desc']        
        acc=Sales(Account_type=Account_type,Account_name=Account_name,Acount_code=Acount_code,Account_desc=Account_desc)
        acc.save()
        return redirect('additem')
    return render(request,'additem.html')
        

def sample(request):
    print("hello")
    return redirect('base')

def view_vendor_list(request):
    user_id=request.user.id
    udata=User.objects.get(id=user_id)
    data=vendor_table.objects.filter(user=udata)
    return render(request,'vendor_list.html',{'data':data})

def view_vendor_details(request,pk):
    user_id=request.user.id
    udata=User.objects.get(id=user_id)
    vdata1=vendor_table.objects.filter(user=udata)
    vdata2=vendor_table.objects.get(id=pk)
    mdata=mail_table.objects.filter(vendor=vdata2)
    ddata=doc_upload_table.objects.filter(user=udata,vendor=vdata2)

    return render(request,'vendor_details.html',{'vdata':vdata1,'vdata2':vdata2,'mdata':mdata,'ddata':ddata})

def add_comment(request,pk):
    if request.method=='POST':
        comment=request.POST['comment']
        user_id=request.user.id
        udata=User.objects.get(id=user_id)
        vdata2=vendor_table.objects.get(id=pk)
        comments=comments_table(user=udata,vendor=vdata2,comment=comment)
        comments.save()
        return redirect("view_vendor_list")

def sendmail(request,pk):
    if request.method=='POST':
        user_id=request.user.id
        udata=User.objects.get(id=user_id)
        vdata2=vendor_table.objects.get(id=pk)
        mail_from=settings.EMAIL_HOST_USER
        mail_to=request.POST['email']
        subject=request.POST['subject']
        content=request.POST['content']
        mail_data=mail_table(user=udata,vendor=vdata2,mail_from=mail_from,mail_to=mail_to,subject=subject,content=content)
        mail_data.save()

        subject = request.POST['subject']
        message = request.POST['content']
        recipient = request.POST['email']     #  recipient =request.POST["inputTagName"]
        send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient])

        return redirect("view_vendor_list")



def edit_vendor(request,pk):
    vdata=vendor_table.objects.get(id=pk)
    if remarks_table.objects.filter(vendor=vdata).exists() or contact_person_table.objects.filter(vendor=vdata).exists():
        if remarks_table.objects.filter(vendor=vdata).exists() and contact_person_table.objects.filter(vendor=vdata).exists():
            rdata=remarks_table.objects.get(vendor=vdata)
            pdata=contact_person_table.objects.filter(vendor=vdata)
            return render(request,'edit_vendor.html',{'vdata':vdata,'rdata':rdata,'pdata':pdata})
        else:
            if remarks_table.objects.filter(vendor=vdata).exists():
                rdata=remarks_table.objects.get(vendor=vdata)
                return render(request,'edit_vendor.html',{'vdata':vdata,'rdata':rdata})
            if contact_person_table.objects.filter(vendor=vdata).exists():
                pdata=contact_person_table.objects.filter(vendor=vdata)
                return render(request,'edit_vendor.html',{'vdata':vdata,'pdata':pdata})      
        
    else:
        return render(request,'edit_vendor.html',{'vdata':vdata})


def edit_vendor_details(request,pk):
    if request.method=='POST':
        vdata=vendor_table.objects.get(id=pk)
        vdata.salutation=request.POST['salutation']
        vdata.first_name=request.POST['first_name']
        vdata.last_name=request.POST['last_name']
        vdata.company_name=request.POST['company_name']
        vdata.vendor_display_name=request.POST['v_display_name']
        vdata.vendor_email=request.POST['vendor_email']
        vdata.vendor_wphone=request.POST['w_phone']
        vdata.vendor_mphone=request.POST['m_phone']
        vdata.skype_number=request.POST['skype_number']
        vdata.designation=request.POST['designation']
        vdata.department=request.POST['department']
        vdata.website=request.POST['website']
        vdata.gst_treatment=request.POST['gst']
        if vdata.gst_treatment=="Unregistered Business-not Registered under GST":
            vdata.pan_number=request.POST['pan_number']
            vdata.gst_number="null"
        else:
            vdata.gst_number=request.POST['gst_number']
            vdata.pan_number=request.POST['pan_number']

        vdata.source_supply=request.POST['source_supply']
        vdata.currency=request.POST['currency']
        vdata.opening_bal=request.POST['opening_bal']
        vdata.payment_terms=request.POST['payment_terms']

        vdata.battention=request.POST['battention']
        vdata.bcountry=request.POST['bcountry']
        vdata.baddress=request.POST['baddress']
        vdata.bcity=request.POST['bcity']
        vdata.bstate=request.POST['bstate']
        vdata.bzip=request.POST['bzip']
        vdata.bphone=request.POST['bphone']
        vdata.bfax=request.POST['bfax']

        vdata.sattention=request.POST['sattention']
        vdata.scountry=request.POST['scountry']
        vdata.saddress=request.POST['saddress']
        vdata.scity=request.POST['scity']
        vdata.sstate=request.POST['sstate']
        vdata.szip=request.POST['szip']
        vdata.sphone=request.POST['sphone']
        vdata.sfax=request.POST['sfax']

        vdata.save()
             # .................................edit remarks_table ..........................
        vendor=vdata
        user_id=request.user.id
        udata=User.objects.get(id=user_id)
        if remarks_table.objects.filter(vendor=vdata).exists():
            rdata=remarks_table.objects.get(vendor=vdata)
            rdata.remarks=request.POST['remark']
            rdata.save()
        else:
            rdata=remarks_table()
            rdata.remarks=request.POST["remark"]
            rdata.vendor=vendor
            rdata.user=udata
            rdata.save()

            # .......................contact_person_table................ deleting existing entries and inserting  ...............

        pdata=contact_person_table.objects.filter(vendor=vdata)
        salutation =request.POST.getlist('salutation[]')
        first_name =request.POST.getlist('first_name[]')
        last_name =request.POST.getlist('last_name[]')
        email =request.POST.getlist('email[]')
        work_phone =request.POST.getlist('wphone[]')
        mobile =request.POST.getlist('mobile[]')
        skype_number =request.POST.getlist('skype[]')
        designation =request.POST.getlist('designation[]')
        department =request.POST.getlist('department[]') 

        vdata=vendor_table.objects.get(id=vdata.id)
        vendor=vdata
        user_id=request.user.id
        udata=User.objects.get(id=user_id)

        # .....  deleting existing rows......
        pdata.delete()
        if len(salutation)==len(first_name)==len(last_name)==len(email)==len(work_phone)==len(mobile)==len(skype_number)==len(designation)==len(department):
            mapped2=zip(salutation,first_name,last_name,email,work_phone,mobile,skype_number,designation,department)
            mapped2=list(mapped2)
            print(mapped2)
            for ele in mapped2:
                created = contact_person_table.objects.get_or_create(salutation=ele[0],first_name=ele[1],last_name=ele[2],email=ele[3],
                         work_phone=ele[4],mobile=ele[5],skype_number=ele[6],designation=ele[7],department=ele[8],user=udata,vendor=vendor)
        



        return redirect("view_vendor_list")

def upload_document(request,pk):
    if request.method=='POST':
        user_id=request.user.id
        udata=User.objects.get(id=user_id)
        vdata=vendor_table.objects.get(id=pk)
        title=request.POST['title']
        document=request.FILES.get('file')
        doc_data=doc_upload_table(user=udata,vendor=vdata,title=title,document=document)
        doc_data.save()
        return redirect("view_vendor_list")

def download_doc(request,pk):
    document=get_object_or_404(doc_upload_table,id=pk)
    response=HttpResponse(document.document,content_type='application/pdf')
    response['Content-Disposition']=f'attachment; filename="{document.document.name}"'
    return response

def cancel_vendor(request):
    return redirect("view_vendor_list")

def delete_vendor(request,pk):
    if comments_table.objects.filter(vendor=pk).exists():
        user2=comments_table.objects.filter(vendor=pk)
        user2.delete()
    if mail_table.objects.filter(vendor=pk).exists():
        user3=mail_table.objects.filter(vendor=pk)
        user3.delete()
    if doc_upload_table.objects.filter(vendor=pk).exists():
        user4=doc_upload_table.objects.filter(vendor=pk)
        user4.delete()
    if contact_person_table.objects.filter(vendor=pk).exists():
        user5=contact_person_table.objects.filter(vendor=pk)
        user5.delete()
    if remarks_table.objects.filter(vendor=pk).exists():
        user6=remarks_table.objects.filter(vendor=pk)
        user6.delete()
    
    user1=vendor_table.objects.get(id=pk)
    user1.delete()
    return redirect("view_vendor_list")
    
    

# view functions for retainer invoice

@login_required(login_url='login')
def add_customer(request):
    if request.method=='POST':
        customer_name=request.POST['name']
        address=request.POST['address']
        customer=customer(customer_name=customer_name,customer_address=address)
        customer.save()
        return redirect('add_invoice')
    return render(request,'add_customer.html')


@login_required(login_url='login')
def retainer_invoice(request):
    invoices=RetainerInvoice.objects.all()
    context={'invoices':invoices}
    return render(request,'retainer_invoice.html',context)



@login_required(login_url='login')
def add_invoice(request):
    customer=customer.objects.all()   
    context={'customer':customer,}    
    return render(request,'add_invoice.html',context)

@login_required(login_url='login')
def create_invoice_draft(request):
    
    if request.method=='POST':
        select=request.POST['select']
        customer_name=customer.objects.get(id=select)
        retainer_invoice_number=request.POST['retainer-invoice-number']
        references=request.POST['references']
        retainer_invoice_date=request.POST['invoicedate']
        total_amount=request.POST.get('total')
        customer_notes=request.POST['customer_notes']
        terms_and_conditions=request.POST['terms']
    
        retainer_invoice=RetainerInvoice(
            customer_name=customer_name,retainer_invoice_number=retainer_invoice_number,refrences=references,retainer_invoice_date=retainer_invoice_date,total_amount=total_amount,customer_notes=customer_notes,terms_and_conditions=terms_and_conditions)
    
        retainer_invoice.save()
        

        description = request.POST.getlist('description[]')
        amount =request.POST.getlist('amount[]')
        if len(description)==len(amount):
            mapped = zip(description,amount)
            mapped=list(mapped)
            for ele in mapped:
                created = Retaineritems.objects.get_or_create(description=ele[0],amount=ele[1], retainer=retainer_invoice)
        else:
            pass

        return redirect('retainer_invoice')

            
        

         
@login_required(login_url='login')
def create_invoice_send(request):
    if request.method=='POST':
        select=request.POST['select']
        customer_name=customer.objects.get(id=select)
        retainer_invoice_number=request.POST['retainer-invoice-number']
        references=request.POST['references']
        retainer_invoice_date=request.POST['invoicedate']
        total_amount=request.POST.get('total')
        customer_notes=request.POST['customer_notes']
        terms_and_conditions=request.POST['terms']
        retainer_invoice=RetainerInvoice(
        customer_name=customer_name,retainer_invoice_number=retainer_invoice_number,refrences=references,retainer_invoice_date=retainer_invoice_date,total_amount=total_amount,customer_notes=customer_notes,terms_and_conditions=terms_and_conditions,is_draft=False)
        retainer_invoice.save()

        description = request.POST.getlist('description[]')
        amount = request.POST.getlist('amount[]')
        if len(description)==len(amount):
            mapped = zip(description,amount)
            mapped=list(mapped)
            for ele in mapped:
                created = Retaineritems.objects.get_or_create(description=ele[0],amount=ele[1], retainer=retainer_invoice)
        else:
            pass
        return redirect('invoice_view',pk=retainer_invoice.id)



@login_required(login_url='login')
def invoice_view(request,pk):
    invoices=RetainerInvoice.objects.all()
    invoice=RetainerInvoice.objects.get(id=pk)
    item=Retaineritems.objects.filter(retainer=pk)

    context={'invoices':invoices,'invoice':invoice,'item':item}
    return render(request,'invoice_view.html',context)

@login_required(login_url='login')
def retainer_template(request,pk):
    invoice=RetainerInvoice.objects.get(id=pk)
    return render(request,'template.html',{'invoice':invoice})

@login_required(login_url='login')
def retainer_edit_page(request,pk):
    invoice=RetainerInvoice.objects.get(id=pk)
    customer=customer.objects.all()
    items=Retaineritems.objects.filter(retainer=pk)
    context={'invoice':invoice, 'customer':customer,'items':items}
    return render(request,'retainer_invoice_edit.html', context)


@login_required(login_url='login')
def retainer_update(request,pk):

    if request.method=='POST':
        retainer_invoice=RetainerInvoice.objects.get(id=pk)
        select=request.POST['select']
        retainer_invoice.customer_name=customer.objects.get(id=select)
        retainer_invoice.retainer_invoice_number=request.POST['retainer-invoice-number']
        retainer_invoice.refrences=request.POST['references']
        retainer_invoice.retainer_invoice_date=request.POST['invoicedate']
        retainer_invoice.total_amount=request.POST.get('total')
        retainer_invoice.customer_notes=request.POST['customer_notes']
        retainer_invoice.terms_and_conditions=request.POST['terms']
    
        retainer_invoice.save()
        
        descriptions=request.POST.getlist('description[]')
        amounts=request.POST.getlist('amount[]')
        # if len(descriptions)==len(amounts):
        #     mapped = zip(descriptions,amounts)
        #     mapped=list(mapped)
        #     for ele in mapped:
        #         created=Retaineritems.objects.filter(retainer=retainer_invoice).update(description=ele[0])
        # else:
        #     pass
        for i in range(len(descriptions)):
            description=descriptions[i]
            amount=amounts[i]
            obj,created=Retaineritems.objects.update_or_create(retainer=retainer_invoice,description=description,defaults={'amount':amount})
            obj.save()





        return redirect('retainer_invoice')

@login_required(login_url='login')
def mail_send(request,pk):

    if request.method=='POST':
        comments=request.POST.getlist('mailcomments')
        print(comments)
        files=request.FILES.getlist('files')
        email_to='alenantony32@gmail.com'
        subject='Retainer Invoice'
        message1=f'Please keep the attached\nretainer invoice for future use.\n\ncomments:\n'
        message2='' 

        for comment in comments:
            message2 += comment + '\n'

        messages=message1+message2    


        email=EmailMessage(
            subject=subject,
            body=messages,
            to=[email_to]
        )
        
        for file in files:
            email.attach(file.name, file.read(), file.content_type)

        email.send() 
        print('bottom') 
        retainer_invoice=RetainerInvoice.objects.get(id=pk)
        retainer_invoice.is_draft=False
        retainer_invoice.is_sent=True
        retainer_invoice.save()  
        return redirect('retainer_invoice')
    
    return redirect('retainer_invoice')

@login_required(login_url='login')
def retaineritem_delete(request,pk):
    print('delete')
    item = get_object_or_404(Retaineritems, id=pk)
    item.delete()
    print('deleted')
    return redirect('retainer_edit_page' ,pk=item.retainer.id)
    
@login_required(login_url='login')
def retainer_delete(request,pk):
    items=Retaineritems.objects.filter(retainer=pk)
    items.delete()
    retainer=RetainerInvoice.objects.get(id=pk)
    retainer.delete()
    return redirect('retainer_invoice')
        
            
def allestimates(request):
    user = request.user
    estimates = Estimates.objects.filter(user=user).order_by('-id')
    company = company_details.objects.get(user=user)
    context = {
        'estimates': estimates,
        'company': company,
    }
    # for i in estimates:
    #     print(i)

    return render(request, 'all_estimates.html', context)





def newestimate(request):
    user = request.user
    # print(user_id)
    company = company_details.objects.get(user=user)
    items = AddItem.objects.filter(user_id=user.id)
    customers = customer.objects.filter(user_id=user.id)
    estimates_count = Estimates.objects.count()
    next_count = estimates_count+1
    context = {'company': company,
               'items': items,
               'customers': customers,
               'count': next_count,
               }

    return render(request, 'new_estimate.html', context)


def itemdata_est(request):
    cur_user = request.user
    user = User.objects.get(id=cur_user.id)
    company = company_details.objects.get(user=user)
    # print(company.state)
    id = request.GET.get('id')
    cust = request.GET.get('cust')
    print(id)
    print(cust)

    item = AddItem.objects.get(Name=id, user=user)

    rate = item.p_price
    place = company.state
    gst = item.intrastate
    igst = item.interstate
    place_of_supply = customer.objects.get(
        customerName=cust, user=user).placeofsupply
    return JsonResponse({"status": " not", 'place': place, 'rate': rate, 'pos': place_of_supply, 'gst': gst, 'igst': igst})
    return redirect('/')


def createestimate(request):
    print('hi1')
    cur_user = request.user
    user = User.objects.get(id=cur_user.id)
    print('hi1')
    if request.method == 'POST':
        cust_name = request.POST['customer_name']
        est_number = request.POST['estimate_number']
        reference = request.POST['reference']
        est_date = request.POST['estimate_date']
        exp_date = request.POST['expiry_date']

        item = request.POST.getlist('item[]')
        quantity = request.POST.getlist('quantity[]')
        rate = request.POST.getlist('rate[]')
        discount = request.POST.getlist('discount[]')
        tax = request.POST.getlist('tax[]')
        amount = request.POST.getlist('amount[]')
        # print(item)
        # print(quantity)
        # print(rate)
        # print(discount)
        # print(tax)
        # print(amount)

        cust_note = request.POST['customer_note']
        sub_total = request.POST['subtotal']
        igst = request.POST['igst']
        sgst = request.POST['sgst']
        cgst = request.POST['cgst']
        tax_amnt = request.POST['total_taxamount']
        shipping = request.POST['shipping_charge']
        adjustment = request.POST['adjustment_charge']
        total = request.POST['total']
        tearms_conditions = request.POST['tearms_conditions']
        attachment = request.FILES.get('file')
        status = 'Draft'

        estimate = Estimates(user=user, customer_name=cust_name, estimate_no=est_number, reference=reference, estimate_date=est_date, 
                             expiry_date=exp_date, sub_total=sub_total,igst=igst,sgst=sgst,cgst=cgst,tax_amount=tax_amnt, shipping_charge=shipping,
                             adjustment=adjustment, total=total, status=status, customer_notes=cust_note, terms_conditions=tearms_conditions, 
                             attachment=attachment)
        estimate.save()

        if len(item) == len(quantity) == len(rate) == len(discount) == len(tax) == len(amount):
            mapped = zip(item, quantity, rate, discount, tax, amount)
            mapped = list(mapped)
            for element in mapped:
                created = EstimateItems.objects.get_or_create(
                    estimate=estimate, item_name=element[0], quantity=element[1], rate=element[2], discount=element[3], tax_percentage=element[4], amount=element[5])
    return redirect('newestimate')


def create_and_send_estimate(request):
    cur_user = request.user
    user = User.objects.get(id=cur_user.id)
    print("hello")
    if request.method == 'POST':
        cust_name = request.POST['customer_name']
        est_number = request.POST['estimate_number']
        reference = request.POST['reference']
        est_date = request.POST['estimate_date']
        exp_date = request.POST['expiry_date']

        item = request.POST.getlist('item[]')
        quantity1 = request.POST.getlist('quantity[]')
        quantity = [float(x) for x in quantity1]
        rate1 = request.POST.getlist('rate[]')
        rate = [float(x) for x in rate1]
        discount1 = request.POST.getlist('discount[]')
        discount = [float(x) for x in discount1]
        tax1 = request.POST.getlist('tax[]')
        tax = [float(x) for x in tax1]
        amount1 = request.POST.getlist('amount[]')
        amount = [float(x) for x in amount1]
        print(item)
        print(quantity)
        print(rate)
        print(discount)
        print(tax)
        print(amount)

        cust_note = request.POST['customer_note']
        sub_total = float(request.POST['subtotal'])
        igst = float(request.POST['igst'])
        sgst = float(request.POST['sgst'])
        cgst = float(request.POST['cgst'])
        tax_amnt = float(request.POST['total_taxamount'])
        shipping = float(request.POST['shipping_charge'])
        adjustment = float(request.POST['adjustment_charge'])
        total = float(request.POST['total'])
        tearms_conditions = request.POST['tearms_conditions']
        attachment = request.FILES.get('file')
        status = 'Sent'
        tot_in_string = str(total)

        estimate = Estimates(user=user, customer_name=cust_name, estimate_no=est_number, reference=reference, estimate_date=est_date, 
                             expiry_date=exp_date, sub_total=sub_total,igst=igst,sgst=sgst,cgst=cgst,tax_amount=tax_amnt, shipping_charge=shipping,
                             adjustment=adjustment, total=total, status=status, customer_notes=cust_note, terms_conditions=tearms_conditions, 
                             attachment=attachment)
        estimate.save()

        if len(item) == len(quantity) == len(rate) == len(discount) == len(tax) == len(amount):
            mapped = zip(item, quantity, rate, discount, tax, amount)
            mapped = list(mapped)
            for element in mapped:
                created = EstimateItems.objects.get_or_create(
                    estimate=estimate, item_name=element[0], quantity=element[1], rate=element[2], discount=element[3], tax_percentage=element[4], amount=element[5])

        cust_email = customer.objects.get(
            user=user, customerName=cust_name).customerEmail
        print(cust_email)
        subject = 'Estimate'
        message = 'Dear Customer,\n Your Estimate has been Saved for a total amount of: ' + tot_in_string
        recipient = cust_email
        send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient])

    return redirect('newestimate')

def estimateslip(request, est_id):
    user = request.user
    company = company_details.objects.get(user=user)
    all_estimates = Estimates.objects.filter(user=user)
    estimate = Estimates.objects.get(id=est_id)
    items = EstimateItems.objects.filter(estimate=estimate)
    context = {
        'company': company,
        'all_estimates':all_estimates,
        'estimate': estimate,
        'items': items,
    }
    return render(request, 'estimate_slip.html', context)




def editestimate(request,est_id):
    user = request.user
    company = company_details.objects.get(user=user)
    customers = customer.objects.filter(user_id=user.id)
    items = AddItem.objects.filter(user_id=user.id)
    estimate = Estimates.objects.get(id=est_id)
    est_items = EstimateItems.objects.filter(estimate=estimate)
    context = {
        'company': company,
        'estimate': estimate,
        'customers': customers,
        'items': items,
        'est_items': est_items,
    }
    return render(request, 'edit_estimate.html', context)

def updateestimate(request,pk):
    cur_user = request.user
    user = User.objects.get(id=cur_user.id)

    if request.method == 'POST':
        estimate = Estimates.objects.get(id=pk)
        estimate.user = user
        estimate.customer_name = request.POST['customer_name']
        estimate.estimate_no = request.POST['estimate_number']
        estimate.reference = request.POST['reference']
        estimate.estimate_date = request.POST['estimate_date']
        estimate.expiry_date = request.POST['expiry_date']

        estimate.customer_notes = request.POST['customer_note']
        estimate.sub_total = float(request.POST['subtotal'])
        estimate.tax_amount = float(request.POST['total_taxamount'])
        estimate.shipping_charge = float(request.POST['shipping_charge'])
        estimate.adjustment = float(request.POST['adjustment_charge'])
        estimate.total = float(request.POST['total'])
        estimate.terms_conditions = request.POST['tearms_conditions']
        estimate.status = 'Draft'

        old=estimate.attachment
        new=request.FILES.get('file')
        if old != None and new == None:
            estimate.attachment = old
        else:
            estimate.attachment = new

        estimate.save()

        item = request.POST.getlist('item[]')
        quantity1 = request.POST.getlist('quantity[]')
        quantity = [float(x) for x in quantity1]
        rate1 = request.POST.getlist('rate[]')
        rate = [float(x) for x in rate1]
        discount1 = request.POST.getlist('discount[]')
        discount = [float(x) for x in discount1]
        tax1 = request.POST.getlist('tax[]')
        tax = [float(x) for x in tax1]
        amount1 = request.POST.getlist('amount[]')
        amount = [float(x) for x in amount1]
        # print(item)
        # print(quantity)
        # print(rate)
        # print(discount)
        # print(tax)
        # print(amount)

        objects_to_delete = EstimateItems.objects.filter(estimate_id=estimate.id)
        objects_to_delete.delete()

        
        if len(item) == len(quantity) == len(rate) == len(discount) == len(tax) == len(amount):
            mapped = zip(item, quantity, rate, discount, tax, amount)
            mapped = list(mapped)
            for element in mapped:
                created = EstimateItems.objects.get_or_create(
                    estimate=estimate, item_name=element[0], quantity=element[1], rate=element[2], discount=element[3], tax_percentage=element[4], amount=element[5])
    return redirect('allestimates')

def converttoinvoice(request,est_id):
    user = request.user
    company = company_details.objects.get(user=user)
    estimate = Estimates.objects.get(id=est_id)
    items = EstimateItems.objects.filter(estimate=estimate)
    cust = customer.objects.get(customerName=estimate.customer_name,user=user)
    invoice_count = invoice.objects.count()
    next_no = invoice_count+1 
    inv = invoice(customer=cust,invoice_no=next_no,terms='null',order_no=estimate.estimate_no,
                      inv_date=estimate.estimate_date,due_date=estimate.expiry_date,igst=estimate.igst,cgst=estimate.cgst,
                      sgst=estimate.sgst,t_tax=estimate.tax_amount,subtotal=estimate.sub_total,grandtotal=estimate.total,
                      cxnote=estimate.customer_notes,file=estimate.attachment,terms_condition=estimate.terms_conditions,
                      status=estimate.status)
    inv.save()
    inv = invoice.objects.get(invoice_no=next_no,customer=cust)
    for item in items:
        items = invoice_item(product=item.item_name,quantity=item.quantity,hsn='null',tax=item.tax_percentage,
                             total=item.amount,desc=item.discount,rate=item.rate,inv=inv)
        items.save()
    return redirect('allestimates')

class EmailAttachementView(View):
    form_class = EmailForm
    template_name = 'newmail.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'email_form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            files = request.FILES.getlist('attach')

            try:
                mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
                for f in files:
                    mail.attach(f.name, f.read(), f.content_type)
                mail.send()
                return render(request, self.template_name, {'email_form': form, 'error_message': 'Sent email to %s'%email})
            except:
                return render(request, self.template_name, {'email_form': form, 'error_message': 'Either the attachment is too big or corrupt'})

        return render(request, self.template_name, {'email_form': form, 'error_message': 'Unable to send email. Please try again later'})



def add_customer_for_estimate(request):   
    return render(request,'createinvoice.html',{'sb':sb})
    
def entr_custmr_for_estimate(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            type=request.POST.get('type')
            txtFullName=request.POST['txtFullName']
            cpname=request.POST['cpname']
           
            email=request.POST.get('myEmail')
            wphone=request.POST.get('wphone')
            mobile=request.POST.get('mobile')
            skname=request.POST.get('skname')
            desg=request.POST.get('desg')      
            dept=request.POST.get('dept')
            wbsite=request.POST.get('wbsite')

            gstt=request.POST.get('gstt')
            posply=request.POST.get('posply')
            tax1=request.POST.get('tax1')
            crncy=request.POST.get('crncy')
            obal=request.POST.get('obal')

            select=request.POST.get('pterms')
            pterms=payment_terms.objects.get(id=select)
            pterms=request.POST.get('pterms')

            plst=request.POST.get('plst')
            plang=request.POST.get('plang')
            fbk=request.POST.get('fbk')
            twtr=request.POST.get('twtr')
        
            atn=request.POST.get('atn')
            ctry=request.POST.get('ctry')
            
            addrs=request.POST.get('addrs')
            addrs1=request.POST.get('addrs1')
            bct=request.POST.get('bct')
            bst=request.POST.get('bst')
            bzip=request.POST.get('bzip')
            bpon=request.POST.get('bpon')
            bfx=request.POST.get('bfx')

            sal=request.POST.get('sal')
            ftname=request.POST.get('ftname')
            ltname=request.POST.get('ltname')
            mail=request.POST.get('mail')
            bworkpn=request.POST.get('bworkpn')
            bmobile=request.POST.get('bmobile')

            bskype=request.POST.get('bskype')
            bdesg=request.POST.get('bdesg')
            bdept=request.POST.get('bdept')
            u = User.objects.get(id = request.user.id)

          
            ctmr=customer(customerName=txtFullName,customerType=type,
                        companyName=cpname,customerEmail=email,customerWorkPhone=wphone,
                         customerMobile=mobile,skype=skname,designation=desg,department=dept,
                           website=wbsite,GSTTreatment=gstt,placeofsupply=posply, Taxpreference=tax1,
                             currency=crncy,OpeningBalance=obal,PaymentTerms=pterms,
                                PriceList=plst,PortalLanguage=plang,Facebook=fbk,Twitter=twtr,
                                 Attention=atn,country=ctry,Address1=addrs,Address2=addrs1,
                                  city=bct,state=bst,zipcode=bzip,phone1=bpon,
                                   fax=bfx,CPsalutation=sal,Firstname=ftname,
                                    Lastname=ltname,CPemail=mail,CPphone=bworkpn,
                                    CPmobile= bmobile,CPskype=bskype,CPdesignation=bdesg,
                                     CPdepartment=bdept,user=u )
            ctmr.save()  
            
            return redirect("newestimate")
        return redirect("newestimate")
    
def payment_term_for_estimate(request):
    if request.method=='POST':
        term=request.POST.get('term')
        day=request.POST.get('day')
        ptr=payment_terms(Terms=term,Days=day)
        ptr.save()
        return redirect("add_customer_for_estimate")

    
@login_required(login_url='login')

def payment_term(request):
    if request.method=='POST':
        term=request.POST.getlist('terms[]')
        day=request.POST.getlist('days[]')
        if len(term)==len(day):
            mapped = zip(term,day)
            mapped = list(mapped)
            for ele in mapped:
                created = payment_terms.objects.get_or_create(Terms=ele[0],Days=ele[1])
            return redirect('add_prod')
    return redirect("add_customer")

@login_required(login_url='login')

def invoiceview(request):
    invoicev=invoice.objects.all()
    
    if not payment_terms.objects.filter(Terms='net 15').exists(): 
       payment_terms(Terms='net 15',Days=15).save()
    if not payment_terms.objects.filter(Terms='due end of month').exists():
        payment_terms(Terms='due end of month',Days=60).save()
    elif not  payment_terms.objects.filter(Terms='net 30').exists():
        payment_terms(Terms='net 30',Days=30).save() 
    
    
    context={
        'invoice':invoicev,
        
    }
    return render(request,'invoiceview.html',context)

@login_required(login_url='login')

def detailedview(request,id):
    inv_dat=invoice.objects.all()
    inv_master=invoice.objects.get(id=id)
    invoiceitem=invoice_item.objects.filter(inv_id=id)
    company=company_details.objects.get(user_id=request.user.id)
    
    
    context={
        'inv_dat':inv_dat,
        'invoiceitem':invoiceitem,
        'comp':company,
        'invoice':inv_master,
        
                    }
    return render(request,'invoice_det.html',context)



@login_required(login_url='login')

def dele(request,pk):
    d=invoice.objects.get(id=pk)
    d.delete()
    return redirect('invoiceview')

@login_required(login_url='login')

def addinvoice(request):
    c=customer.objects.all()
    p=AddItem.objects.all()
    i=invoice.objects.all()
    pay=payment.objects.all()
    if not payment.objects.filter(term='net 15').exists(): 
       payment(term='net 15',days=15).save()
    if not payment.objects.filter(term='due end of month').exists():
        payment(term='due end of month',days=60).save()
    elif not  payment.objects.filter(term='net 30').exists():
        payment(term='net 30',days=30).save() 
    


    
            
            
            
            
    context={
        'c':c,
        'p':p,
        'i':i,
        'pay':pay,
        
    }
       
    return render(request,'createinvoice.html',context)


@login_required(login_url='login')

def add_prod(request):
    c=customer.objects.all()
    p=AddItem.objects.all()
    i=invoice.objects.all()
    pay=payment_terms.objects.all()
    if not payment_terms.objects.filter(Terms='net 15').exists(): 
       payment_terms(Terms='net 15',Days=15).save()
    if not payment_terms.objects.filter(Terms='due end of month').exists():
        payment_terms(Terms='due end of month',Days=60).save()
    elif not  payment_terms.objects.filter(Terms='net 30').exists():
        payment_terms(Terms='net 30',Days=30).save() 
    
    
   
    if request.user.is_authenticated:
        if request.method=='POST':
            c=request.POST['cx_name']
            cus=customer.objects.get(customerName=c) 
            print(cus.id)  
            custo=cus.id
            invoice_no=request.POST['inv_no']
            terms=request.POST['term']
            term=payment_terms.objects.get(id=terms)
            order_no=request.POST['ord_no']
            inv_date=request.POST['inv_date']
            due_date=request.POST['due_date']
        
            
            cxnote=request.POST['customer_note']
            subtotal=request.POST['subtotal']
            igst=request.POST['igst']
            cgst=request.POST['cgst']
            sgst=request.POST['sgst']
            totaltax=request.POST['totaltax']
            t_total=request.POST['t_total']
            if request.FILES.get('file') is not None:
                file=request.FILES['file']
            else:
                file="/static/images/alt.jpg"
            tc=request.POST['ter_cond']

            status=request.POST['sd']
            if status=='draft':
                print(status)   
            else:
                print(status)  
        
            product=request.POST.getlist('item[]')
            hsn=request.POST.getlist('hsn[]')
            quantity=request.POST.getlist('quantity[]')
            rate=request.POST.getlist('rate[]')
            desc=request.POST.getlist('desc[]')
            tax=request.POST.getlist('tax[]')
            total=request.POST.getlist('amount[]')
            term=payment_terms.objects.get(id=term.id)

            inv=invoice(customer_id=custo,invoice_no=invoice_no,terms=term,order_no=order_no,inv_date=inv_date,due_date=due_date,
                        cxnote=cxnote,subtotal=subtotal,igst=igst,cgst=cgst,sgst=sgst,t_tax=totaltax,
                        grandtotal=t_total,status=status,terms_condition=tc,file=file)
            inv.save()
            inv_id=invoice.objects.get(id=inv.id)
            if len(product)==len(hsn)==len(quantity)==len(desc)==len(tax)==len(total)==len(rate):

                mapped = zip(product,hsn,quantity,desc,tax,total,rate)
                mapped = list(mapped)
                for element in mapped:
                    created = invoice_item.objects.get_or_create(inv=inv_id,product=element[0],hsn=element[1],
                                        quantity=element[2],desc=element[3],tax=element[4],total=element[5],rate=element[6])
                    
                return redirect('invoiceview')
    context={
            'c':c,
            'p':p,
            'i':i,
            'pay':pay,
    }       
    return render(request,'createinvoice.html',context)


@login_required(login_url='login')

def add_payment(request):
    if request.method=='POST':
            terms=request.POST.get()
    return redirect('add_prod')


@login_required(login_url='login')

def add_cx(request):
    if request.user.is_authenticated:
        if request.method=='POST':
                user=request.user.id
                user=User.objects.get(id=user)
                print(user)
                name=request.POST.get('name')
                email=request.POST.get('email')
                pos=request.POST.get('position')
                state=request.POST.get('state')
                com_name=request.POST.get('company')
                customer(customerName=name,customerEmail=email,placeofsupply=pos,state=state,companyName=com_name,user_id=user.id).save()
        return redirect('add_prod')




@login_required(login_url='login')

def edited_prod(request,id):
    print(id)
    c = customer.objects.all()
    p = AddItem.objects.all()
    invoiceitem = invoice_item.objects.filter(inv_id=id)
    invoic = invoice.objects.get(id=id)
    pay=payment_terms.objects.all()
  
    if request.method == 'POST':
        u=request.user.id
        c=request.POST['cx_name']
        
        cust=customer.objects.get(customerName=c) 
        invoic.customer=cust
        term=request.POST['term']
        
        
        invoic.terms = payment_terms.objects.get(id=term)
        invoic.inv_date = request.POST['inv_date']
        invoic.due_date = request.POST['due_date']
        invoic.cxnote = request.POST['customer_note']
        invoic.subtotal = request.POST['subtotal']
        invoic.igst = request.POST['igst']
        invoic.cgst = request.POST['cgst']
        invoic.sgst = request.POST['sgst']
        invoic.t_tax = request.POST['totaltax']
        invoic.grandtotal = request.POST['t_total']

        if request.FILES.get('file') is not None:
            invoic.file = request.FILES['file']
        else:
            invoic.file = "/static/images/alt.jpg"

            invoic.terms_condition = request.POST.get('ter_cond')
        
        status=request.POST['sd']
        if status=='draft':
            invoic.status=status      
        else:
            invoic.status=status   
         
        invoic.save()
        
        print("/////////////////////////////////////////////////////////")
        product=request.POST.getlist('item[]')
        hsn=request.POST.getlist('hsn[]')
        quantity=request.POST.getlist('quantity[]')
        rate=request.POST.getlist('rate[]')
        desc=request.POST.getlist('desc[]')
        tax=request.POST.getlist('tax[]')
        total=request.POST.getlist('amount[]')
        obj_dele=invoice_item.objects.filter(inv_id=invoic.id)
        obj_dele.delete()
       
        if len(product)==len(hsn)==len(quantity)==len(desc)==len(tax)==len(total)==len(rate):

            mapped = zip(product,hsn,quantity,desc,tax,total,rate)
            mapped = list(mapped)
            for element in mapped:
                created = invoice_item.objects.get_or_create(inv=invoic,product=element[0],hsn=element[1],
                                    quantity=element[2],desc=element[3],tax=element[4],total=element[5],rate=element[6])
                
            return redirect('detailedview',id)
                    
    context = {
            'c': c,
            'p': p,
            'inv': invoiceitem,
            'i': invoic,
            'pay':pay,
        }             
        
    return render(request, 'invoiceedit.html', context)





@login_required(login_url='login')

def edited(request,id):
    c=customer.objects.all()
    p=AddItem.objects.all()
    invoiceitem=invoice_item.objects.filter(inv_id=id)
    inv=invoice.objects.get(id=id)
    context={
        'c':c,
        'p':p,
        'inv':invoiceitem,
        'inv':inv,
        
    }
    
    return render(request,'editinvoice.html')



@login_required(login_url='login')

def itemdata(request):
    cur_user = request.user.id
    user = User.objects.get(id=cur_user)
    company = company_details.objects.get(user = user)
    # print(company.state)
    id = request.GET.get('id')
    cust = request.GET.get('cust')
    
        
    item = AddItem.objects.get(Name=id)
    cus=customer.objects.get(customerName=cust)
    rate = item.s_price
    place=company.state
    gst = item.intrastate
    igst = item.interstate
    desc=item.s_desc
    print(place)
    mail=cus.customerEmail
    
    place_of_supply = customer.objects.get(customerName=cust).placeofsupply
    print(place_of_supply)
    return JsonResponse({"status":" not",'mail':mail,'desc':desc,'place':place,'rate':rate,'pos':place_of_supply,'gst':gst,'igst':igst})
    return redirect('/')
    

def deleteestimate(request,est_id):
    user = request.user
    company = company_details.objects.get(user=user)
    estimate = Estimates.objects.get(id=est_id)
    items = EstimateItems.objects.filter(estimate=estimate)
    items.delete()
    estimate.delete()
    return redirect('allestimates')
    

@login_required(login_url='login')
def additem_page_est(request):
    unit=Unit.objects.all()
    sale=Sales.objects.all()
    purchase=Purchase.objects.all()
    accounts = Purchase.objects.all()
    account_types = set(Purchase.objects.values_list('Account_type', flat=True))

    
    account = Sales.objects.all()
    account_type = set(Sales.objects.values_list('Account_type', flat=True))
    
    

    return render(request,'additem_est.html',{'unit':unit,'sale':sale,'purchase':purchase,
               
                            "account":account,"account_type":account_type,"accounts":accounts,"account_types":account_types,
                            
                            })

def additem_est(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            radio=request.POST.get('radio')
            if radio=='tax':
    
                
                inter=request.POST['inter']
                intra=request.POST['intra']
                type=request.POST.get('type')
                name=request.POST['name']
                unit=request.POST['unit']
                sel_price=request.POST.get('sel_price')
                sel_acc=request.POST.get('sel_acc')
                s_desc=request.POST.get('sel_desc')
                cost_price=request.POST.get('cost_price')
                cost_acc=request.POST.get('cost_acc')      
                p_desc=request.POST.get('cost_desc')
                u=request.user.id
                us=request.user
                history="Created by" + str(us)
                user=User.objects.get(id=u)
                unit=Unit.objects.get(id=unit)
                sel=Sales.objects.get(id=sel_acc)
                cost=Purchase.objects.get(id=cost_acc)
                ad_item=AddItem(type=type,Name=name,p_desc=p_desc,s_desc=s_desc,s_price=sel_price,p_price=cost_price,unit=unit,
                            sales=sel,purchase=cost,user=user,creat=history,interstate=inter,intrastate=intra
                                )
                
            else:
                                                  
                type=request.POST.get('type')
                name=request.POST['name']
                unit=request.POST['unit']
                sel_price=request.POST.get('sel_price')
                sel_acc=request.POST.get('sel_acc')
                s_desc=request.POST.get('sel_desc')
                cost_price=request.POST.get('cost_price')
                cost_acc=request.POST.get('cost_acc')      
                p_desc=request.POST.get('cost_desc')
                u=request.user.id
                us=request.user
                history="Created by" + str(us)
                user=User.objects.get(id=u)
                unit=Unit.objects.get(id=unit)
                sel=Sales.objects.get(id=sel_acc)
                cost=Purchase.objects.get(id=cost_acc)
                ad_item=AddItem(type=type,Name=name,p_desc=p_desc,s_desc=s_desc,s_price=sel_price,p_price=cost_price,unit=unit,
                            sales=sel,purchase=cost,user=user,creat=history,interstate='none',intrastate='none'
                                )
                ad_item.save()
            ad_item.save()
           
            return redirect("newestimate")
    return render(request,'additem_est.html')

@login_required(login_url='login')
def add_unit_est(request):
    if request.method=='POST':
        unit_name=request.POST['unit_name']
        Unit(unit=unit_name).save()
        return redirect('additem_est')
    return redirect("additem_est")
    
#-------------new view functions to add

@login_required(login_url='login')
def add_sales_est(request):
    if request.method=='POST':
        Account_type  =request.POST['acc_type']
        Account_name =request.POST['acc_name']
        Acount_code =request.POST['acc_code']
        Account_desc =request.POST['acc_desc']        
        acc=Sales(Account_type=Account_type,Account_name=Account_name,Acount_code=Acount_code,Account_desc=Account_desc)
        acc.save()
        return redirect('additem_est')
    return redirect("additem_est")

@login_required(login_url='login')
def add_account_est(request):
    if request.method=='POST':
        Account_type  =request.POST['acc_type']
        Account_name =request.POST['acc_name']
        Acount_code =request.POST['acc_code']
        Account_desc =request.POST['acc_desc']
       
        acc=Purchase(Account_type=Account_type,Account_name=Account_name,Acount_code=Acount_code,Account_desc=Account_desc)
        acc.save()                 
        return redirect("additem_est")
        
    return redirect("additem_est")
    
def customerdata(request):
    customer_id = request.GET.get('id')
    print(customer_id)
    cust = customer.objects.get(customerName=customer_id)
    data7 = {'email': cust.customerEmail}
    
    print(data7)
    return JsonResponse(data7)


def add_customer_for_invoice(request):
    pt=payment_terms.objects.all()
    if request.user.is_authenticated:
        if request.method=='POST':
            type=request.POST.get('type')
            txtFullName=request.POST['txtFullName']
            cpname=request.POST['cpname']
           
            email=request.POST.get('myEmail')
            wphone=request.POST.get('wphone')
            mobile=request.POST.get('mobile')
            skname=request.POST.get('skname')
            desg=request.POST.get('desg')      
            dept=request.POST.get('dept')
            wbsite=request.POST.get('wbsite')

            gstt=request.POST.get('gstt')
            posply=request.POST.get('posply')
            tax1=request.POST.get('tax1')
            crncy=request.POST.get('crncy')
            obal=request.POST.get('obal')

            select=request.POST.get('pterms')
            pterms=payment_terms.objects.get(id=select)
            pterms=request.POST.get('pterms')

            plst=request.POST.get('plst')
            plang=request.POST.get('plang')
            fbk=request.POST.get('fbk')
            twtr=request.POST.get('twtr')
        
            atn=request.POST.get('atn')
            ctry=request.POST.get('ctry')
            
            addrs=request.POST.get('addrs')
            addrs1=request.POST.get('addrs1')
            bct=request.POST.get('bct')
            bst=request.POST.get('bst')
            bzip=request.POST.get('bzip')
            bpon=request.POST.get('bpon')
            bfx=request.POST.get('bfx')

            sal=request.POST.get('sal')
            ftname=request.POST.get('ftname')
            ltname=request.POST.get('ltname')
            mail=request.POST.get('mail')
            bworkpn=request.POST.get('bworkpn')
            bmobile=request.POST.get('bmobile')

            bskype=request.POST.get('bskype')
            bdesg=request.POST.get('bdesg')
            bdept=request.POST.get('bdept')
            u = User.objects.get(id = request.user.id)

          
            ctmr=customer(customerName=txtFullName,customerType=type,
                        companyName=cpname,customerEmail=email,customerWorkPhone=wphone,
                         customerMobile=mobile,skype=skname,designation=desg,department=dept,
                           website=wbsite,GSTTreatment=gstt,placeofsupply=posply, Taxpreference=tax1,
                             currency=crncy,OpeningBalance=obal,PaymentTerms=pterms,
                                PriceList=plst,PortalLanguage=plang,Facebook=fbk,Twitter=twtr,
                                 Attention=atn,country=ctry,Address1=addrs,Address2=addrs1,
                                  city=bct,state=bst,zipcode=bzip,phone1=bpon,
                                   fax=bfx,CPsalutation=sal,Firstname=ftname,
                                    Lastname=ltname,CPemail=mail,CPphone=bworkpn,
                                    CPmobile= bmobile,CPskype=bskype,CPdesignation=bdesg,
                                     CPdepartment=bdept,user=u )
            ctmr.save()  
            
            return redirect("add_prod")
        return render(request,"createinvoice.html",)
        
        
def payment_term_for_invoice(request):
    if request.method=='POST':
        term=request.POST.get('term')
        day=request.POST.get('day')
        ptr=payment_terms(Terms=term,Days=day)
        ptr.save()
        return redirect("add_prod")
        
        
def addprice(request):
    add=AddItem.objects.all()
    return render(request,'addprice_list.html',{'add':add})
def addpl(request):
    print('hi')
    if request.method == "POST":
        

        
        name = request.POST.get('name')
        print(name)
        types = request.POST.get('type')
        print(types)
        taxes=request.POST.get('rate')
        desc = request.POST.get('desc')
        cur = request.POST.get('currency')
        print(cur)
        mark = request.POST.get('mark')
        print(mark)
        perc = request.POST.get('per')
        print(perc)
        rounds = request.POST.get('round')
        print(rounds)
        u = request.user.id
        user = User.objects.get(id=u)
            
        ad_item = Pricelist(
                name=name,
                types=types,
                tax=taxes,
                currency=cur,
                description=desc,
                mark=mark,
                percentage=perc,
                roundoff=rounds,
                user=user,
            )
            
        ad_item.save()
        item_name = request.POST.getlist('iname[]') 
        print(item_name)
        price = request.POST.getlist('iprice[]')
        rate = request.POST.getlist('custom[]') 
        if len(item_name) == len(price) == len(rate):
            mapped2 = zip(item_name, price, rate)
            mapped2 = list(mapped2)
         
            for ele in mapped2:
                created = Sample_table.objects.get_or_create(item_name=ele[0], price=ele[1], cust_rate=ele[2], pl=ad_item)

        return redirect("viewpricelist")
    else:
        # Handle the case when the request method is not POST
        return render(request, 'addprice_list.html')
    # return render(request, 'addprice_list.html')
def createpl(request):
    return render(request,'addprice_list.html')
def active_status(request, id):
    user = request.user.id
    user = User.objects.get(id=user)
    viewitem = Pricelist.objects.all()
    event = Pricelist.objects.get(id=id)
    
    if request.method == 'POST':
        action = request.POST['action']
        event.status = action  # Updated field name to 'status'
        event.save()
    
    return render(request, 'view_price_list.html', {'view': viewitem})

def viewpricelist(request):
    view=Pricelist.objects.all()                                                                                                                                                                                                                                                                                                                        
    return render(request,'view_price_list.html',{'view':view})
def viewlist(request,id):
    user_id=request.user
    items=Pricelist.objects.all()
    product=Pricelist.objects.get(id=id)
    print(product.id)
    
    
    context={
       "allproduct":items,
       "product":product,
      
    }
    
    return render(request,'list.html',context)

def editlist(request,id):
    editpl=Pricelist.objects.get(id=id)
    sam=Sample_table.objects.filter(pl=id)
    return render(request,'edit_pricelist.html',{'editpl':editpl,'sam':sam})
def editpage(request,id):
    if request.method=='POST':
        edit=Pricelist.objects.get(id=id)
        edit.name=request.POST['name']
        edit.description=request.POST['desc']
        edit.mark=request.POST['mark']
        edit.percentage=request.POST['per']
        print(request.POST['per'])
        edit.tax=request.POST['types']
        
        edit.roundoff=request.POST['round']
        print(edit.roundoff)
        item_name = request.POST.getlist('iname[]') 
        print(item_name)
        price = request.POST.getlist('iprice[]')
        rate = request.POST.getlist('custom[]') 
        sam=Sample_table.objects.filter(pl=id).delete()

        if len(item_name) == len(price) == len(rate):
            mapped2 = zip(item_name, price, rate)
            mapped2 = list(mapped2)
         
            for ele in mapped2:
                created = Sample_table.objects.get_or_create(item_name=ele[0], price=ele[1], cust_rate=ele[2],pl=edit)
        edit.save()

        return redirect('viewpricelist')
def delete_item(request,id):
    dl=Pricelist.objects.get(id=id)
    dl.delete()
    return redirect('viewpricelist')


def banking_home(request):
  
    viewitem=banking.objects.filter(user=request.user)
    return render(request,'banking.html',{'view':viewitem})       
    
def create_banking(request):
    company = company_details.objects.get(user = request.user)
    print(company.company_name)
    banks = bank.objects.filter(user=request.user, acc_type="bank")
    return render(request,'create_banking.html',{"bank":banks,"company":company})    

def save_banking(request):
    if request.method == "POST":
        a=banking()
        a.name = request.POST.get('main_name',None)
        a.alias = request.POST.get('main_alias',None)
        a.acc_type = request.POST.get('main_type',None)
        a.ac_holder = request.POST.get('ac_holder',None)
        a.ac_no = request.POST.get('ac_number',None)
        a.ifsc = request.POST.get('ifsc',None)
        a.swift_code = request.POST.get('sw_code',None)
        a.bnk_name = request.POST.get('bnk_nm',None)
        a.bnk_branch = request.POST.get('br_name',None)
        a.chq_book = request.POST.get('alter_chq',None)
        a.chq_print = request.POST.get('en_chq',None)
        a.chq_config = request.POST.get('chq_prnt',None)
        a.mail_name = request.POST.get('name',None)
        a.mail_addr = request.POST.get('address',None)
        a.mail_country = request.POST.get('country',None)
        a.mail_state = request.POST.get('state',None)
        a.mail_pin = request.POST.get('pin',None)
        a.bd_bnk_det = request.POST.get('bnk_det',None)
        a.bd_pan_no = request.POST.get('pan',None)
        a.bd_reg_typ = request.POST.get('register_type',None)
        a.bd_gst_no = request.POST.get('gstin',None)
        a.bd_gst_det = request.POST.get('gst_det',None)
        a.user=request.user
        a.opening_bal = request.POST.get('balance',None)
        a.save()
        return redirect("banking_home")
    return redirect("create_banking")

def view_bank(request,id):
    viewitem=banking.objects.filter(user=request.user)
    bnk=banking.objects.get(id=id,user=request.user)
    context={
        'view':viewitem,
        'bnk':bnk,
    }
    return render(request,"view_bank.html",context)

def banking_edit(request,id):
    bnk=banking.objects.get(id=id,user=request.user)
    banks = bank.objects.filter(user=request.user, acc_type="bank")
    context={
        'bnk':bnk,
        "bank":banks
    }
    return render(request,"edit_banking.html",context)

def save_edit_bnk(request,id):
    if request.method == "POST":
        a=banking.objects.get(id=id,user=request.user)
        a.name = request.POST.get('main_name',None)
        a.alias = request.POST.get('main_alias',None)
        a.acc_type = request.POST.get('main_type',None)
        a.ac_holder = request.POST.get('ac_holder',None)
        a.ac_no = request.POST.get('ac_number',None)
        a.ifsc = request.POST.get('ifsc',None)
        a.swift_code = request.POST.get('sw_code',None)
        a.bnk_name = request.POST.get('bnk_nm',None)
        a.bnk_branch = request.POST.get('br_name',None)
        a.chq_book = request.POST.get('alter_chq',None)
        a.chq_print = request.POST.get('en_chq',None)
        a.chq_config = request.POST.get('chq_prnt',None)
        a.mail_name = request.POST.get('name',None)
        a.mail_addr = request.POST.get('address',None)
        a.mail_country = request.POST.get('country',None)
        a.mail_state = request.POST.get('state',None)
        a.mail_pin = request.POST.get('pin',None)
        a.bd_bnk_det = request.POST.get('bnk_det',None)
        a.bd_pan_no = request.POST.get('pan',None)
        a.bd_reg_typ = request.POST.get('register_type',None)
        a.bd_gst_no = request.POST.get('gstin',None)
        a.bd_gst_det = request.POST.get('gst_det',None)
        a.opening_bal = request.POST.get('balance',None)
        a.save()
        return redirect("banking_home")
    return redirect("create_banking")

def save_bank(request):
    if request.method == "POST":
        a=bank()
        a.acc_type = request.POST.get('type',None)
        a.bank_name = request.POST.get('bank',None)
        a.user = request.user
        a.save()
        return redirect("create_banking")
    return redirect("create_banking")
def save_banking_edit(request,id):
    if request.method == "POST":
        a=bank()
        a.acc_type = request.POST.get('type',None)
        a.bank_name = request.POST.get('bank',None)
        a.user = request.user
        a.save()
        return redirect("banking_edit", id)
    return redirect("banking_edit", id)
    
def basenav(request):
    company = company_details.objects.get(user = request.user)
    print(company.company_name)
    context = {
                'company' : company
            }
    return render(request,'base.html',context)

@login_required(login_url='login')
def recurringhome(request):
    selected_vendor_id = request.GET.get('vendor')
    vendors = vendor_table.objects.filter(user=request.user)
    selected_vendor = vendor_table.objects.filter(id=selected_vendor_id).first()
    gst_number = selected_vendor.gst_number if selected_vendor else ''
    return render(request, 'recurring_home.html', {
        'vendors': vendors,
        'selected_vendor_id': selected_vendor_id,
        'gst_number': gst_number,
    })




from django.shortcuts import get_object_or_404
from .models import Expense, vendor_table

def add_expense(request):
    if request.method == 'POST':
        profile_name = request.POST['profile_name']
        repeat_every = request.POST['repeat_every']
        start_date = request.POST['start_date']
        ends_on = request.POST['ends_on']
        expense_account = request.POST.get('expense_account', '')  # Use get() with a default value
        expense_type = request.POST['expense_type']
        goods_label = request.POST.get('goods_label')
        amount = request.POST['amount']
        currency = request.POST['currency']
        paidthrough = request.POST['paidthrough']
        vendor_id = request.POST['vendor']
        vendor = get_object_or_404(vendor_table, pk=vendor_id)
        gst = request.POST['gst']
        destination = request.POST['destination']
        tax = request.POST['tax']
        notes = request.POST['notes']
        customer_id = request.POST['customername']
        customer_obj = get_object_or_404(customer, pk=customer_id)
        expense = Expense(
            profile_name=profile_name, repeat_every=repeat_every, start_date=start_date,
            ends_on=ends_on, expense_account=expense_account, expense_type=expense_type,
            goods_label=goods_label, amount=amount, currency=currency, paidthrough=paidthrough,
            vendor=vendor, gst=gst, customername=customer_obj.customerName,
            notes=notes, tax=tax, destination=destination
        )
        expense.save()
        return redirect('recurringbase')
    else:
        vendors = vendor_table.objects.all()
        return render(request, 'add_expense.html', {'vendors': vendors})


@login_required(login_url='login')
def recurringbase(request):
    expenses = Expense.objects.all()
    return render(request, 'recurring_base.html',{'expenses': expenses})

def show_recurring(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    expenses = Expense.objects.all()
    return render(request, 'show_recurring.html', {'expense': expense,'expenses': expenses})


def expense_details(request):
    expenses = Expense.objects.all()
    return render(request, 'recurring_base.html',{'expenses': expenses})

@login_required(login_url='login')
def vendor(request):
    return render(request,'create_vendor.html')



@login_required(login_url='login')
def add_vendor(request):
    if request.method=="POST":
        vendor_data=vendor_table()
        vendor_data.salutation=request.POST['salutation']
        vendor_data.first_name=request.POST['first_name']
        vendor_data.last_name=request.POST['last_name']
        vendor_data.company_name=request.POST['company_name']
        vendor_data.vendor_display_name=request.POST['v_display_name']
        vendor_data.vendor_email=request.POST['vendor_email']
        vendor_data.vendor_wphone=request.POST['w_phone']
        vendor_data.vendor_mphone=request.POST['m_phone']
        vendor_data.skype_number=request.POST['skype_number']
        vendor_data.designation=request.POST['designation']
        vendor_data.department=request.POST['department']
        vendor_data.website=request.POST['website']
        vendor_data.gst_treatment=request.POST['gst']

        x=request.POST['gst']
        if x=="Unregistered Business-not Registered under GST":
            vendor_data.pan_number=request.POST['pan_number']
            vendor_data.gst_number="null"
        else:
            vendor_data.gst_number=request.POST['gst_number']
            vendor_data.pan_number=request.POST['pan_number']

        vendor_data.source_supply=request.POST['source_supply']
        vendor_data.currency=request.POST['currency']
        vendor_data.opening_bal=request.POST['opening_bal']
        vendor_data.payment_terms=request.POST['payment_terms']

        user_id=request.user.id
        udata=User.objects.get(id=user_id)
        vendor_data.user=udata
        vendor_data.battention=request.POST['battention']
        vendor_data.bcountry=request.POST['bcountry']
        vendor_data.baddress=request.POST['baddress']
        vendor_data.bcity=request.POST['bcity']
        vendor_data.bstate=request.POST['bstate']
        vendor_data.bzip=request.POST['bzip']
        vendor_data.bphone=request.POST['bphone']
        vendor_data.bfax=request.POST['bfax']

        vendor_data.sattention=request.POST['sattention']
        vendor_data.scountry=request.POST['scountry']
        vendor_data.saddress=request.POST['saddress']
        vendor_data.scity=request.POST['scity']
        vendor_data.sstate=request.POST['sstate']
        vendor_data.szip=request.POST['szip']
        vendor_data.sphone=request.POST['sphone']
        vendor_data.sfax=request.POST['sfax']
        vendor_data.save()
# .......................................................adding to remaks table.....................
        vdata=vendor_table.objects.get(id=vendor_data.id)
        vendor=vdata
        rdata=remarks_table()
        rdata.remarks=request.POST['remark']
        rdata.user=udata
        rdata.vendor=vdata
        rdata.save()


#  ...........................adding multiple rows of table to model  ........................................................       
        salutation =request.POST.getlist('salutation[]')
        first_name =request.POST.getlist('first_name[]')
        last_name =request.POST.getlist('last_name[]')
        email =request.POST.getlist('email[]')
        work_phone =request.POST.getlist('wphone[]')
        mobile =request.POST.getlist('mobile[]')
        skype_number =request.POST.getlist('skype[]')
        designation =request.POST.getlist('designation[]')
        department =request.POST.getlist('department[]') 
        vdata=vendor_table.objects.get(id=vendor_data.id)
        vendor=vdata
       

        if len(salutation)==len(first_name)==len(last_name)==len(email)==len(work_phone)==len(mobile)==len(skype_number)==len(designation)==len(department):
            mapped2=zip(salutation,first_name,last_name,email,work_phone,mobile,skype_number,designation,department)
            mapped2=list(mapped2)
            print(mapped2)
            for ele in mapped2:
                created = contact_person_table.objects.get_or_create(salutation=ele[0],first_name=ele[1],last_name=ele[2],email=ele[3],
                         work_phone=ele[4],mobile=ele[5],skype_number=ele[6],designation=ele[7],department=ele[8],user=udata,vendor=vendor)
        
       
                 
        return redirect('recurringhome')
        
def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    vendors = vendor_table.objects.all()
    customers = customer.objects.all()  # Fetch all customers

    if request.method == 'POST':
        expense.profile_name = request.POST.get('profile_name')
        expense.repeat_every = request.POST.get('repeat_every')
        expense.start_date = request.POST.get('start_date')
        expense.ends_on = request.POST.get('ends_on')
        expense.expense_account = request.POST.get('expense_account')
        expense.expense_type = request.POST.get('expense_type')
        expense.amount = request.POST.get('amount')
        expense.currency = request.POST.get('currency')
        expense.paidthrough = request.POST.get('paidthrough')
        expense.vendor_id = request.POST.get('vendor')
        expense.goods_label = request.POST.get('goods_label')
        expense.gst = request.POST.get('gst')
        expense.destination = request.POST.get('destination')
        expense.tax = request.POST.get('tax')
        expense.notes = request.POST.get('notes')
        customer_id = request.POST.get('customername')  # Get the customer ID from POST data
        customer_obj = get_object_or_404(customer, pk=customer_id)  # Fetch the customer object
        expense.customername = customer_obj.customerName  # Set the customer name in the expense object

        expense.save()
        return redirect('recurringbase')

    else:
        return render(request, 'edit_expense.html', {'expense': expense, 'vendors': vendors, 'customers': customers})



@login_required(login_url='login')
def newexp(request):
    return render(request,'create_expense.html')


def save_data(request):
    if request.method == 'POST':
        account_type = request.POST.get('accountType')
        account_name = request.POST.get('accountName')
        account_code = request.POST.get('accountCode')
        description = request.POST.get('description')

        account = Account(accountType=account_type, accountName=account_name, accountCode=account_code, description=description)
        account.save()

        return redirect('recurringhome')

    return render(request, 'recurring_home.html')


from django.http import JsonResponse
from .models import Account

def get_account_names(request):
    account_names = Account.objects.values_list('accountName', flat=True)
    return JsonResponse(list(account_names), safe=False)


@login_required(login_url='login')
def profileshow(request,expense_id):
    expenses = Expense.objects.all()
    expense = get_object_or_404(Expense, id=expense_id)

    return render(request, 'show_recurring.html', {'expenses': expenses,'expense':expense})


def add_customer(request):
    sb=payment_terms.objects.all()
    return render(request,'customer.html',{'sb':sb})
def entr_custmr(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            type=request.POST.get('type')
            txtFullName=request.POST['txtFullName']
            cpname=request.POST['cpname']
           
            email=request.POST.get('myEmail')
            wphone=request.POST.get('wphone')
            mobile=request.POST.get('mobile')
            skname=request.POST.get('skname')
            desg=request.POST.get('desg')      
            dept=request.POST.get('dept')
            wbsite=request.POST.get('wbsite')

            gstt=request.POST.get('gstt')
            posply=request.POST.get('posply')
            tax1=request.POST.get('tax1')
            crncy=request.POST.get('crncy')
            obal=request.POST.get('obal')

            select = request.POST.get('pterms')
        try:
            pterms = payment_terms.objects.get(id=select)
        except payment_terms.DoesNotExist:
            pterms = None

            plst=request.POST.get('plst')
            plang=request.POST.get('plang')
            fbk=request.POST.get('fbk')
            twtr=request.POST.get('twtr')
        
            atn=request.POST.get('atn')
            ctry=request.POST.get('ctry')
            
            addrs=request.POST.get('addrs')
            addrs1=request.POST.get('addrs1')
            bct=request.POST.get('bct')
            bst=request.POST.get('bst')
            bzip=request.POST.get('bzip')
            bpon=request.POST.get('bpon')
            bfx=request.POST.get('bfx')

            sal=request.POST.get('sal')
            ftname=request.POST.get('ftname')
            ltname=request.POST.get('ltname')
            mail=request.POST.get('mail')
            bworkpn=request.POST.get('bworkpn')
            bmobile=request.POST.get('bmobile')

            bskype=request.POST.get('bskype')
            bdesg=request.POST.get('bdesg')
            bdept=request.POST.get('bdept')
            u = User.objects.get(id = request.user.id)

          
            ctmr=customer(customerName=txtFullName,customerType=type,
                        companyName=cpname,customerEmail=email,customerWorkPhone=wphone,
                         customerMobile=mobile,skype=skname,designation=desg,department=dept,
                           website=wbsite,GSTTreatment=gstt,placeofsupply=posply, Taxpreference=tax1,
                             currency=crncy,OpeningBalance=obal,PaymentTerms=pterms,
                                PriceList=plst,PortalLanguage=plang,Facebook=fbk,Twitter=twtr,
                                 Attention=atn,country=ctry,Address1=addrs,Address2=addrs1,
                                  city=bct,state=bst,zipcode=bzip,phone1=bpon,
                                   fax=bfx,CPsalutation=sal,Firstname=ftname,
                                    Lastname=ltname,CPemail=mail,CPphone=bworkpn,
                                    CPmobile= bmobile,CPskype=bskype,CPdesignation=bdesg,
                                     CPdepartment=bdept,user=u )
            ctmr.save()  
            
            return redirect("recurringhome")
        return render(request,'recurring_home.html')
def payment_term(request):
    if request.method=='POST':
        term=request.POST.get('term')
        day=request.POST.get('day')
        ptr=payment_terms(Terms=term,Days=day)
        ptr.save()
        return redirect("add_customer")

from django.http import JsonResponse

def get_customer_names(request):
    customers = customer.objects.all()
    customer_names = [{'id': c.id, 'name': c.customerName} for c in customers]
    return JsonResponse(customer_names, safe=False)


def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    expense.delete()
    return redirect('recurringbase')


def get_profile_details(request, profile_id):
    expense = get_object_or_404(Expense, id=profile_id)
    vendor = expense.vendor 
    data = {
        'id': expense.id,
        'profile_name': expense.profile_name,
        'repeat_every': expense.repeat_every,
        'start_date': expense.start_date,
        'ends_on': expense.ends_on,
        'expense_account': expense.expense_account,
        'expense_type': expense.expense_type,
        'amount': expense.amount,
        'paidthrough': expense.paidthrough,
        'vendor': vendor.vendor_display_name,  
        'gst': expense.gst,
        'destination': expense.destination,
        'tax': expense.tax,
        'notes': expense.notes,
        'customername': expense.customername,
    }
    return JsonResponse(data)






@login_required(login_url='login')
def view_sales_order(request):
    sales=SalesOrder.objects.all()
    return render(request,'view_sales_order.html',{"sale":sales})   

    
@login_required(login_url='login')
def create_sales_order(request):
    cust=customer.objects.all()
    pay=payment_terms.objects.all()
    itm=AddItem.objects.all()
    context={
        "c":cust,
        "pay":pay,
        "itm":itm,
    }
    return render(request,'create_sales_order.html',context)

    
@login_required(login_url='login')
def add_customer_for_sorder(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            type=request.POST.get('type')
            txtFullName=request.POST['txtFullName']
            cpname=request.POST['cpname']
           
            email=request.POST.get('myEmail')
            wphone=request.POST.get('wphone')
            mobile=request.POST.get('mobile')
            skname=request.POST.get('skname')
            desg=request.POST.get('desg')      
            dept=request.POST.get('dept')
            wbsite=request.POST.get('wbsite')

            gstt=request.POST.get('gstt')
            posply=request.POST.get('posply')
            tax1=request.POST.get('tax1')
            crncy=request.POST.get('crncy')
            obal=request.POST.get('obal')

          
            pterms=request.POST.get('pterms')

            plst=request.POST.get('plst')
            plang=request.POST.get('plang')
            fbk=request.POST.get('fbk')
            twtr=request.POST.get('twtr')
        
            atn=request.POST.get('atn')
            ctry=request.POST.get('ctry')
            
            addrs=request.POST.get('addrs')
            addrs1=request.POST.get('addrs1')
            bct=request.POST.get('bct')
            bst=request.POST.get('bst')
            bzip=request.POST.get('bzip')
            bpon=request.POST.get('bpon')
            bfx=request.POST.get('bfx')

            sal=request.POST.get('sal')
            ftname=request.POST.get('ftname')
            ltname=request.POST.get('ltname')
            mail=request.POST.get('mail')
            bworkpn=request.POST.get('bworkpn')
            bmobile=request.POST.get('bmobile')

            bskype=request.POST.get('bskype')
            bdesg=request.POST.get('bdesg')
            bdept=request.POST.get('bdept')
            u = User.objects.get(id = request.user.id)

          
            ctmr=customer(customerName=txtFullName,customerType=type,
                        companyName=cpname,customerEmail=email,customerWorkPhone=wphone,
                         customerMobile=mobile,skype=skname,designation=desg,department=dept,
                           website=wbsite,GSTTreatment=gstt,placeofsupply=posply, Taxpreference=tax1,
                             currency=crncy,OpeningBalance=obal,PaymentTerms=pterms,
                                PriceList=plst,PortalLanguage=plang,Facebook=fbk,Twitter=twtr,
                                 Attention=atn,country=ctry,Address1=addrs,Address2=addrs1,
                                  city=bct,state=bst,zipcode=bzip,phone1=bpon,
                                   fax=bfx,CPsalutation=sal,Firstname=ftname,
                                    Lastname=ltname,CPemail=mail,CPphone=bworkpn,
                                    CPmobile= bmobile,CPskype=bskype,CPdesignation=bdesg,
                                     CPdepartment=bdept,user=u )
            ctmr.save()  
            
            return redirect("create_sales_order")

    
@login_required(login_url='login')        
def payment_term_for_sorder(request):
    if request.method=='POST':
        term=request.POST.get('term')
        day=request.POST.get('day')
        ptr=payment_terms(Terms=term,Days=day)
        ptr.save()
        return redirect("create_sales_order")
        


    
@login_required(login_url='login')
def add_sales_order(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            c=request.POST['cx_name']
            cus=customer.objects.get(customerName=c)   
            custo=cus.id
            sales_no=request.POST['sale_no']
            terms=request.POST['term']
            term=payment_terms.objects.get(id=terms)
            reference=request.POST['ord_no']
            sa_date=request.POST['sa_date']
            sh_date=request.POST['sh_date']
            d_method=request.POST['d_meth']
            s_pers=request.POST['s_pers']
        
            
            cxnote=request.POST['customer_note']
            subtotal=request.POST['subtotal']
            igst=request.POST['igst']
            cgst=request.POST['cgst']
            sgst=request.POST['sgst']
            totaltax=request.POST['totaltax']
            t_total=request.POST['t_total']
            if request.FILES.get('file') is not None:
                file=request.FILES['file']
            else:
                file="/static/images/alt.jpg"
            tc=request.POST['ter_cond']

            status=request.POST['sd']
            if status=='draft':
                print(status)   
            else:
                print(status)  
        
            product=request.POST.getlist('item[]')
            hsn=request.POST.getlist('hsn[]')
            quantity=request.POST.getlist('quantity[]')
            rate=request.POST.getlist('rate[]')
            desc=request.POST.getlist('desc[]')
            tax=request.POST.getlist('tax[]')
            total=request.POST.getlist('amount[]')
            term=payment_terms.objects.get(id=term.id)

            sales=SalesOrder(customer_id=custo,sales_no=sales_no,terms=term,reference=reference, sales_date=sa_date,ship_date=sh_date,
                        cxnote=cxnote,subtotal=subtotal,igst=igst,cgst=cgst,sgst=sgst,t_tax=totaltax,
                        grandtotal=t_total,status=status,terms_condition=tc,file=file,d_method=d_method,s_person=s_pers)
            sales.save()
            sale_id=SalesOrder.objects.get(id=sales.id)
            if len(product)==len(quantity)==len(tax)==len(total)==len(rate):

                mapped = zip(product,quantity,tax,total,rate)
                mapped = list(mapped)
                for element in mapped:
                    created =sales_item.objects.get_or_create(sale=sale_id,product=element[0],
                                        quantity=element[1],tax=element[2],total=element[3],rate=element[4])
                

                    
               
   
    return render(request,'create_sales_order.html')            
    
@login_required(login_url='login')
def sales_order_det(request,id):
    sales=SalesOrder.objects.get(id=id)
    saleitem=sales_item.objects.filter(sale_id=id)
    sale_order=SalesOrder.objects.all()
    company=company_details.objects.get(user_id=request.user.id)
    
    
    context={
        'sale':sales,
        'saleitem':saleitem,
        'sale_order':sale_order,
        'comp':company,
        
        
                    }
    return render(request,'sales_order_det.html',context)

    
@login_required(login_url='login')
def delet_sales(request,id):
    d=SalesOrder.objects.get(id=id)
    d.delete()
    return redirect('view_sales_order')
    
    
@login_required(login_url='login')
def edit_sales_order(request,id):
    c = customer.objects.all()
    itm = AddItem.objects.all()
    salesitem = sales_item.objects.filter(sale_id=id)
    sales = SalesOrder.objects.get(id=id)
    pay=payment_terms.objects.all()


    if request.method == 'POST':
        u=request.user.id
        c=request.POST['cx_name']
        
        cust=customer.objects.get(customerName=c) 
        sales.customer=cust
        term=request.POST['term']
        
        
        sales.terms = payment_terms.objects.get(id=term)
        sales.sales_date = request.POST['sa_date']
        sales.shipdate=request.POST['sh_date']
        sales.cxnote = request.POST['customer_note']
        sales.igst = request.POST['igst']
        sales.cgst = request.POST['cgst']
        sales.sgst = request.POST['sgst']
        sales.t_tax = request.POST['totaltax']
        sales.grandtotal = request.POST['t_total']

        if request.FILES.get('file') is not None:
            sales.file = request.FILES['file']
        else:
            sales.file = "/static/images/alt.jpg"

            sales.terms_condition = request.POST.get('ter_cond')
        
        status=request.POST['sd']
        if status=='draft':
            sales.status=status      
        else:
            sales.status=status   
         
        sales.save()
        
        product=request.POST.getlist('item[]')
        quantity=request.POST.getlist('quantity[]')
        rate=request.POST.getlist('rate[]')
        tax=request.POST.getlist('tax[]')
        total=request.POST.getlist('amount[]')
        obj_dele=sales_item.objects.filter(sale_id=sales.id)
        obj_dele.delete()
       
        if len(product)==len(quantity)==len(tax)==len(total)==len(rate):

            mapped = zip(product,quantity,tax,total,rate)
            mapped = list(mapped)
            for element in mapped:
                created = sales_item.objects.get_or_create(sale=sales,product=element[0],
                                    quantity=element[1],tax=element[2],total=element[3],rate=element[4])
                
            return redirect('sales_order_det',id)
    context={
        "c":c,
        "itm":itm,
        "saleitm":salesitem,
        "sale":sales,
        "pay":pay

    }
    return render(request,'edit_sale_page.html',context)

def create_account_journal(request):
    if request.method=='POST':
        a=Chart_of_Account()
        cur_user = request.user
        user = User.objects.get(id=cur_user.id)
        a.user = user
        a.account_type = request.POST.get("account_type",None)
        a.account_name = request.POST.get("account_name",None)
        a.account_code = request.POST.get("account_code",None)
        a.description = request.POST.get("description",None)
        a.watchlist = request.POST.get("watchlist",None)
        a.status="inactive"
        if a.account_type=="Other Current Assets":
            a.credit_no = request.POST.get("credit_number",None)
            a.sub_account = request.POST.get("sub_account",None)
            a.parent_account = request.POST.get("parent_account",None)
            a.bank_account_no = request.POST.get("account_number",None)
            a.currency = request.POST.get("currency",None)

        if a.account_type=="Cash":
            a.credit_no = request.POST.get("credit_number",None)
            a.sub_account = request.POST.get("sub_account22",None)
            a.parent_account = request.POST.get("parent_account22",None)
            a.bank_account_no = request.POST.get("account_number",None)
            a.currency = request.POST.get("currency",None)

        if a.account_type=="Fixed Assets":
            a.credit_no = request.POST.get("credit_number",None)
            a.sub_account = request.POST.get("sub_account33",None)
            a.parent_account = request.POST.get("parent_account33",None)
            a.bank_account_no = request.POST.get("account_number",None)
            a.currency = request.POST.get("currency",None)
        
        if a.account_type=="Stock":
            a.credit_no = request.POST.get("credit_number",None)
            a.sub_account = request.POST.get("sub_account44",None)
            a.parent_account = request.POST.get("parent_account44",None)
            a.bank_account_no = request.POST.get("account_number",None)
            a.currency = request.POST.get("currency",None)
        
        if a.account_type=="Other Current Liability":
            a.credit_no = request.POST.get("credit_number",None)
            a.sub_account = request.POST.get("sub_account55",None)
            a.parent_account = request.POST.get("parent_account55",None)
            a.bank_account_no = request.POST.get("account_number",None)
            a.currency = request.POST.get("currency",None)
        
        if a.account_type=="Long Term Liability":
            a.credit_no = request.POST.get("credit_number",None)
            a.sub_account = request.POST.get("sub_account66",None)
            a.parent_account = request.POST.get("parent_account66",None)
            a.bank_account_no = request.POST.get("account_number",None)
            a.currency = request.POST.get("currency",None)
        
        if a.account_type=="Other Liability":
            a.credit_no = request.POST.get("credit_number",None)
            a.sub_account = request.POST.get("sub_account77",None)
            a.parent_account = request.POST.get("parent_account77",None)
            a.bank_account_no = request.POST.get("account_number",None)
            a.currency = request.POST.get("currency",None)
        
        if a.account_type=="Equity":
            a.credit_no = request.POST.get("credit_number",None)
            a.sub_account = request.POST.get("sub_account88",None)
            a.parent_account = request.POST.get("parent_account88",None)
            a.bank_account_no = request.POST.get("account_number",None)
            a.currency = request.POST.get("currency",None)
        
        if a.account_type=="Income":
            a.credit_no = request.POST.get("credit_number",None)
            a.sub_account = request.POST.get("sub_account99",None)
            a.parent_account = request.POST.get("parent_account99",None)
            a.bank_account_no = request.POST.get("account_number",None)
            a.currency = request.POST.get("currency",None)
        
        if a.account_type=="Expense":
            a.credit_no = request.POST.get("credit_number",None)
            a.sub_account = request.POST.get("sub_account100",None)
            a.parent_account = request.POST.get("parent_account100",None)
            a.bank_account_no = request.POST.get("account_number",None)
            a.currency = request.POST.get("currency",None)
        
        if a.account_type=="Cost Of Goods Sold":
            a.credit_no = request.POST.get("credit_number",None)
            a.sub_account = request.POST.get("sub_account111",None)
            a.parent_account = request.POST.get("parent_account111",None)
            a.bank_account_no = request.POST.get("account_number",None)
            a.currency = request.POST.get("currency",None)
        
        if a.account_type=="Other Expense":
            a.credit_no = request.POST.get("credit_number",None)
            a.sub_account = request.POST.get("sub_account222",None)
            a.parent_account = request.POST.get("parent_account222",None)
            a.bank_account_no = request.POST.get("account_number",None)
            a.currency = request.POST.get("currency",None)

        a.save()
        return JsonResponse({'success': True, 'account_name': a.account_name})

    return JsonResponse({'error': 'Invalid request method'}, status=405)

def account_edit_journal(request):
    if request.method=='POST':
        a=Chart_of_Account()
        cur_user = request.user
        user = User.objects.get(id=cur_user.id)
        a.user = user
        a.account_type = request.POST.get("account_type",None)
        a.account_name = request.POST.get("account_name",None)
        a.account_code = request.POST.get("account_code",None)
        a.description = request.POST.get("description",None)
        a.watchlist = request.POST.get("watchlist",None)
        a.status="inactive"
        if a.account_type=="Other Current Assets":
            a.credit_no = request.POST.get("credit_number",None)
            a.sub_account = request.POST.get("sub_account",None)
            a.parent_account = request.POST.get("parent_account",None)
            a.bank_account_no = request.POST.get("account_number",None)
            a.currency = request.POST.get("currency",None)

        if a.account_type=="Cash":
            a.credit_no = request.POST.get("credit_number",None)
            a.sub_account = request.POST.get("sub_account22",None)
            a.parent_account = request.POST.get("parent_account22",None)
            a.bank_account_no = request.POST.get("account_number",None)
            a.currency = request.POST.get("currency",None)

        if a.account_type=="Fixed Assets":
            a.credit_no = request.POST.get("credit_number",None)
            a.sub_account = request.POST.get("sub_account33",None)
            a.parent_account = request.POST.get("parent_account33",None)
            a.bank_account_no = request.POST.get("account_number",None)
            a.currency = request.POST.get("currency",None)
        
        if a.account_type=="Stock":
            a.credit_no = request.POST.get("credit_number",None)
            a.sub_account = request.POST.get("sub_account44",None)
            a.parent_account = request.POST.get("parent_account44",None)
            a.bank_account_no = request.POST.get("account_number",None)
            a.currency = request.POST.get("currency",None)
        
        if a.account_type=="Other Current Liability":
            a.credit_no = request.POST.get("credit_number",None)
            a.sub_account = request.POST.get("sub_account55",None)
            a.parent_account = request.POST.get("parent_account55",None)
            a.bank_account_no = request.POST.get("account_number",None)
            a.currency = request.POST.get("currency",None)
        
        if a.account_type=="Long Term Liability":
            a.credit_no = request.POST.get("credit_number",None)
            a.sub_account = request.POST.get("sub_account66",None)
            a.parent_account = request.POST.get("parent_account66",None)
            a.bank_account_no = request.POST.get("account_number",None)
            a.currency = request.POST.get("currency",None)
        
        if a.account_type=="Other Liability":
            a.credit_no = request.POST.get("credit_number",None)
            a.sub_account = request.POST.get("sub_account77",None)
            a.parent_account = request.POST.get("parent_account77",None)
            a.bank_account_no = request.POST.get("account_number",None)
            a.currency = request.POST.get("currency",None)
        
        if a.account_type=="Equity":
            a.credit_no = request.POST.get("credit_number",None)
            a.sub_account = request.POST.get("sub_account88",None)
            a.parent_account = request.POST.get("parent_account88",None)
            a.bank_account_no = request.POST.get("account_number",None)
            a.currency = request.POST.get("currency",None)
        
        if a.account_type=="Income":
            a.credit_no = request.POST.get("credit_number",None)
            a.sub_account = request.POST.get("sub_account99",None)
            a.parent_account = request.POST.get("parent_account99",None)
            a.bank_account_no = request.POST.get("account_number",None)
            a.currency = request.POST.get("currency",None)
        
        if a.account_type=="Expense":
            a.credit_no = request.POST.get("credit_number",None)
            a.sub_account = request.POST.get("sub_account100",None)
            a.parent_account = request.POST.get("parent_account100",None)
            a.bank_account_no = request.POST.get("account_number",None)
            a.currency = request.POST.get("currency",None)
        
        if a.account_type=="Cost Of Goods Sold":
            a.credit_no = request.POST.get("credit_number",None)
            a.sub_account = request.POST.get("sub_account111",None)
            a.parent_account = request.POST.get("parent_account111",None)
            a.bank_account_no = request.POST.get("account_number",None)
            a.currency = request.POST.get("currency",None)
        
        if a.account_type=="Other Expense":
            a.credit_no = request.POST.get("credit_number",None)
            a.sub_account = request.POST.get("sub_account222",None)
            a.parent_account = request.POST.get("parent_account222",None)
            a.bank_account_no = request.POST.get("account_number",None)
            a.currency = request.POST.get("currency",None)

        a.save()
        # journal_id = a.id

        # return HttpResponseRedirect(reverse('edit_journal', kwargs={'journal_id': journal_id}))
        return redirect('edit_journal')
    return redirect('edit_journal')

def manual_journal_home(request):
    query = request.GET.get('query')
    filter_type = request.GET.get('filter')

    journals = Journal.objects.all()

    if query:
        journals = journals.filter(
            Q(date__icontains=query) |
            Q(journal_no__icontains=query) |
            Q(reference_no__icontains=query) |
            Q(status__icontains=query) |
            Q(notes__icontains=query) |
            Q(total_debit__icontains=query)
        )

    if filter_type == 'draft':
        journals = journals.filter(status='draft')
    elif filter_type == 'published':
        journals = journals.filter(status='published')

    context = {
        'journal': journals,
        'query': query,
        'filter_type': filter_type
    }
    return render(request, 'manual_journal.html', context)

def add_journal(request):
    accounts = Chart_of_Account.objects.all()
    vendors = vendor_table.objects.all()
    customers = customer.objects.all()

    if request.method == 'POST':
        user = request.user
        date = request.POST.get('date')
        journal_no = request.POST.get('journal_no')
        reference_no = request.POST.get('reference_no')
        notes = request.POST.get('notes')
        currency = request.POST.get('currency')
        cash_journal = request.POST.get('cash_journal') == 'True'

        attachment = request.FILES.get('attachment')  

        journal = Journal(
            user=user,
            date=date,
            journal_no=journal_no,
            reference_no=reference_no,
            notes=notes,
            currency=currency,
            cash_journal=cash_journal,
            attachment=attachment  
        )
        journal.save()

        account_list = request.POST.getlist('account')
        description_list = request.POST.getlist('description')
        contact_list = request.POST.getlist('contact')
        debits_list = request.POST.getlist('debits')
        credits_list = request.POST.getlist('credits')

        total_debit = 0
        total_credit = 0

        for i in range(len(account_list)):
            account = account_list[i]
            description = description_list[i]
            contact = contact_list[i]
            debits = debits_list[i]
            credits = credits_list[i]

            journal_entry = JournalEntry(
                journal=journal,
                account=account,
                description=description,
                contact=contact,
                debits=debits,
                credits=credits
            )
            journal_entry.save()

            total_debit += float(debits) if debits else 0
            total_credit += float(credits) if credits else 0

        difference = total_debit - total_credit

        journal.total_debit = total_debit
        journal.total_credit = total_credit
        journal.difference = difference
        journal.save()

        return redirect('manual_journal_home')

    return render(request, 'add_journal.html', {'accounts': accounts, 'vendors': vendors, 'customers': customers})

# def add_account(request):
#     if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
#         account_type = request.POST.get('accountType')
#         account_name = request.POST.get('accountName')
#         account_code = request.POST.get('accountCode')
#         description = request.POST.get('description')

#         account = Account(accountType=account_type, accountName=account_name, accountCode=account_code, description=description)
#         account.save()

#         return JsonResponse({'success': True, 'message': 'Account created successfully.', 'accountName': account.accountName})

#     return JsonResponse({'success': False, 'message': 'Invalid request.'})

def journal_list(request):
    query = request.GET.get('query')
    filter_param = request.GET.get('filter')

    journals = Journal.objects.all()

    if query:
        journals = journals.filter(
            Q(date__icontains=query) |
            Q(journal_no__icontains=query) |
            Q(reference_no__icontains=query) |
            Q(status__icontains=query) |
            Q(notes__icontains=query) |
            Q(total_debit__icontains=query)
        )

    if filter_param:
        if filter_param == 'draft':
            journals = journals.filter(status='draft')
        elif filter_param == 'published':
            journals = journals.filter(status='published')

    selected_journal_id = request.GET.get('selected_journal_id')
    return render(request, 'journal_list.html', {'journals': journals, 'selected_journal_id': selected_journal_id})

def journal_details(request):
    journal_id = request.GET.get('journal_id')
    journal = get_object_or_404(Journal, id=journal_id)
    journal_entries = JournalEntry.objects.filter(journal=journal)
    
    try:
        company = company_details.objects.get(user=request.user)
        company_name = company.company_name
        address = company.address
    except company_details.DoesNotExist:
        company_name = ''
        address = ''
    
    context = {
        'journal': journal,
        'journal_entries': journal_entries,
        'company_name': company_name,
        'address': address,
    }
    
    return render(request, 'journal_template.html', context)


def delete_journal(request, journal_id):
    journal = Journal.objects.get(id=journal_id)    
    journal_entries = JournalEntry.objects.filter(journal=journal)    
    journal_entries.delete()    
    journal.delete()    
    return redirect('journal_list')

def get_journal_details(request):
    journal_id = request.GET.get('journal_id')
    journal = get_object_or_404(Journal, id=journal_id)
    journal_entries = JournalEntry.objects.filter(journal=journal)
    try:
        company = company_details.objects.get(user=request.user)
        company_name = company.company_name
        address = company.address
    except company_details.DoesNotExist:
        company_name = ''
        address = ''
    
    context = {
        'journal': journal,
        'journal_entries': journal_entries,
        'company_name': company_name,
        'address': address,
    }
    return render(request, 'journal_details.html',context) 

def publish_journal(request):
    if request.method == 'POST':
        journal_id = request.POST.get('journal_id')
        journal = get_object_or_404(Journal, id=journal_id)
        journal.status = 'published'
        journal.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})
    
@csrf_exempt
def journal_comments(request):
    if request.method == 'GET':
        journal_id = request.GET.get('journal_id')
        comments = JournalComment.objects.filter(journal_id=journal_id).order_by('-date_time')
        comment_list = []
        for comment in comments:
            comment_data = {
                'text': comment.text,
                'date_time': comment.date_time.strftime('%Y-%m-%d %H:%M:%S')
            }
            comment_list.append(comment_data)
        return JsonResponse({'comments': comment_list})

    elif request.method == 'POST':
        journal_id = request.POST.get('journal_id')
        comment_text = request.POST.get('comment')

        journal = Journal.objects.get(id=journal_id)
        user = request.user

        comment = JournalComment(journal=journal, user=user, text=comment_text)
        comment.save()

        comment_data = {
            'text': comment.text,
            'date_time': comment.date_time.strftime('%Y-%m-%d %H:%M:%S')
        }

        return JsonResponse({'comment': comment_data})

# @csrf_exempt
# def add_comment(request, journal_id):
#     if request.method == 'POST':
#         journal = get_object_or_404(Journal, id=journal_id)
#         comment_text = request.POST.get('comment', '')
#         user = request.user
#         comment = JournalComment.objects.create(journal=journal, user=user, text=comment_text)
#         new_comment = {
#             'id': comment.id,
#             'text': comment.text,
#             'date_time': comment.date_time.strftime('%Y-%m-%d %H:%M:%S'),
#         }
#         return JsonResponse({'comment': new_comment})
#     else:
#         return JsonResponse({'error': 'Invalid request method'})
    
def add_comment(request, journal_id):
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        journal = get_object_or_404(Journal, id=journal_id)
        comment = JournalComment(journal=journal, text=comment_text)
        comment.save()
        return JsonResponse({'status': 'success', 'date_time': comment.date_time})
    else:
        return JsonResponse({'status': 'error'})
    
def get_comments(request, journal_id):
    journal = get_object_or_404(Journal, id=journal_id)
    comments = journal.comments.filter(active=True) 
    return render(request, 'journal_comments.html', {'comments': comments})
    
def edit_journal(request, journal_id):
    journal = get_object_or_404(Journal, id=journal_id)
    accounts = Chart_of_Account.objects.all()
    vendors = vendor_table.objects.all()
    customers = customer.objects.all()

    if request.method == 'POST':
        date = request.POST.get('date')
        journal_no = request.POST.get('journal_no')
        reference_no = request.POST.get('reference_no')
        notes = request.POST.get('notes')
        currency = request.POST.get('currency')
        cash_journal = request.POST.get('cash_journal') == 'True'

        journal.date = date
        journal.journal_no = journal_no
        journal.reference_no = reference_no
        journal.notes = notes
        journal.currency = currency
        journal.cash_journal = cash_journal       
        journal.user = request.user
        old=journal.attachment
        new = request.FILES.get('attachment')
        if old !=None and new==None:
            journal.attachment=old
        else:
            journal.attachment=new            
        journal.save()

        account_list = request.POST.getlist('account')
        description_list = request.POST.getlist('description')
        contact_list = request.POST.getlist('contact')
        debits_list = request.POST.getlist('debits')
        credits_list = request.POST.getlist('credits')

        total_debit = 0
        total_credit = 0

        JournalEntry.objects.filter(journal=journal).delete()

        for i in range(len(account_list)):
            account = account_list[i]
            description = description_list[i]
            contact = contact_list[i]
            debits = debits_list[i]
            credits = credits_list[i]

            journal_entry = JournalEntry(
                journal=journal,
                account=account,
                description=description,
                contact=contact,
                debits=debits,
                credits=credits
            )
            journal_entry.save()

            total_debit += float(debits) if debits else 0
            total_credit += float(credits) if credits else 0

        difference = total_debit - total_credit

        journal.total_debit = total_debit
        journal.total_credit = total_credit
        journal.difference = difference
        journal.save()

        return redirect('journal_list')

    return render(request, 'edit_journal.html', {'journal': journal, 'accounts': accounts, 'vendors': vendors, 'customers': customers})

def save_pdf(request):
    if request.method == 'POST':
        pdf_data = request.POST.get('pdf_data')
        decoded_pdf_data = base64.b64decode(pdf_data)

        with open('/path/to/your/journal.pdf', 'wb') as f:
            f.write(decoded_pdf_data)

        with open('/path/to/your/journal.pdf', 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="journal.pdf"'
            return response

    return HttpResponse('Invalid request method')