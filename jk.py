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


@cli.command('jobs-list')
def jobs_list():
    """Get List of Jobs."""
    jkm.get_jobs_list()


@cli.command('count-all')
def count_all():
    """Get Number of Jobs and Builds"""
    jkm.get_job_build_count()


@cli.command('job-config')
@click.argument('jobname')
def job_config(jobname):
    """Get Job Config"""
    jkm.get_job_config(jobname)


@cli.command('job-info')
@click.argument('jobname')
def job_info(jobname):
    """Get Job Info"""
    jkm.get_job_info(jobname)


@cli.command('build-status')
@click.argument('jobname')
def build_status(jobname):
    """Get last Build status"""
    jkm.lastBuildStatus(jobname)


@cli.command('build-result')
@click.argument('jobname')
def build_result(jobname):
    """Get last Build result"""
    jkm.lastBuildResult(jobname)


if __name__ == '__main__':
    cli()
