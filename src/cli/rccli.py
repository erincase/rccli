import click

from src.cli.profile import profile_command


@click.group(short_help="Interact with the RC API")
def rccli():
    pass


def main():
    rccli.add_command(profile_command)
    rccli()
