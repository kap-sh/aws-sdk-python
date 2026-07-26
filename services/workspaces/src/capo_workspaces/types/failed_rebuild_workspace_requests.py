"""Generated from Smithy shape ``com.amazonaws.workspaces#FailedRebuildWorkspaceRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.failed_workspace_change_request

FailedRebuildWorkspaceRequests: TypeAlias = list[
    "capo_workspaces.types.failed_workspace_change_request.FailedWorkspaceChangeRequest"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedRebuildWorkspaceRequests) -> list:
    import capo_workspaces.types.failed_workspace_change_request

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.failed_workspace_change_request.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FailedRebuildWorkspaceRequests:
    import capo_workspaces.types.failed_workspace_change_request

    out: FailedRebuildWorkspaceRequests = []
    for item in data:
        out.append(
            capo_workspaces.types.failed_workspace_change_request.deserialize_aws_json_1_1(
                item
            )
        )
    return out
