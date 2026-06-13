"""Generated from Smithy shape ``com.amazonaws.amp#WorkspaceStatus``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.workspace_status_code


class WorkspaceStatus(TypedDict):
    status_code: "aws_sdk_amp.types.workspace_status_code.WorkspaceStatusCode"
    """<p>The current status of the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceStatus) -> dict:
    out: dict = {}
    out["statusCode"] = value["status_code"]
    return out


def deserialize_json(data: dict) -> WorkspaceStatus:
    out: WorkspaceStatus = {}  # type: ignore[typeddict-item]
    if "statusCode" in data:
        out["status_code"] = data["statusCode"]
    else:
        raise DeserializationError("WorkspaceStatus.status_code required")
    return out
