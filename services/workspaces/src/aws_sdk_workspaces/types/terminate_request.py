"""Generated from Smithy shape ``com.amazonaws.workspaces#TerminateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.workspace_id


class TerminateRequest(TypedDict, closed=True):
    workspace_id: "aws_sdk_workspaces.types.workspace_id.WorkspaceId"
    """<p>The identifier of the WorkSpace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminateRequest) -> dict:
    out: dict = {}
    out["WorkspaceId"] = value["workspace_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TerminateRequest:
    out: TerminateRequest = {}  # type: ignore[typeddict-item]
    if "WorkspaceId" in data:
        out["workspace_id"] = data["WorkspaceId"]
    else:
        raise DeserializationError("TerminateRequest.workspace_id required")
    return out
