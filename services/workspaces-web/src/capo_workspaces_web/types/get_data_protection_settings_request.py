"""Generated from Smithy shape ``com.amazonaws.workspacesweb#GetDataProtectionSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn


class GetDataProtectionSettingsRequest(TypedDict, closed=True):
    data_protection_settings_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the data protection settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataProtectionSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDataProtectionSettingsRequest:
    out: GetDataProtectionSettingsRequest = {}  # type: ignore[typeddict-item]
    return out
