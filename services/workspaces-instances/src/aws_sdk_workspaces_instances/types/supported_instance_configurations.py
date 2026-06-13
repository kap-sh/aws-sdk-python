"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#SupportedInstanceConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.supported_instance_configuration

SupportedInstanceConfigurations: TypeAlias = list[
    "aws_sdk_workspaces_instances.types.supported_instance_configuration.SupportedInstanceConfiguration"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SupportedInstanceConfigurations) -> list:
    import aws_sdk_workspaces_instances.types.supported_instance_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces_instances.types.supported_instance_configuration.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SupportedInstanceConfigurations:
    import aws_sdk_workspaces_instances.types.supported_instance_configuration

    out: SupportedInstanceConfigurations = []
    for item in data:
        out.append(
            aws_sdk_workspaces_instances.types.supported_instance_configuration.deserialize_aws_json_1_0(
                item
            )
        )
    return out
