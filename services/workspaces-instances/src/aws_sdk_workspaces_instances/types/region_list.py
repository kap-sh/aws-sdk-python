"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#RegionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.region

RegionList: TypeAlias = list["aws_sdk_workspaces_instances.types.region.Region"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegionList) -> list:
    import aws_sdk_workspaces_instances.types.region

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces_instances.types.region.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RegionList:
    import aws_sdk_workspaces_instances.types.region

    out: RegionList = []
    for item in data:
        out.append(
            aws_sdk_workspaces_instances.types.region.deserialize_aws_json_1_0(item)
        )
    return out
