"""Generated from Smithy shape ``com.amazonaws.workspaces#FailedRebuildWorkspaceRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.failed_workspace_change_request

FailedRebuildWorkspaceRequests: TypeAlias = list[
    "aws_sdk_workspaces.types.failed_workspace_change_request.FailedWorkspaceChangeRequest"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedRebuildWorkspaceRequests) -> list:
    import aws_sdk_workspaces.types.failed_workspace_change_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces.types.failed_workspace_change_request.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FailedRebuildWorkspaceRequests:
    import aws_sdk_workspaces.types.failed_workspace_change_request

    out: FailedRebuildWorkspaceRequests = []
    for item in data:
        out.append(
            aws_sdk_workspaces.types.failed_workspace_change_request.deserialize_aws_json_1_1(
                item
            )
        )
    return out
