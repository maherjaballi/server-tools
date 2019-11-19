# -*- coding: utf-8 -*-
import openerp
from openerp import api, fields, models, _

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    module_attachment_unindex_content = fields.Boolean(string='Attachment Unindex Content',
        help='This module disables the indexation of attachments content. \n'
          'Attachment model has a field called index_content where the content of the \n'
          'attachment is read and stored directly in the database. This field is useful in \n'
          'order to search content of a file. But most of cases it is not used, so, you \n'
          'can install this module in order to: \n'
          '- **Avoid Duplicating Data:** Because indexation extracts text content from \n'
            'files and put it on the database in order it could be searched, but this \n'
            'implies you have the file data in your ``filestore`` directory, and also part \n'
            '(or sometimes all) of that data in your database too. \n'
          '- **Improve Performance:** Since not all indexed files are plain text, \n'
            'they require extra process to read them. \n'
             '-This installs the module attachment_unindex_content.')
    
    module_auditlog = fields.Boolean(string='Auditlog',
        help='This module allows the administrator to log user operations performed on data \n'
              'models such as ``create``, ``read``, ``write`` and ``delete``. \n')

    module_auto_backup = fields.Boolean(string='Auto-Backup',
        help='A tool for all your back-ups, internal and external!\n')

    module_base_cron_exclusion = fields.Boolean(string='Base Cron Exclusiont',
        help='This module extends the functionality of scheduled actions to allow you to \n'
              'select the ones that should not run simultaneously. \n'
             '-This installs the module account_check_deposit.')


    module_base_exception = fields.Boolean(string='Base Exception',
        help='This module provide an abstract model to manage customizable \n'
              'exceptions to be applied on different models (sale order, invoice, ...). \n'
              'It is not useful for itself. You can see an example of implementation \n'
              'in the sale_exception module. (sale-workflow repository) or \n'
              'purchase_exception module (purchase-workflow repository). \n'
              '-This installs the module base_exception .')

    module_base_fontawesome = fields.Boolean(string='Base Fontawesome',
        help='Provide up to date Fontawesome <http://fontawesome.io/>_ resources.  \n'
            'Current version: 5.7.1 (the version of this module matches it). \n'
            '-This installs the module base_fontawesome .')

    module_base_jsonify = fields.Boolean(string='Base Jsonify',
        help='This module adds a jsonify method to every model of the ORM. \n'
                'It works on the current recordset and requires a single argument parser \n'
                'that specify the field to extract. \n'
             '-This installs the module base_jsonify .')

    module_base_kanban_stage = fields.Boolean(string='Base Kanban Stage',
        help='This module provides a stage model compatible with Kanban views and the  \n'
              'standard views needed to manage these stages. It also provides the \n' 
              '``base.kanban.abstract`` model, which can be inherited to add support for \n' 
              'Kanban views with stages to any other model. Lastly, it includes a base Kanban  \n'
              'view that can be extended as needed. \n'
             '-This installs the module base_kanban_stage .')

    module_base_search_fuzzy = fields.Boolean(string='Base Search Fuzzy',
        help='This addon provides the ability to create GIN or GiST indexes of char and text \n'
                'fields and also to use the search operator `%` in search domains. Currently \n'
                'this module doesnt change the backend search or anything else. It provides \n'
                'only the possibility to perform the fuzzy search for external addons. \n'
             '-This installs the module base_search_fuzzy .')

    module_base_technical_user = fields.Boolean(string='Base Technical User',
        help='This module extends the functionality of company management. \n'
              'It allows you to bind a technical user on the company in order to use it in \n'
                'batch processes. \n'
             '-This installs the module base_technical_user .')

    module_company_country = fields.Boolean(string='Company Country',
        help='This module allow set a country to main company in order to use the hook of  \n'
              'account that install l10n_** based on country of main company. \n'
             '-This installs the module company_country .')

    module_database_cleanup = fields.Boolean(string='Database Cleanup',
        help='Clean your Odoo database from remnants of modules, models, columns and \n'
              'tables left by uninstalled modules (prior to 7.0) or a homebrew database \n'
              'upgrade to a new major version of Odoo. \n'
              'Caution! This module is potentially harmful and can *easily* destroy the \n'
              'integrity of your data. Do not use if you are not entirely comfortable \n'
              'with the technical details of the Odoo data model of *all* the modules \n'
              'that have ever been installed on your database, and do not purge any module, \n'
              'model, column or table if you do not know exactly what you are doing. \n'

             '-This installs the module database_cleanup .')

    module_datetime_formatter = fields.Boolean(string='Datetime Formatter',
        help='This module was written to extend the functionality of Odoo language engine to \n'
                'support formatting `Date`, `Time` and `Datetime` fields easily and allow you to \n'
                'print them in the best format for the user. \n'
             '-This installs the module datetime_formatter .')

    module_dbfilter_from_header = fields.Boolean(string='DBfilter From Header',
        help='This addon lets you pass a dbfilter as a HTTP header. \n'
                'This is interesting for setups where database names cant be mapped to proxied host names. \n'
              '-This installs the module dbfilter_from_header .')

    module_excel_import_export = fields.Boolean(string='Excel Import Export',
        help='The module provide pre-built functions and wizards for developer to build excel import / export / report with ease. \n'
            'Without having to code to create excel file, developer do, \n'
            '- Create menu, action, wizard, model, view a normal Odoo development. \n'
            '- Design excel template using standard Excel application, e.g., colors, fonts, formulas, etc. \n'
            '- Instruct how the data will be located in Excel with simple dictionary instruction or from Odoo UI. \n'
            '- Odoo will combine instruction with excel template, and result in final excel file. \n'
             '-This installs the module excel_import_export .')

    module_excel_import_export_demo = fields.Boolean(string='Excel Import Export Demo',
        help='This module provide some example use case for excel_import_export \n'
                '1. Import/Export Sales Order (import_export_sale_order) \n'
                '2. Import New Sales Orders (import_sale_orders) \n'
                '3. Sales Orders Report (report_sale_order) \n'
                '4. Print Quoation / Order (.xlsx) (report_action/sale_order) \n'
                '5. Run Partner List Report (report_action/partner_list) \n'

                '.. IMPORTANT:: \n'
                   'This is an alpha version, the data model and design can change at any time without warning. \n'
                   'Only for development or testing purpose, do not use in production. \n'
             '-This installs the module excel_import_export_demo .')

    module_fetchmail_notify_error_to_sender = fields.Boolean(string='Fetchmail Notify Error to Sender',
        help='If fetchmail is not able to correctly route an email, the email is \n'
                '"silently" lost (you get an error message in server log). \n'

                'For example, if you configure odoo mail system to route received emails \n'
                'according to recipient address, it may happen users send emails to wrong \n'
                'email address. \n'

                'This module extends the functionality of fetchmail to allow you to \n'
                'automatically send a notification email to sender, when odoo cant \n'
                'correctly process the received email. \n'           
             '-This installs the module fetchmail_notify_error_to_sender .')


    module_html_image_url_extractor = fields.Boolean(string='Html Image URL Extractor',
        help='This module includes a method that extracts image URLs from any chunk of HTML, \n'
              'in appearing order. \n'
             '-This installs the module html_image_url_extractor .')

    module_html_text = fields.Boolean(string='Html Text',
        help='This module just adds a technical utility, but nothing for the end user. \n'
              'If you are a developer and need this utility for your module, see these \n'
              'examples and read the docs inside the code. \n'

              'Python example:: \n'

                  '@api.multi \n'
                  'def some_method(self): \n'
                      '# Get truncated text from an HTML field. It will 40 words and 100 \n'
                      '# characters at most, and will have "..." appended at the end if it \n'
                      '# gets truncated. \n'
                      'truncated_text = self.env["ir.fields.converter"].text_from_html( \n'
                          'self.html_field, 40, 100, "...") \n'

              'QWeb example:: \n'

                  '<t t-esc="env["ir.fields.converter"].text_from_html(doc.html_field)"/> \n'

              '.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas \n'
                 ':alt: Try me on Runbot \n'
                 ':target: https://runbot.odoo-community.org/runbot/149/11.0 \n'
             '-This installs the module html_text .')

    module_module_analysis = fields.Boolean(string='Module Analysis',
        help='This module allows you to know how much code is running on your Odoo \n'
              'instance, group by Type (Odoo Core, OCA, other...) \n'

              'This module can be usefull in the following cases : \n'

              '* To analyse the size of your technical debt, regarding your Custom modules \n'
              '* To know the ratio between Odoo / OCA and Custom modules \n'
              '* To evaluate the amount to pay to odoo to upgrade your custom code, or the \n'
                'induced workload \n'
             '-This installs the module module_analysis .')

    module_module_auto_update = fields.Boolean(string='Module Auto Update',
       help='This addon provides mechanisms to compute sha1 hashes of installed addons, \n'
              'and save them in the database. It also provides a method that exploits these \n'
              'mechanisms to update a database by upgrading only the modules for which the \n'
              'hash has changed since the last successful upgrade. \n'
             '-This installs the module module_auto_update .')

    module_onchange_helper = fields.Boolean(string='Onchange Helper',
        help='This is a technical module. Its goal is to ease the play of onchange method directly called from Python code.\n'
             '-This installs the module onchange_helper .')

   
    module_scheduler_error_mailer = fields.Boolean(string='Scheduler Error Mailer',
        help='This module adds the possibility to send an e-mail when a scheduler raises \n'
              'an error.\n'
             '-This installs the module scheduler_error_mailer .')

    module_sentry = fields.Boolean(string='Sentry',
        help='The module can be installed just like any other Odoo module, by adding the \n'
              'modules directory to Odoo *addons_path*. In order for the module to correctly \n'
              'wrap the Odoo WSGI application, it also needs to be loaded as a server-wide \n'
              'module. This can be done with the ``server_wide_modules`` parameter in your \n'
              'Odoo config file or with the ``--load`` command-line parameter. \n'

              'This module additionally requires the raven_ Python package to be available on \n'
              'the system. It can be installed using pip:: \n'

                  'pip install raven \n'
             '-This installs the module sentry .')

    module_sql_export = fields.Boolean(string='SQl Export',
        help='Allow to export data in csv files FROM sql requests. \n'
                'There are some restrictions in the sql query, you can only read datas. \n'
                'No update, deletion or creation are possible. \n'
                'A new menu named Export is created. \n'
             '-This installs the module sql_export .')

    module_sql_request_abstract = fields.Boolean(string='SQL Request Abstract',
        help='This module provides an abstract model to manage SQL Select requests on database. \n'
              'It is not usefull for itself. You can see an exemple of implementation in the \n'
              'sql_export module. (same repository). \n'
             '-This installs the module sql_request_abstract .')