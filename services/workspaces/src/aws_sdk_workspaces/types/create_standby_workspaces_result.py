"""Generated from Smithy shape ``com.amazonaws.workspaces#CreateStandbyWorkspacesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.failed_create_standby_workspaces_request_list
    import aws_sdk_workspaces.types.pending_create_standby_workspaces_request_list


class CreateStandbyWorkspacesResult(TypedDict, closed=True):
    failed_standby_requests: NotRequired[
        "aws_sdk_workspaces.types.failed_create_standby_workspaces_request_list.FailedCreateStandbyWorkspacesRequestList"
    ]
    """<p>Information about the standby WorkSpace that could not be created. </p>"""
    pending_standby_requests: NotRequired[
        "aws_sdk_workspaces.types.pending_create_standby_workspaces_request_list.PendingCreateStandbyWorkspacesRequestList"
    ]
    """<p>Information about the standby WorkSpace that was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateStandbyWorkspacesResult) -> dict:
    out: dict = {}
    if "failed_standby_requests" in value:
        import aws_sdk_workspaces.types.failed_create_standby_workspaces_request_list

        out["FailedStandbyRequests"] = (
            aws_sdk_workspaces.types.failed_create_standby_workspaces_request_list.serialize_aws_json_1_1(
                value["failed_standby_requests"]
            )
        )
    if "pending_standby_requests" in value:
        import aws_sdk_workspaces.types.pending_create_standby_workspaces_request_list

        out["PendingStandbyRequests"] = (
            aws_sdk_workspaces.types.pending_create_standby_workspaces_request_list.serialize_aws_json_1_1(
                value["pending_standby_requests"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateStandbyWorkspacesResult:
    out: CreateStandbyWorkspacesResult = {}  # type: ignore[typeddict-item]
    if "FailedStandbyRequests" in data:
        import aws_sdk_workspaces.types.failed_create_standby_workspaces_request_list

        out["failed_standby_requests"] = (
            aws_sdk_workspaces.types.failed_create_standby_workspaces_request_list.deserialize_aws_json_1_1(
                data["FailedStandbyRequests"]
            )
        )
    if "PendingStandbyRequests" in data:
        import aws_sdk_workspaces.types.pending_create_standby_workspaces_request_list

        out["pending_standby_requests"] = (
            aws_sdk_workspaces.types.pending_create_standby_workspaces_request_list.deserialize_aws_json_1_1(
                data["PendingStandbyRequests"]
            )
        )
    return out
