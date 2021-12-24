#Uses Scrapli to commit golden image to flash
from nornir import InitNornir
from nornir_scrapli.tasks import send_command, send_interactive
from nornir.plugins.functions.text import print_result

nr = InitNornir(config_file="config.yaml")

def commit_golden(task):
    cmds = [("copy run flash:golden-commit", "Destination filename", False), ("\n", f"{task.host}#", False)]
    task.run(task=send_interactive, interact_events=cmds)


result = nr.run(name="Committing Golden Configurations to Flash", task=commit_golden)
print_result(result)
