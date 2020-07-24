from typing import List, Optional

from avionix.kubernetes_objects.base_objects import KubernetesBaseObject
from avionix.kubernetes_objects.core import Toleration
from avionix.kubernetes_objects.meta import ListMeta, ObjectMeta
from avionix.yaml.yaml_handling import HelmYaml


class Overhead(HelmYaml):
    """
    :param pod_fixed:PodFixed represents the fixed resource overhead associated with \
        running a pod.
    :type pod_fixed: dict
    """

    def __init__(self, pod_fixed: dict):
        self.podFixed = pod_fixed


class Scheduling(HelmYaml):
    """
    :param tolerations:tolerations are appended (excluding duplicates) to pods running \
        with this RuntimeClass during admission, effectively unioning the set of nodes \
        tolerated by the pod and the RuntimeClass.
    :type tolerations: List[Toleration]
    :param node_selector:nodeSelector lists labels that must be present on nodes that \
        support this RuntimeClass. Pods using this RuntimeClass can only be scheduled \
        to a node matched by this selector. The RuntimeClass nodeSelector is merged \
        with a pod's existing nodeSelector. Any conflicts will cause the pod to be \
        rejected in admission.
    :type node_selector: Optional[dict]
    """

    def __init__(
        self, tolerations: List[Toleration], node_selector: Optional[dict] = None
    ):
        self.tolerations = tolerations
        self.nodeSelector = node_selector


class RuntimeClass(KubernetesBaseObject):
    """
    :param metadata:More info: \
        https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata  # noqa
    :type metadata: ObjectMeta
    :param handler:Handler specifies the underlying runtime and configuration that the \
        CRI implementation will use to handle pods of this class. The possible values \
        are specific to the node & CRI configuration.  It is assumed that all handlers \
        are available on every node, and handlers of the same name are equivalent on \
        every node. For example, a handler called "runc" might specify that the runc \
        OCI runtime (using native Linux containers) will be used to run the containers \
        in a pod. The Handler must conform to the DNS Label (RFC 1123) requirements, \
        and is immutable.
    :type handler: str
    :param scheduling:Scheduling holds the scheduling constraints to ensure that pods \
        running with this RuntimeClass are scheduled to nodes that support it. If \
        scheduling is nil, this RuntimeClass is assumed to be supported by all nodes.
    :type scheduling: Scheduling
    :param overhead:Overhead represents the resource overhead associated with running \
        a pod for a given RuntimeClass. For more details, see \
        https://git.k8s.io/enhancements/keps/sig-node/20190226-pod-overhead.md This \
        field is alpha-level as of Kubernetes v1.15, and is only honored by servers \
        that enable the PodOverhead feature.
    :type overhead: Optional[Overhead]
    :param api_version:APIVersion defines the versioned schema of this representation \
        of an object. Servers should convert recognized schemas to the latest internal \
        value, and may reject unrecognized values. More info: \
        https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa
    :type api_version: Optional[str]
    """

    def __init__(
        self,
        metadata: ObjectMeta,
        handler: str,
        scheduling: Scheduling,
        overhead: Optional[Overhead] = None,
        api_version: Optional[str] = None,
    ):
        super().__init__(api_version)
        self.metadata = metadata
        self.handler = handler
        self.scheduling = scheduling
        self.overhead = overhead


class RuntimeClassList(KubernetesBaseObject):
    """
    :param metadata:Standard list metadata. More info: \
        https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata  # noqa
    :type metadata: ListMeta
    :param items:Items is a list of schema objects.
    :type items: List[RuntimeClass]
    :param api_version:APIVersion defines the versioned schema of this representation \
        of an object. Servers should convert recognized schemas to the latest internal \
        value, and may reject unrecognized values. More info: \
        https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa
    :type api_version: Optional[str]
    """

    def __init__(
        self,
        metadata: ListMeta,
        items: List[RuntimeClass],
        api_version: Optional[str] = None,
    ):
        super().__init__(api_version)
        self.metadata = metadata
        self.items = items
