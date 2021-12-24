#Script does a ping Test from all points in the network to target devices specified in textfile
import os
from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from rich import print
from rich.console import Console
from rich.table import Table

nr = InitNornir(config_file='config.yaml')
with open('reader.txt', 'r') as f:
    filelines = f.read().splitlines()
with open('reader.txt', 'r') as f:
    COUNT = 0
    for line in f:
        COUNT += 1

CLEAR = "clear"
os.system(CLEAR)
print("[yellow]*[/yellow]" * 5 + "[yellow]INITIALISING FULL NETWORK PING TEST[/yellow]" + "[yellow]*[/yellow]" * 25)
print("Nornir is conducting a full ping test against all targeted addresses...")
print("< [magenta]If there are no alerts: all devices have full reachability[/magenta] >")
print("\n")
print("[cyan][u]SCOPE SUMMARY:[/u][/cyan]")
print("\n")
table1 = Table(title="Enumerating")
table2 = Table(title="Enumerating")
table1.add_column("DEVICE INVENTORY", justify="center", style="cyan")
table2.add_column("TARGETS", justify="center", style="green")
for host in nr.inventory.hosts:
    dev = host
    STRING_HOST = str(dev)
    ipaddr = nr.inventory.hosts[dev].hostname
    STRING_IP = str(ipaddr)
    table1.add_row(STRING_HOST + " (" + STRING_IP + ")")

for targets in filelines:
    table2.add_row(targets)

console = Console()
console.print(table1, table2)
dev_num = len(nr.inventory.hosts)
perm_num = dev_num * COUNT
print("\n")
print(f"[u]Total number of devices in inventory[/u]: [green]{dev_num}[/green]")
print(f"[u]Total number of IP addresses in target list[/u]: [green]{COUNT}[/green]")
print(f"[u]Total number of ping tests[/u]: [green]{perm_num}[/green]")
print("\n")
for target in filelines:
    results = nr.run(send_command, command="ping " + target)
    for dev in results:
        response = results[dev].result
        if not "!!!" in response:
            print(f"[red]ALERT[/red]: {dev} cannot ping [blue]{target}[/blue]")

print("\n")
print("*" * 5 + "[green] TESTS COMPLETE [/green]" + "*" * 46)