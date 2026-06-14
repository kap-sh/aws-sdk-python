"""Generated from Smithy shape ``com.amazonaws.workspacesweb#AssociateIpAccessSettingsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn


class AssociateIpAccessSettingsRequest(TypedDict):
    portal_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the web portal.</p>"""
    ip_access_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the IP access settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateIpAccessSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AssociateIpAccessSettingsRequest:
    out: AssociateIpAccessSettingsRequest = {}  # type: ignore[typeddict-item]
    return out
