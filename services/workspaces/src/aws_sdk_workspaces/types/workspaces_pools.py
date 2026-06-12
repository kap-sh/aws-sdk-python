"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspacesPools``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.workspaces_pool

WorkspacesPools: TypeAlias = list[
    "aws_sdk_workspaces.types.workspaces_pool.WorkspacesPool"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspacesPools) -> list:
    import aws_sdk_workspaces.types.workspaces_pool

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces.types.workspaces_pool.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> WorkspacesPools:
    import aws_sdk_workspaces.types.workspaces_pool

    out: WorkspacesPools = []
    for item in data:
        out.append(
            aws_sdk_workspaces.types.workspaces_pool.deserialize_aws_json_1_1(item)
        )
    return out
