"""Generated from Smithy shape ``com.amazonaws.workspacesweb#GetIpAccessSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn


class GetIpAccessSettingsRequest(TypedDict, closed=True):
    ip_access_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the IP access settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIpAccessSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetIpAccessSettingsRequest:
    out: GetIpAccessSettingsRequest = {}  # type: ignore[typeddict-item]
    return out
