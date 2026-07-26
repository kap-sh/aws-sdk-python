"""Generated from Smithy shape ``com.amazonaws.workspacesweb#DeleteIpAccessSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn


class DeleteIpAccessSettingsRequest(TypedDict, closed=True):
    ip_access_settings_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the IP access settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIpAccessSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteIpAccessSettingsRequest:
    out: DeleteIpAccessSettingsRequest = {}  # type: ignore[typeddict-item]
    return out
