from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

list = []

def prepchecks():
    list = [1,2,3]
    return list

class MyCustomPolicy(BaseResourceCheck):
    def __init__(self):
        name = "Ensure that a cluster has the name xyz"
        id = "CKV_COMPLEX_3"
        supported_resources = ['aws_ecs_cluster']
        categories = [CheckCategories.LOGGING]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        i=1

        if i in list:
            return CheckResult.PASSED
        else:
            return CheckResult.FAILED
        #return CheckResult.PASSED if conf['name'][0] == 'xyz' else CheckResult.FAILED


list = prepchecks()
check = MyCustomPolicy()