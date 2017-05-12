__author__ = 'Ge Yang'
import click


@click.command()
@click.option('-c', default='./dave.yml', help='location of the configuration file for the experiment')
def main(c, *args, **kwargs):
    """the dave main script for helping you with experiments."""
    click.echo('using configuration file: '.format(c))

@click.command()
@click.option('-c', default='./dave.yml', help='location of the configuration file for the experiment')
def add(c, *args, **kwargs):
    """the dave main script for helping you with experiments."""
    click.echo('add configuration to list of jobs'.format(c))


@click.command()
def list(c, *args, **kwargs):
    """the dave main script for helping you with experiments."""
    click.echo('list jobs')

