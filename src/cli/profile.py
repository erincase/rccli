import click
import requests

from src.authentication.config import AUTH_HEADER


@click.group('profile', short_help="Interact with RC profiles", cls=click.Group)
def profile_command():
    """
    Interact with profiles.
    """
    pass


@profile_command.command("individual", short_help="Get an individual's profile")
@click.option("--person-id", help="Individual's person ID")
@click.option("--email", help="Individual's email address")
def individual(person_id, email):
    """
    Finds an individual's name, pronouns, and email using their person ID or email address
    """
    if not (person_id or email):
        raise click.BadOptionUsage("person_id / email", "must provide either person_id or email")

    id = person_id if person_id else email

    r = requests.get('https://www.recurse.com/api/v1/profiles/{}'.format(id),
                     headers=AUTH_HEADER)

    info = r.json()
    _print_profile(info)


@profile_command.command("search", short_help="Search for profiles that fit a given criteria")
@click.option("--query-string", help="Search by name, skills, or profile questions")
@click.option("--batch-id", type=int, help="Search by batch ID")
@click.option("--role", help="Filter by RC role",
              type=click.Choice(["recurser", "resident", "facilitator", "faculty"]))
@click.option("--scope", help="Filter by status",
              type=click.Choice(choices=["current", "overlap"]))
def search(query_string, batch_id, role, scope):
    """
    Returns all names/pronouns/email addresses from profiles fitting a given search criteria
    """
    url = 'https://www.recurse.com/api/v1/profiles?'
    if query_string:
        url += "query={}&".format(query_string)
    if batch_id:
        url += "batch_id={}&".format(batch_id)
    if role:
        url += "role={}&".format(role)
    if scope:
        url += "scope={}&".format(scope)

    # deal with pagination (default limit = 20)
    offset = 0
    request_again = True
    while request_again:
        r = requests.get(url + "offset={}".format(offset), headers=AUTH_HEADER)
        profiles = r.json()
        for profile in profiles:
            _print_profile(profile)

        if not r.json():
            request_again = False

        offset += 20


def _print_profile(info):
    click.echo("{} {} ({}) - {}".format(info['first_name'],
                                        info['last_name'],
                                        info['pronouns'],
                                        info['email']))
