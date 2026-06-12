"""Generated from Smithy shape ``com.amazonaws.workspacesweb#DisassociateNetworkSettingsRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn

class DisassociateNetworkSettingsRequest(TypedDict):
    portal_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the web portal.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DisassociateNetworkSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateNetworkSettingsRequest:
    out: DisassociateNetworkSettingsRequest = {}  # type: ignore[typeddict-item]
    return out