"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsClusterConfigurationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ecs_cluster_configuration_execute_command_configuration_details


class AwsEcsClusterConfigurationDetails(TypedDict):
    execute_command_configuration: NotRequired[
        "aws_sdk_securityhub.types.aws_ecs_cluster_configuration_execute_command_configuration_details.AwsEcsClusterConfigurationExecuteCommandConfigurationDetails"
    ]
    """<p>Contains the run command configuration for the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsClusterConfigurationDetails) -> dict:
    out: dict = {}
    if "execute_command_configuration" in value:
        import aws_sdk_securityhub.types.aws_ecs_cluster_configuration_execute_command_configuration_details

        out["ExecuteCommandConfiguration"] = (
            aws_sdk_securityhub.types.aws_ecs_cluster_configuration_execute_command_configuration_details.serialize_json(
                value["execute_command_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsEcsClusterConfigurationDetails:
    out: AwsEcsClusterConfigurationDetails = {}  # type: ignore[typeddict-item]
    if "ExecuteCommandConfiguration" in data:
        import aws_sdk_securityhub.types.aws_ecs_cluster_configuration_execute_command_configuration_details

        out["execute_command_configuration"] = (
            aws_sdk_securityhub.types.aws_ecs_cluster_configuration_execute_command_configuration_details.deserialize_json(
                data["ExecuteCommandConfiguration"]
            )
        )
    return out
