"""Generated from Smithy shape ``com.amazonaws.workspaces#TerminateWorkspacesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.failed_terminate_workspace_requests


class TerminateWorkspacesResult(TypedDict, closed=True):
    failed_requests: NotRequired[
        "aws_sdk_workspaces.types.failed_terminate_workspace_requests.FailedTerminateWorkspaceRequests"
    ]
    """<p>Information about the WorkSpaces that could not be terminated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminateWorkspacesResult) -> dict:
    out: dict = {}
    if "failed_requests" in value:
        import aws_sdk_workspaces.types.failed_terminate_workspace_requests

        out["FailedRequests"] = (
            aws_sdk_workspaces.types.failed_terminate_workspace_requests.serialize_aws_json_1_1(
                value["failed_requests"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TerminateWorkspacesResult:
    out: TerminateWorkspacesResult = {}  # type: ignore[typeddict-item]
    if "FailedRequests" in data:
        import aws_sdk_workspaces.types.failed_terminate_workspace_requests

        out["failed_requests"] = (
            aws_sdk_workspaces.types.failed_terminate_workspace_requests.deserialize_aws_json_1_1(
                data["FailedRequests"]
            )
        )
    return out
