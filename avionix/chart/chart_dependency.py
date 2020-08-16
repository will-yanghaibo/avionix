from typing import Optional

from yaml import dump

from avionix._process_utils import custom_check_output
from avionix.kubernetes_objects.base_objects import HelmYaml


class ChartDependency(HelmYaml):
    """
    An object that is equivalent to listing a chart dependency in chart info in helm

    You can also set the values.yaml through this configuration to set any values
    that need to be configured within dependencies

    :param name: Name of chart
    :type name: str
    :param version: The version of the chart
    :type version: str
    :param repository: The url of the repository that this chart originates from
    :type repository: str
    :param values: A dictionary representing the yaml to be output in the values.yaml \
        file for this dependency
    :param values: Optional[dict]
    """

    def __init__(
        self,
        name: str,
        version: str,
        repository: str,
        local_repo_name: str,
        values: Optional[dict] = None,
    ):
        self.name = name
        self.version = version
        self.repository = repository
        self.__values = values
        self.__local_repo_name = local_repo_name

    def get_values_yaml(self):
        return dump({self.name: self.__values})

    def add_repo(self):
        custom_check_output(
            f"helm repo add {self.__local_repo_name} " f"{self.repository}"
        )