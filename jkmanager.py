#!/usr/bin/python

import jenkins

class jenkinsmanager:

    def __init__(self, jenkins_url, jenkins_user, jenkins_pass):
        self.jenkins_password=jenkins_password
        self.jenkins_user=jenkins_user
        self.jenkins_url=jenkins_url

        try:
            self.server=jenkins.Jenkins(url=self.jenkins_url,username=self.jenkins_user,
                                        password=self.jenkins_password,timeout=20)
        except Exception as e:
            print('Jenkins Exception：%s'%e)
