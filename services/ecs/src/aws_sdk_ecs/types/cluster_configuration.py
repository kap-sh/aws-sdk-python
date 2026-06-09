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


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterConfiguration) -> dict:
    out: dict = {}
    if "execute_command_configuration" in value:
        import aws_sdk_ecs.types.execute_command_configuration

        out["executeCommandConfiguration"] = (
            aws_sdk_ecs.types.execute_command_configuration.serialize_aws_json_1_1(
                value["execute_command_configuration"]
            )
        )
    if "managed_storage_configuration" in value:
        import aws_sdk_ecs.types.managed_storage_configuration

        out["managedStorageConfiguration"] = (
            aws_sdk_ecs.types.managed_storage_configuration.serialize_aws_json_1_1(
                value["managed_storage_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterConfiguration:
    out: ClusterConfiguration = {}  # type: ignore[typeddict-item]
    if "executeCommandConfiguration" in data:
        import aws_sdk_ecs.types.execute_command_configuration

        out["execute_command_configuration"] = (
            aws_sdk_ecs.types.execute_command_configuration.deserialize_aws_json_1_1(
                data["executeCommandConfiguration"]
            )
        )
    if "managedStorageConfiguration" in data:
        import aws_sdk_ecs.types.managed_storage_configuration

        out["managed_storage_configuration"] = (
            aws_sdk_ecs.types.managed_storage_configuration.deserialize_aws_json_1_1(
                data["managedStorageConfiguration"]
            )
        )
    return out
