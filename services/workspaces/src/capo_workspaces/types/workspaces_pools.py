"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspacesPools``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.workspaces_pool

WorkspacesPools: TypeAlias = list[
    "capo_workspaces.types.workspaces_pool.WorkspacesPool"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspacesPools) -> list:
    import capo_workspaces.types.workspaces_pool

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.workspaces_pool.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> WorkspacesPools:
    import capo_workspaces.types.workspaces_pool

    out: WorkspacesPools = []
    for item in data:
        out.append(capo_workspaces.types.workspaces_pool.deserialize_aws_json_1_1(item))
    return out
