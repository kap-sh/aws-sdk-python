"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspacesIpGroupsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.workspaces_ip_group

WorkspacesIpGroupsList: TypeAlias = list[
    "aws_sdk_workspaces.types.workspaces_ip_group.WorkspacesIpGroup"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspacesIpGroupsList) -> list:
    import aws_sdk_workspaces.types.workspaces_ip_group

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces.types.workspaces_ip_group.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> WorkspacesIpGroupsList:
    import aws_sdk_workspaces.types.workspaces_ip_group

    out: WorkspacesIpGroupsList = []
    for item in data:
        out.append(
            aws_sdk_workspaces.types.workspaces_ip_group.deserialize_aws_json_1_1(item)
        )
    return out
