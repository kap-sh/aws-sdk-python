"""Generated from Smithy shape ``com.amazonaws.iot#TimestreamTimestamp``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.timestream_timestamp_unit
    import aws_sdk_iot.types.timestream_timestamp_value


class TimestreamTimestamp(TypedDict):
    value: "aws_sdk_iot.types.timestream_timestamp_value.TimestreamTimestampValue"
    """<p>An expression that returns a long epoch time value.</p>"""
    unit: "aws_sdk_iot.types.timestream_timestamp_unit.TimestreamTimestampUnit"
    """<p>The precision of the timestamp value that results from the expression described in <code>value</code>.</p> <p>Valid values: <code>SECONDS</code> | <code>MILLISECONDS</code> | <code>MICROSECONDS</code> | <code>NANOSECONDS</code>. The default is <code>MILLISECONDS</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimestreamTimestamp) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    out["unit"] = value["unit"]
    return out


def deserialize_json(data: dict) -> TimestreamTimestamp:
    out: TimestreamTimestamp = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("TimestreamTimestamp.value required")
    if "unit" in data:
        out["unit"] = data["unit"]
    else:
        raise DeserializationError("TimestreamTimestamp.unit required")
    return out
