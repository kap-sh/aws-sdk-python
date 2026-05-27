"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedInstancesLocalStorageConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boolean


class ManagedInstancesLocalStorageConfiguration(TypedDict):
    use_local_storage: "aws_sdk_ecs.types.boolean.Boolean"
    """<p>Use instance store volumes for data storage when available. EBS volumes are not provisioned for data storage. If the container instance has multiple instance store volumes, a single data volume is created. Consider defining instance store requirements using the <code>localStorage</code>, <code>localStorageTypes</code> and <code>totalLocalStorageGB</code> properties.</p>"""
