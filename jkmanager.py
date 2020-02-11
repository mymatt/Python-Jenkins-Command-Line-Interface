#!/usr/bin/python

import jenkins

class jenkinsmanager:

    def __init__(self, jenkins_url, jenkins_user, jenkins_pass):
        self.jenkins_password=jenkins_password
        self.jenkins_user=jenkins_user
        self.jenkins_url=jenkins_url


    def server_instance(self):
        server=jenkins.Jenkins(url=self.jenkins_url,username=self.jenkins_user, password=self.jenkins_password,timeout=20)
        return server


    def get_version(self):
        vers = self.server_instance().get_version()
        print("Jenkins Version Number {}".format(vers))


    def get_jobs_list(self):
        jobs = self.server_instance().get_all_jobs()
        print("Jobs {}".format(jobs))


    def get_job_build_count(self):
        build_total = 0
        print("Number of Jobs: {}".format(self.server_instance().jobs_count()))
        for job in self.server_instance().get_jobs():
            info = self.server_instance().get_job_info(job['name'])
            build_num = str(len(info['builds']))
            print("Jobname: {0}, Build Count: {1}".format(job['name'], build_num))
            build_total += build_num
        print("Total Build Count: {}".format(build_total))


    def get_job_config(self, jobname):
        job_config = self.server_instance().get_job_config(jobname)
        print('Jobconfig of Job {0}: {1}'.format(jobname, job_config))


    def get_job_info(self, jobname):
        job_info = self.server_instance().get_job_info(jobname)
        print('Job Info of Job {0}: {1}'.format(jobname, job_info))


    def lastBuildStatus(self,jobname):
        last_build = self.server_instance().get_job_info(jobname)['lastBuild']['number']
        build_status = self.server_instance().get_build_info(jobname, last_build)['building']
        return build_status


    def lastBuildResult(self,jobname):
        last_build = self.server_instance().get_job_info(jobname)['lastBuild']['number']
        build_result = self.server_instance()).get_build_info(jobname, last_build)['result']
        return build_result
