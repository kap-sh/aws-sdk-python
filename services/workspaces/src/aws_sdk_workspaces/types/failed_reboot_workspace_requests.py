"""Generated from Smithy shape ``com.amazonaws.workspaces#FailedRebootWorkspaceRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.failed_workspace_change_request

FailedRebootWorkspaceRequests: TypeAlias = list[
    "aws_sdk_workspaces.types.failed_workspace_change_request.FailedWorkspaceChangeRequest"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedRebootWorkspaceRequests) -> list:
    import aws_sdk_workspaces.types.failed_workspace_change_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces.types.failed_workspace_change_request.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FailedRebootWorkspaceRequests:
    import aws_sdk_workspaces.types.failed_workspace_change_request

    out: FailedRebootWorkspaceRequests = []
    for item in data:
        out.append(
            aws_sdk_workspaces.types.failed_workspace_change_request.deserialize_aws_json_1_1(
                item
            )
        )
    return out
