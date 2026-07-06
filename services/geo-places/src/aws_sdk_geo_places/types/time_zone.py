"""Generated from Smithy shape ``com.amazonaws.geoplaces#TimeZone``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_geo_places.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.duration_seconds
    import aws_sdk_geo_places.types.sensitive_string


class TimeZone(TypedDict, closed=True):
    name: "aws_sdk_geo_places.types.sensitive_string.SensitiveString"
    """<p>The time zone name.</p>"""
    offset: NotRequired["aws_sdk_geo_places.types.sensitive_string.SensitiveString"]
    """<p>Time zone offset of the timezone from UTC.</p>"""
    offset_seconds: "aws_sdk_geo_places.types.duration_seconds.DurationSeconds"
    """<p>The offset of the time zone from UTC, in seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeZone) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "offset" in value:
        out["Offset"] = value["offset"]
    out["OffsetSeconds"] = value.get("offset_seconds", 0)
    return out


def deserialize_json(data: dict) -> TimeZone:
    out: TimeZone = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("TimeZone.name required")
    if "Offset" in data:
        out["offset"] = data["Offset"]
    if "OffsetSeconds" in data:
        out["offset_seconds"] = data["OffsetSeconds"]
    else:
        out["offset_seconds"] = 0
    return out
