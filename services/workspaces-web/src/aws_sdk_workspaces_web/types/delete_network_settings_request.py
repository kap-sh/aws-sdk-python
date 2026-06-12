"""Generated from Smithy shape ``com.amazonaws.workspacesweb#DeleteNetworkSettingsRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn

class DeleteNetworkSettingsRequest(TypedDict):
    network_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the network settings.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteNetworkSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteNetworkSettingsRequest:
    out: DeleteNetworkSettingsRequest = {}  # type: ignore[typeddict-item]
    return out