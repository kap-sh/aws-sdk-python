"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RangeOverride``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.end
    import aws_sdk_customer_profiles.types.range_unit
    import aws_sdk_customer_profiles.types.start


class RangeOverride(TypedDict):
    start: "aws_sdk_customer_profiles.types.start.Start"
    """<p>The start time of when to include objects.</p>"""
    end: "aws_sdk_customer_profiles.types.end.End"
    """<p>The end time of when to include objects.</p>"""
    unit: "aws_sdk_customer_profiles.types.range_unit.RangeUnit"
    """<p>The unit for start and end.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RangeOverride) -> dict:
    out: dict = {}
    out["Start"] = value.get("start", 366)
    out["End"] = value.get("end", 0)
    import aws_sdk_customer_profiles.types.range_unit

    out["Unit"] = aws_sdk_customer_profiles.types.range_unit.serialize_json(
        value["unit"]
    )
    return out


def deserialize_json(data: dict) -> RangeOverride:
    out: RangeOverride = {}  # type: ignore[typeddict-item]
    if "Start" in data:
        out["start"] = data["Start"]
    else:
        out["start"] = 366
    if "End" in data:
        out["end"] = data["End"]
    else:
        out["end"] = 0
    if "Unit" in data:
        import aws_sdk_customer_profiles.types.range_unit

        out["unit"] = aws_sdk_customer_profiles.types.range_unit.deserialize_json(
            data["Unit"]
        )
    else:
        raise DeserializationError("RangeOverride.unit required")
    return out
