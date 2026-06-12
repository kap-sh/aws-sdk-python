"""Generated from Smithy shape ``com.amazonaws.workspacesweb#AssociateNetworkSettingsRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn

class AssociateNetworkSettingsRequest(TypedDict):
    portal_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the web portal.</p>"""
    network_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the network settings.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AssociateNetworkSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AssociateNetworkSettingsRequest:
    out: AssociateNetworkSettingsRequest = {}  # type: ignore[typeddict-item]
    return out