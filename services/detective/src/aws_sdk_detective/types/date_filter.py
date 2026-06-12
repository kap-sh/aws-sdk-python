"""Generated from Smithy shape ``com.amazonaws.detective#DateFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_detective.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_detective.types.timestamp


class DateFilter(TypedDict):
    start_inclusive: "aws_sdk_detective.types.timestamp.Timestamp"
    """<p>A timestamp representing the start of the time period from when data is filtered, including the start date.</p>"""
    end_inclusive: "aws_sdk_detective.types.timestamp.Timestamp"
    """<p>A timestamp representing the end date of the time period until when data is filtered, including the end date.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DateFilter) -> dict:
    out: dict = {}
    import aws_sdk_detective.types.timestamp

    out["StartInclusive"] = aws_sdk_detective.types.timestamp.serialize_json(
        value["start_inclusive"]
    )
    import aws_sdk_detective.types.timestamp

    out["EndInclusive"] = aws_sdk_detective.types.timestamp.serialize_json(
        value["end_inclusive"]
    )
    return out


def deserialize_json(data: dict) -> DateFilter:
    out: DateFilter = {}  # type: ignore[typeddict-item]
    if "StartInclusive" in data:
        import aws_sdk_detective.types.timestamp

        out["start_inclusive"] = aws_sdk_detective.types.timestamp.deserialize_json(
            data["StartInclusive"]
        )
    else:
        raise DeserializationError("DateFilter.start_inclusive required")
    if "EndInclusive" in data:
        import aws_sdk_detective.types.timestamp

        out["end_inclusive"] = aws_sdk_detective.types.timestamp.deserialize_json(
            data["EndInclusive"]
        )
    else:
        raise DeserializationError("DateFilter.end_inclusive required")
    return out
