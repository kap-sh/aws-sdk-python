"""Generated from Smithy shape ``com.amazonaws.location#TimeZone``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.sensitive_integer
    import aws_sdk_location.types.sensitive_string


class TimeZone(TypedDict, closed=True):
    name: "aws_sdk_location.types.sensitive_string.SensitiveString"
    r"""<p>The name of the time zone, following the <a href=\"https://www.iana.org/time-zones\"> IANA time zone standard</a>. For example, <code>America/Los_Angeles</code>.</p>"""
    offset: NotRequired["aws_sdk_location.types.sensitive_integer.SensitiveInteger"]
    """<p>The time zone's offset, in seconds, from UTC.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeZone) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "offset" in value:
        out["Offset"] = value["offset"]
    return out


def deserialize_json(data: dict) -> TimeZone:
    out: TimeZone = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("TimeZone.name required")
    if "Offset" in data:
        out["offset"] = data["Offset"]
    return out
