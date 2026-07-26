"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.setting_attribute


class GetSettingsRequest(TypedDict, closed=True):
    attribute: "capo_auditmanager.types.setting_attribute.SettingAttribute"
    """<p> The list of setting attribute enum values. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSettingsRequest:
    out: GetSettingsRequest = {}  # type: ignore[typeddict-item]
    return out
