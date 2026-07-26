"""Generated from Smithy shape ``com.amazonaws.deadline#GetMonitorSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.settings_map


class GetMonitorSettingsResponse(TypedDict, closed=True):
    settings: "capo_deadline.types.settings_map.SettingsMap"
    """<p>The monitor settings as key-value pairs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMonitorSettingsResponse) -> dict:
    out: dict = {}
    import capo_deadline.types.settings_map

    out["settings"] = capo_deadline.types.settings_map.serialize_json(value["settings"])
    return out


def deserialize_json(data: dict) -> GetMonitorSettingsResponse:
    out: GetMonitorSettingsResponse = {}  # type: ignore[typeddict-item]
    if "settings" in data:
        import capo_deadline.types.settings_map

        out["settings"] = capo_deadline.types.settings_map.deserialize_json(
            data["settings"]
        )
    else:
        raise DeserializationError("GetMonitorSettingsResponse.settings required")
    return out
