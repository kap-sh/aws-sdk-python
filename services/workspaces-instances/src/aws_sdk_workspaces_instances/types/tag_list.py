"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#TagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.tag

TagList: TypeAlias = list["aws_sdk_workspaces_instances.types.tag.Tag"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagList) -> list:
    import aws_sdk_workspaces_instances.types.tag

    out: list = []
    for item in value:
        out.append(aws_sdk_workspaces_instances.types.tag.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> TagList:
    import aws_sdk_workspaces_instances.types.tag

    out: TagList = []
    for item in data:
        out.append(
            aws_sdk_workspaces_instances.types.tag.deserialize_aws_json_1_0(item)
        )
    return out
