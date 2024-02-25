from rich.console import Console
console = Console()
from rich.table import Table

def help_table() -> None:
    ''' Return the list of available commands through Tab's rich module '''

    table = Table(
        title="BREADS - Commands List", 
        caption='All available commands for different protocols and profile management',  
        show_lines=True, 
        show_header=True,
        highlight=False,
        leading=True
    )

    table.add_column("Protocol", style="green")
    table.add_column("Name", style="white")
    table.add_column("Description", style="green")
    table.add_column("Usage", style="white")

    table.add_row("N/A", "create_profile", "Ask user input to create a new profile", "create_profile <name>")
    table.add_row("N/A", "load_profile", "Ask user input to load a existing profile", "load_profile <name>")
    table.add_row("N/A", "banner", "Return the banner from the application", "banner")
    table.add_row("LDAP", "list_dcs", "Retrieve 'dNSHostName' from all Domain Controllers", "list_dcs")
    table.add_row("LDAP", "list_users", "Retrieve 'sAMAccountName' from all users", "list_users")
    table.add_row("LDAP", "disabled_accounts", "Retrieve 'sAMAccountName' from all the disabled accounts", "disabled_accounts")
    table.add_row("LDAP", "whoami", "Extract information from a desired account through user input", "whoami <username>")
    table.add_row("LDAP", "list_adcs", "Retrieve 'dNSHostName', 'cn', 'msPKI-Enrollment-Servers from all ADCS computers", "list_adcs")
    table.add_row("LDAP", "administrators", "Get all the accounts from domain that has administrator privilege in somewhere", "administrators")
    table.add_row("LDAP", "computers", "Return all the computers that can be located on the environmen", "computers")
    table.add_row("LDAP", "maq_account_quota", "Get the Macchine Account Quota value domain-level attribute", "maq_account_quota")
    table.add_row("LDAP", "obsolete", "Search for computers with obsolete operating systems", "obsolete")
    table.add_row("LDAP", "cpnl", "Find all Users that need to change password on next login", "cpnl")
    table.add_row("SMB", "get_uac", "Get the UAC value from a specified target", "get_uac <target>")

    console.print(table)