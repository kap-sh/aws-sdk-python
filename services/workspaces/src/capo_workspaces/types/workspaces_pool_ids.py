"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspacesPoolIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.workspaces_pool_id

WorkspacesPoolIds: TypeAlias = list[
    "capo_workspaces.types.workspaces_pool_id.WorkspacesPoolId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspacesPoolIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> WorkspacesPoolIds:
    return list(data)
