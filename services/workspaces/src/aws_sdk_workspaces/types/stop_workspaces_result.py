"""Generated from Smithy shape ``com.amazonaws.workspaces#StopWorkspacesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.failed_stop_workspace_requests


class StopWorkspacesResult(TypedDict):
    failed_requests: NotRequired[
        "aws_sdk_workspaces.types.failed_stop_workspace_requests.FailedStopWorkspaceRequests"
    ]
    """<p>Information about the WorkSpaces that could not be stopped.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopWorkspacesResult) -> dict:
    out: dict = {}
    if "failed_requests" in value:
        import aws_sdk_workspaces.types.failed_stop_workspace_requests

        out["FailedRequests"] = (
            aws_sdk_workspaces.types.failed_stop_workspace_requests.serialize_aws_json_1_1(
                value["failed_requests"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StopWorkspacesResult:
    out: StopWorkspacesResult = {}  # type: ignore[typeddict-item]
    if "FailedRequests" in data:
        import aws_sdk_workspaces.types.failed_stop_workspace_requests

        out["failed_requests"] = (
            aws_sdk_workspaces.types.failed_stop_workspace_requests.deserialize_aws_json_1_1(
                data["FailedRequests"]
            )
        )
    return out
