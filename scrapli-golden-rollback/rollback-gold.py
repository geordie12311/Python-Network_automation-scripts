#Uses Scrapli to rollback golden image
from nornir import InitNornir
from nornir_scrapli.tasks import send_configs, send_interactive
from nornir.plugins.functions.text import print_result

nr = InitNornir(config_file="config.yaml")


def rollback_golden(task):
    cmds = [
            ("configure replace flash:golden-commit",
            "Enter Y if you are sure you want to proceed. ? [no]", False),
            ("Y\n",
            f"{task.host}#", False)
]
    task.run(task=send_interactive, interact_events=cmds)

def remove_vlans(task):
    vlan_cmds = ["no vlan 2-1001", "no vlan 1006-4094"]
    task.run(task=send_configs, configs=vlan_cmds)

rollback_result = nr.run(name="Rollback Golden", task=rollback_golden)
targets = nr.filter(device="switch")
vlan_result = targets.run(name="Removing VLAN configuration", task=remove_vlans)
print_result(rollback_result)
print_result(vlan_result)