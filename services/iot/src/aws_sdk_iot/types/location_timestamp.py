"""Generated from Smithy shape ``com.amazonaws.iot#LocationTimestamp``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.string


class LocationTimestamp(TypedDict, closed=True):
    value: "aws_sdk_iot.types.string.String"
    """<p>An expression that returns a long epoch time value.</p>"""
    unit: NotRequired["aws_sdk_iot.types.string.String"]
    """<p>The precision of the timestamp value that results from the expression described in <code>value</code>.</p> <p>Valid values: <code>SECONDS</code> | <code>MILLISECONDS</code> | <code>MICROSECONDS</code> | <code>NANOSECONDS</code>. The default is <code>MILLISECONDS</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LocationTimestamp) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    if "unit" in value:
        out["unit"] = value["unit"]
    return out


def deserialize_json(data: dict) -> LocationTimestamp:
    out: LocationTimestamp = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("LocationTimestamp.value required")
    if "unit" in data:
        out["unit"] = data["unit"]
    return out
