"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspacesPoolSessions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.workspaces_pool_session

WorkspacesPoolSessions: TypeAlias = list[
    "capo_workspaces.types.workspaces_pool_session.WorkspacesPoolSession"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspacesPoolSessions) -> list:
    import capo_workspaces.types.workspaces_pool_session

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.workspaces_pool_session.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> WorkspacesPoolSessions:
    import capo_workspaces.types.workspaces_pool_session

    out: WorkspacesPoolSessions = []
    for item in data:
        out.append(
            capo_workspaces.types.workspaces_pool_session.deserialize_aws_json_1_1(item)
        )
    return out
