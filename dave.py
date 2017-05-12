__author__ = 'Ge Yang'
import click


@click.command()
@click.option('-c', default='./dave.yml', help='location of the configuration file for the experiment')
def main(*args, **kwargs):
    """the dave main script for helping you with experiments."""
    click.echo(args)
    click.echo(kwargs)
    click.echo('hello World!!')
