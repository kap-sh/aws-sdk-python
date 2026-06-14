"""Generated from Smithy shape ``com.amazonaws.workspacesweb#DeleteIpAccessSettingsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn


class DeleteIpAccessSettingsRequest(TypedDict):
    ip_access_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the IP access settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIpAccessSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteIpAccessSettingsRequest:
    out: DeleteIpAccessSettingsRequest = {}  # type: ignore[typeddict-item]
    return out
