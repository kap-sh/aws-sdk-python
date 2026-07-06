"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ValueRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.value_range_end
    import aws_sdk_customer_profiles.types.value_range_start


class ValueRange(TypedDict, closed=True):
    start: "aws_sdk_customer_profiles.types.value_range_start.ValueRangeStart"
    """<p>The start time of when to include objects. Use positive numbers to indicate that the starting point is in the past, and negative numbers to indicate it is in the future.</p>"""
    end: "aws_sdk_customer_profiles.types.value_range_end.ValueRangeEnd"
    """<p>The end time of when to include objects. Use positive numbers to indicate that the starting point is in the past, and negative numbers to indicate it is in the future.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValueRange) -> dict:
    out: dict = {}
    out["Start"] = value["start"]
    out["End"] = value["end"]
    return out


def deserialize_json(data: dict) -> ValueRange:
    out: ValueRange = {}  # type: ignore[typeddict-item]
    if "Start" in data:
        out["start"] = data["Start"]
    else:
        raise DeserializationError("ValueRange.start required")
    if "End" in data:
        out["end"] = data["End"]
    else:
        raise DeserializationError("ValueRange.end required")
    return out
