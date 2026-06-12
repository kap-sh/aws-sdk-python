"""Generated from Smithy shape ``com.amazonaws.workspacesweb#AssociateUserSettingsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_workspaces_web.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn

class AssociateUserSettingsResponse(TypedDict):
    portal_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the web portal.</p>"""
    user_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the user settings.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AssociateUserSettingsResponse) -> dict:
    out: dict = {}
    out["portalArn"] = value["portal_arn"]
    out["userSettingsArn"] = value["user_settings_arn"]
    return out


def deserialize_json(data: dict) -> AssociateUserSettingsResponse:
    out: AssociateUserSettingsResponse = {}  # type: ignore[typeddict-item]
    if "portalArn" in data:
        out["portal_arn"] = data["portalArn"]
    else:
        raise DeserializationError("AssociateUserSettingsResponse.portal_arn required")
    if "userSettingsArn" in data:
        out["user_settings_arn"] = data["userSettingsArn"]
    else:
        raise DeserializationError("AssociateUserSettingsResponse.user_settings_arn required")
    return out