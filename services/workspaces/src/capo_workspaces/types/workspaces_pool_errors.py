"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspacesPoolErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.workspaces_pool_error

WorkspacesPoolErrors: TypeAlias = list[
    "capo_workspaces.types.workspaces_pool_error.WorkspacesPoolError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspacesPoolErrors) -> list:
    import capo_workspaces.types.workspaces_pool_error

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.workspaces_pool_error.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> WorkspacesPoolErrors:
    import capo_workspaces.types.workspaces_pool_error

    out: WorkspacesPoolErrors = []
    for item in data:
        out.append(
            capo_workspaces.types.workspaces_pool_error.deserialize_aws_json_1_1(item)
        )
    return out
