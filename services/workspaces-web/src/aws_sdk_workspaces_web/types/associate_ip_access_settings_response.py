"""Generated from Smithy shape ``com.amazonaws.workspacesweb#AssociateIpAccessSettingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn


class AssociateIpAccessSettingsResponse(TypedDict):
    portal_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the web portal.</p>"""
    ip_access_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the IP access settings resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateIpAccessSettingsResponse) -> dict:
    out: dict = {}
    out["portalArn"] = value["portal_arn"]
    out["ipAccessSettingsArn"] = value["ip_access_settings_arn"]
    return out


def deserialize_json(data: dict) -> AssociateIpAccessSettingsResponse:
    out: AssociateIpAccessSettingsResponse = {}  # type: ignore[typeddict-item]
    if "portalArn" in data:
        out["portal_arn"] = data["portalArn"]
    else:
        raise DeserializationError(
            "AssociateIpAccessSettingsResponse.portal_arn required"
        )
    if "ipAccessSettingsArn" in data:
        out["ip_access_settings_arn"] = data["ipAccessSettingsArn"]
    else:
        raise DeserializationError(
            "AssociateIpAccessSettingsResponse.ip_access_settings_arn required"
        )
    return out
