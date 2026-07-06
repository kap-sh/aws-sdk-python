"""Generated from Smithy shape ``com.amazonaws.amp#WorkspaceConfigurationStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.workspace_configuration_status_code


class WorkspaceConfigurationStatus(TypedDict, closed=True):
    status_code: "aws_sdk_amp.types.workspace_configuration_status_code.WorkspaceConfigurationStatusCode"
    """<p>The current status of the workspace configuration.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason for the current status, if a reason is available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceConfigurationStatus) -> dict:
    out: dict = {}
    out["statusCode"] = value["status_code"]
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_json(data: dict) -> WorkspaceConfigurationStatus:
    out: WorkspaceConfigurationStatus = {}  # type: ignore[typeddict-item]
    if "statusCode" in data:
        out["status_code"] = data["statusCode"]
    else:
        raise DeserializationError("WorkspaceConfigurationStatus.status_code required")
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    return out
