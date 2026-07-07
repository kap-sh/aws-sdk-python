"""Generated from Smithy shape ``com.amazonaws.chime#RoomRetentionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.retention_days


class RoomRetentionSettings(TypedDict, closed=True):
    retention_days: NotRequired["aws_sdk_chime.types.retention_days.RetentionDays"]
    """<p>The number of days for which to retain chat-room messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoomRetentionSettings) -> dict:
    out: dict = {}
    if "retention_days" in value:
        out["RetentionDays"] = value["retention_days"]
    return out


def deserialize_json(data: dict) -> RoomRetentionSettings:
    out: RoomRetentionSettings = {}  # type: ignore[typeddict-item]
    if "RetentionDays" in data:
        out["retention_days"] = data["RetentionDays"]
    return out
