"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateMonitorSettingsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.monitor_id
    import aws_sdk_deadline.types.settings_map


class UpdateMonitorSettingsRequest(TypedDict):
    monitor_id: "aws_sdk_deadline.types.monitor_id.MonitorId"
    """<p>The unique identifier of the monitor to update settings for.</p>"""
    settings: "aws_sdk_deadline.types.settings_map.SettingsMap"
    """<p>The monitor settings to update as key-value pairs. Keys present in the request are upserted; keys absent are left unchanged. Send an empty string value to delete a key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMonitorSettingsRequest) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.settings_map

    out["settings"] = aws_sdk_deadline.types.settings_map.serialize_json(
        value["settings"]
    )
    return out


def deserialize_json(data: dict) -> UpdateMonitorSettingsRequest:
    out: UpdateMonitorSettingsRequest = {}  # type: ignore[typeddict-item]
    if "settings" in data:
        import aws_sdk_deadline.types.settings_map

        out["settings"] = aws_sdk_deadline.types.settings_map.deserialize_json(
            data["settings"]
        )
    else:
        raise DeserializationError("UpdateMonitorSettingsRequest.settings required")
    return out
