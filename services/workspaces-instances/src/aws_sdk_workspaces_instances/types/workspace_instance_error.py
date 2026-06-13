"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#WorkspaceInstanceError``."""

from typing import TypedDict

from typing_extensions import NotRequired


class WorkspaceInstanceError(TypedDict):
    error_code: NotRequired["str"]
    """<p>Unique error code for the WorkSpace Instance error.</p>"""
    error_message: NotRequired["str"]
    """<p>Detailed description of the WorkSpace Instance error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkspaceInstanceError) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkspaceInstanceError:
    out: WorkspaceInstanceError = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
