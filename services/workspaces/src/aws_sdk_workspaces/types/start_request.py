"""Generated from Smithy shape ``com.amazonaws.workspaces#StartRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.workspace_id


class StartRequest(TypedDict, closed=True):
    workspace_id: NotRequired["aws_sdk_workspaces.types.workspace_id.WorkspaceId"]
    """<p>The identifier of the WorkSpace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartRequest) -> dict:
    out: dict = {}
    if "workspace_id" in value:
        out["WorkspaceId"] = value["workspace_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartRequest:
    out: StartRequest = {}  # type: ignore[typeddict-item]
    if "WorkspaceId" in data:
        out["workspace_id"] = data["WorkspaceId"]
    return out
