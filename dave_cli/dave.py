__author__ = 'Ge Yang'
import click

path_type = click.Path(exists=True, file_okay=True, dir_okay=True)


# todo: add method alias group. Not Urgent
# class AliasedGroup(click.Group):
#     def get_command(self, ctx, cmd_name):


@click.group()
def cli(*args, **kwargs):
    """dave helps you with experiments. Use dave --help to learn more."""


@cli.command()
@click.argument('runner', nargs=1, type=path_type)
# ,help='path to the job runner of the configuration file')
@click.argument('job-config', nargs=1, type=path_type)
# , help='path to the configuration file of the job')
def add(runner, job_config, *args, **kwargs):
    """add a job to queue."""
    click.echo(runner)
    click.echo(job_config)


@cli.command()
@click.option('-a', '--all', default=False, help='list all jobs, including ones already completed.')
def list(all, *args, **kwargs):
    """list all jobs currently in the queue"""
    click.echo(all)

from .client import connect as _connect
@cli.command()
@click.option('--url', help="url of the dave-server")
def connect(url, *args, **kwargs):
    _connect(url)


