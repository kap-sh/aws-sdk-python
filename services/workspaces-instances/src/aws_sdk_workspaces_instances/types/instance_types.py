"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#InstanceTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.instance_type_info

InstanceTypes: TypeAlias = list[
    "aws_sdk_workspaces_instances.types.instance_type_info.InstanceTypeInfo"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceTypes) -> list:
    import aws_sdk_workspaces_instances.types.instance_type_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces_instances.types.instance_type_info.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> InstanceTypes:
    import aws_sdk_workspaces_instances.types.instance_type_info

    out: InstanceTypes = []
    for item in data:
        out.append(
            aws_sdk_workspaces_instances.types.instance_type_info.deserialize_aws_json_1_0(
                item
            )
        )
    return out
