from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck



class MyCustomPolicy(BaseResourceCheck):
    def __init__(self):
        name = "Ensure that a cluster has the name xyz"
        id = "CKV_COMPLEX_2"
        supported_resources = ['aws_ecs_cluster']
        categories = [CheckCategories.LOGGING]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        return CheckResult.PASSED if conf['name'][0] == 'xyz' else CheckResult.FAILED


check = MyCustomPolicy()