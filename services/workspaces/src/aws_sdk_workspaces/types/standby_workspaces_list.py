"""Generated from Smithy shape ``com.amazonaws.workspaces#StandbyWorkspacesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.standby_workspace

StandbyWorkspacesList: TypeAlias = list[
    "aws_sdk_workspaces.types.standby_workspace.StandbyWorkspace"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StandbyWorkspacesList) -> list:
    import aws_sdk_workspaces.types.standby_workspace

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces.types.standby_workspace.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> StandbyWorkspacesList:
    import aws_sdk_workspaces.types.standby_workspace

    out: StandbyWorkspacesList = []
    for item in data:
        out.append(
            aws_sdk_workspaces.types.standby_workspace.deserialize_aws_json_1_1(item)
        )
    return out
