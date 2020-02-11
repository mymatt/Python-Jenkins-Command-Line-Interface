#!/usr/bin/python

import click
import os

from jkmanager import jenkinsmanager

jkm = None

jenkins_user = os.environ['JENKINS_USER']
jenkins_pass = os.environ['JENKINS_PASS']
jenkins_url = 'http://jenkins.com'

@click.group()
@click.option('--url', default=jenkins_url, help='Jenkins URL')
@click.option('--user', default=jenkins_user, help='Jenkins User')
@click.option('--pass', default=jenkins_pass, help='Jenkins Pass')
def cli(url, user, pass):
    global jkm
    jkm = jenkinsmanager(url, user, pass)


@cli.command('version')
def version():
    """Get Jenkins Version."""
    jkm.get_version()


if __name__ == '__main__':
    cli()
