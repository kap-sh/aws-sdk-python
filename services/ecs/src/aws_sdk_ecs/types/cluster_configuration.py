"""Generated from Smithy shape ``com.amazonaws.ecs#ClusterConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.execute_command_configuration
    import aws_sdk_ecs.types.managed_storage_configuration


class ClusterConfiguration(TypedDict):
    execute_command_configuration: NotRequired[
        "aws_sdk_ecs.types.execute_command_configuration.ExecuteCommandConfiguration"
    ]
    """<p>The details of the execute command configuration.</p>"""
    managed_storage_configuration: NotRequired[
        "aws_sdk_ecs.types.managed_storage_configuration.ManagedStorageConfiguration"
    ]
    """<p>The details of the managed storage configuration.</p>"""
