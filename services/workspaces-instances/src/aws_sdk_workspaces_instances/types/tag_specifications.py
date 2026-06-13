"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#TagSpecifications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.tag_specification

TagSpecifications: TypeAlias = list[
    "aws_sdk_workspaces_instances.types.tag_specification.TagSpecification"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagSpecifications) -> list:
    import aws_sdk_workspaces_instances.types.tag_specification

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces_instances.types.tag_specification.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> TagSpecifications:
    import aws_sdk_workspaces_instances.types.tag_specification

    out: TagSpecifications = []
    for item in data:
        out.append(
            aws_sdk_workspaces_instances.types.tag_specification.deserialize_aws_json_1_0(
                item
            )
        )
    return out
