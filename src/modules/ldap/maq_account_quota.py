import ldap

from typing import Optional, Dict
from rich.console import Console
console = Console()

from handlers.ldap_connection import LdapHandler

class MaqAccountQuota:
    name = "maq_account_quota"
    desc = "Get ms-DS-MachineAccountQuota value"
    module_protocol = ['ldap']
    opsec_safe = True
    multiple_hosts = False
    user_target = None
    search_filter = '(objectClass=*)'
    requires_args = False
    attributes = 'ms-DS-MachineAccountQuota'

    def __init__(self, context=None, module_options=None):
        self.context = context
        self.module_options: Optional[Dict] = module_options

    def options (self):
        pass

    def on_login(self):
        conn, base_dn = LdapHandler.connection(self)
        results = conn.search(base_dn, self.search_filter, attributes=self.attributes)
        res_status = results[0]
        res_response = results[2][0]
  
        if res_status:
            maq_value = res_response['attributes']['ms-DS-MachineAccountQuota']
            console.print(f'[green][+][/] {self.attributes}: {maq_value}', highlight=False)
        else:
            console.print("[red][!][/] No entries found in the results.")