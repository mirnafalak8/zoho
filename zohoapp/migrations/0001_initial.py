# Generated by Django 4.2.1 on 2023-06-29 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountType', models.CharField(max_length=255)),
                ('accountName', models.CharField(max_length=255)),
                ('accountCode', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AddItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(max_length=255)),
                ('Name', models.TextField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('s_desc', models.TextField(max_length=255)),
                ('p_desc', models.TextField(max_length=255)),
                ('creat', models.CharField(max_length=255)),
                ('s_price', models.CharField(max_length=255)),
                ('p_price', models.TextField(max_length=255)),
                ('satus', models.TextField(default='active')),
                ('interstate', models.CharField(default='', max_length=255)),
                ('intrastate', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerName', models.CharField(blank=True, max_length=100, null=True)),
                ('customerType', models.CharField(blank=True, max_length=100, null=True)),
                ('companyName', models.CharField(blank=True, max_length=100, null=True)),
                ('customerEmail', models.CharField(blank=True, max_length=100, null=True)),
                ('customerWorkPhone', models.CharField(blank=True, max_length=100, null=True)),
                ('customerMobile', models.CharField(blank=True, max_length=100, null=True)),
                ('skype', models.CharField(blank=True, max_length=100, null=True)),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
                ('website', models.CharField(blank=True, max_length=100, null=True)),
                ('GSTTreatment', models.CharField(blank=True, max_length=100, null=True)),
                ('placeofsupply', models.CharField(blank=True, max_length=100, null=True)),
                ('Taxpreference', models.CharField(blank=True, max_length=100, null=True)),
                ('currency', models.CharField(blank=True, max_length=100, null=True)),
                ('OpeningBalance', models.IntegerField(blank=True, null=True)),
                ('PaymentTerms', models.CharField(blank=True, max_length=100, null=True)),
                ('PriceList', models.CharField(blank=True, max_length=100, null=True)),
                ('PortalLanguage', models.CharField(blank=True, max_length=100, null=True)),
                ('Facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('Twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('Attention', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('Address1', models.CharField(blank=True, max_length=100, null=True)),
                ('Address2', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=100, null=True)),
                ('phone1', models.CharField(blank=True, max_length=100, null=True)),
                ('fax', models.CharField(blank=True, max_length=100, null=True)),
                ('CPsalutation', models.CharField(blank=True, max_length=100, null=True)),
                ('Firstname', models.CharField(blank=True, max_length=100, null=True)),
                ('Lastname', models.CharField(blank=True, max_length=100, null=True)),
                ('CPemail', models.CharField(blank=True, max_length=100, null=True)),
                ('CPphone', models.CharField(blank=True, max_length=100, null=True)),
                ('CPmobile', models.CharField(blank=True, max_length=100, null=True)),
                ('CPskype', models.CharField(blank=True, max_length=100, null=True)),
                ('CPdesignation', models.CharField(blank=True, max_length=100, null=True)),
                ('CPdepartment', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.TextField(max_length=255)),
                ('order_no', models.IntegerField()),
                ('inv_date', models.DateField()),
                ('due_date', models.DateField()),
                ('igst', models.TextField(max_length=255)),
                ('cgst', models.TextField(max_length=255)),
                ('sgst', models.TextField(max_length=255)),
                ('t_tax', models.FloatField()),
                ('subtotal', models.FloatField()),
                ('grandtotal', models.FloatField()),
                ('cxnote', models.TextField(max_length=255)),
                ('file', models.ImageField(upload_to='documents')),
                ('terms_condition', models.TextField(max_length=255)),
                ('status', models.TextField(max_length=255)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.customer')),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.TextField(max_length=255)),
                ('days', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='payment_terms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Terms', models.CharField(blank=True, max_length=100, null=True)),
                ('Days', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pricelist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('types', models.CharField(max_length=255)),
                ('tax', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('mark', models.CharField(max_length=255)),
                ('percentage', models.IntegerField()),
                ('roundoff', models.CharField(max_length=255)),
                ('currency', models.CharField(max_length=255)),
                ('status', models.TextField(default='active')),
                ('itemtable', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.additem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Account_type', models.TextField(max_length=255)),
                ('Account_name', models.TextField(max_length=255)),
                ('Acount_code', models.TextField(max_length=255)),
                ('Account_desc', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RetainerInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('retainer_invoice_number', models.CharField(max_length=255)),
                ('refrences', models.CharField(max_length=255)),
                ('retainer_invoice_date', models.DateField()),
                ('total_amount', models.CharField(max_length=100)),
                ('customer_notes', models.TextField()),
                ('terms_and_conditions', models.TextField()),
                ('is_draft', models.BooleanField(default=True)),
                ('is_sent', models.BooleanField(default=False)),
                ('customer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Account_type', models.TextField(max_length=255)),
                ('Account_name', models.TextField(max_length=255)),
                ('Acount_code', models.TextField(max_length=255)),
                ('Account_desc', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='vendor_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salutation', models.CharField(max_length=25)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=150)),
                ('vendor_display_name', models.CharField(max_length=150)),
                ('vendor_email', models.CharField(max_length=250)),
                ('vendor_wphone', models.CharField(max_length=50)),
                ('vendor_mphone', models.CharField(max_length=50)),
                ('skype_number', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=250)),
                ('gst_treatment', models.CharField(max_length=100)),
                ('gst_number', models.CharField(max_length=50, null=True)),
                ('pan_number', models.CharField(max_length=50, null=True)),
                ('source_supply', models.CharField(max_length=100)),
                ('currency', models.CharField(max_length=50)),
                ('opening_bal', models.CharField(max_length=100)),
                ('payment_terms', models.CharField(max_length=100)),
                ('battention', models.CharField(default='', max_length=100)),
                ('bcountry', models.CharField(default='', max_length=100)),
                ('baddress', models.CharField(default='', max_length=300)),
                ('bcity', models.CharField(default='', max_length=100)),
                ('bstate', models.CharField(default='', max_length=100)),
                ('bzip', models.CharField(default='', max_length=100)),
                ('bphone', models.CharField(default='', max_length=100)),
                ('bfax', models.CharField(default='', max_length=100)),
                ('sattention', models.CharField(default='', max_length=100)),
                ('scountry', models.CharField(default='', max_length=100)),
                ('saddress', models.CharField(default='', max_length=300)),
                ('scity', models.CharField(default='', max_length=100)),
                ('sstate', models.CharField(default='', max_length=100)),
                ('szip', models.CharField(default='', max_length=100)),
                ('sphone', models.CharField(default='', max_length=100)),
                ('sfax', models.CharField(default='', max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sample_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('cust_rate', models.FloatField()),
                ('pl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.pricelist')),
            ],
        ),
        migrations.CreateModel(
            name='SalesOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sales_no', models.CharField(blank=True, max_length=255, null=True)),
                ('reference', models.CharField(blank=True, max_length=255, null=True)),
                ('sales_date', models.DateField(blank=True, max_length=255, null=True)),
                ('ship_date', models.DateField(blank=True, max_length=255, null=True)),
                ('d_method', models.TextField(blank=True, null=True)),
                ('s_person', models.TextField(blank=True, null=True)),
                ('igst', models.TextField(blank=True, max_length=255, null=True)),
                ('cgst', models.TextField(blank=True, max_length=255, null=True)),
                ('sgst', models.TextField(blank=True, max_length=255, null=True)),
                ('t_tax', models.FloatField(blank=True, null=True)),
                ('subtotal', models.FloatField(blank=True, null=True)),
                ('grandtotal', models.FloatField(blank=True, null=True)),
                ('cxnote', models.TextField(blank=True, max_length=255, null=True)),
                ('file', models.ImageField(blank=True, null=True, upload_to='documents')),
                ('terms_condition', models.TextField(blank=True, max_length=255, null=True)),
                ('status', models.TextField(blank=True, max_length=255, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.customer')),
                ('terms', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.payment_terms')),
            ],
        ),
        migrations.CreateModel(
            name='sales_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.TextField(blank=True, max_length=255, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('hsn', models.TextField(blank=True, max_length=255, null=True)),
                ('tax', models.IntegerField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('desc', models.TextField(blank=True, max_length=255, null=True)),
                ('rate', models.TextField(blank=True, max_length=255, null=True)),
                ('sale', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.salesorder')),
            ],
        ),
        migrations.CreateModel(
            name='Retaineritems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('amount', models.CharField(max_length=100)),
                ('retainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.retainerinvoice')),
            ],
        ),
        migrations.CreateModel(
            name='remarks_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarks', models.CharField(max_length=500)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.vendor_table')),
            ],
        ),
        migrations.CreateModel(
            name='mail_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_from', models.TextField(max_length=300)),
                ('mail_to', models.TextField(max_length=300)),
                ('subject', models.TextField(max_length=250)),
                ('content', models.TextField(max_length=900)),
                ('mail_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.vendor_table')),
            ],
        ),
        migrations.CreateModel(
            name='invoice_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.TextField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('hsn', models.TextField(max_length=255)),
                ('tax', models.IntegerField()),
                ('total', models.FloatField()),
                ('desc', models.TextField(max_length=255)),
                ('rate', models.TextField(max_length=255)),
                ('inv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.invoice')),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='terms',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.payment_terms'),
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('message', models.CharField(max_length=255)),
                ('p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.additem')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_name', models.CharField(max_length=255)),
                ('repeat_every', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('ends_on', models.DateField()),
                ('expense_account', models.CharField(max_length=255)),
                ('expense_type', models.CharField(max_length=50)),
                ('goods_label', models.CharField(default='', max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(max_length=10)),
                ('paidthrough', models.CharField(max_length=50)),
                ('gst', models.CharField(blank=True, max_length=255)),
                ('destination', models.CharField(blank=True, max_length=255)),
                ('tax', models.CharField(blank=True, max_length=255)),
                ('notes', models.CharField(blank=True, max_length=255)),
                ('customername', models.CharField(blank=True, max_length=255)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.vendor_table')),
            ],
        ),
        migrations.CreateModel(
            name='Estimates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(blank=True, max_length=100, null=True)),
                ('estimate_no', models.CharField(blank=True, max_length=100, null=True)),
                ('reference', models.CharField(blank=True, max_length=100, null=True)),
                ('estimate_date', models.DateField(null=True)),
                ('expiry_date', models.DateField(null=True)),
                ('sub_total', models.FloatField(blank=True, null=True)),
                ('igst', models.FloatField(blank=True, null=True)),
                ('sgst', models.FloatField(blank=True, null=True)),
                ('cgst', models.FloatField(blank=True, null=True)),
                ('tax_amount', models.FloatField(blank=True, null=True)),
                ('shipping_charge', models.FloatField(blank=True, null=True)),
                ('adjustment', models.FloatField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('customer_notes', models.CharField(blank=True, max_length=250, null=True)),
                ('terms_conditions', models.CharField(blank=True, max_length=250, null=True)),
                ('attachment', models.ImageField(null=True, upload_to='image/')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EstimateItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('rate', models.FloatField(blank=True, null=True)),
                ('discount', models.FloatField(blank=True, null=True)),
                ('tax_percentage', models.IntegerField(blank=True, null=True)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('estimate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.estimates')),
            ],
        ),
        migrations.CreateModel(
            name='doc_upload_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200)),
                ('document', models.FileField(upload_to='doc/')),
                ('user', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.vendor_table')),
            ],
        ),
        migrations.CreateModel(
            name='contact_person_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salutation', models.CharField(max_length=25)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=200)),
                ('work_phone', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=50)),
                ('skype_number', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.vendor_table')),
            ],
        ),
        migrations.CreateModel(
            name='company_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_number', models.CharField(blank=True, max_length=100, null=True)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('company_email', models.CharField(blank=True, max_length=255, null=True)),
                ('business_name', models.CharField(blank=True, max_length=255, null=True)),
                ('company_type', models.CharField(blank=True, max_length=255, null=True)),
                ('industry_type', models.CharField(blank=True, max_length=255, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='image/patient')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='comments_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=500)),
                ('user', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.vendor_table')),
            ],
        ),
        migrations.CreateModel(
            name='banking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('alias', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('acc_type', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('ac_holder', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('ac_no', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('ifsc', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('swift_code', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('bnk_name', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('bnk_branch', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('chq_book', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('chq_print', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('chq_config', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('mail_name', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('mail_addr', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('mail_country', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('mail_state', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('mail_pin', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('bd_bnk_det', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('bd_pan_no', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('bd_reg_typ', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('bd_gst_no', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('bd_gst_det', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('opening_bal', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc_type', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('bank_name', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='additem',
            name='purchase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.purchase'),
        ),
        migrations.AddField(
            model_name='additem',
            name='sales',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.sales'),
        ),
        migrations.AddField(
            model_name='additem',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.unit'),
        ),
        migrations.AddField(
            model_name='additem',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
