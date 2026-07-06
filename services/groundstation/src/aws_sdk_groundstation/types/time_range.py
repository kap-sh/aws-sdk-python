"""Generated from Smithy shape ``com.amazonaws.groundstation#TimeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import datetime


class TimeRange(TypedDict, closed=True):
    start_time: "datetime.datetime"
    """<p>Unix epoch timestamp in UTC at which the time range starts.</p>"""
    end_time: "datetime.datetime"
    """<p>Unix epoch timestamp in UTC at which the time range ends.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeRange) -> dict:
    out: dict = {}
    import aws_sdk_groundstation.types._prelude.timestamp

    out["startTime"] = aws_sdk_groundstation.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    import aws_sdk_groundstation.types._prelude.timestamp

    out["endTime"] = aws_sdk_groundstation.types._prelude.timestamp.serialize_json(
        value["end_time"]
    )
    return out


def deserialize_json(data: dict) -> TimeRange:
    out: TimeRange = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        import aws_sdk_groundstation.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_groundstation.types._prelude.timestamp.deserialize_json(
                data["startTime"]
            )
        )
    else:
        raise DeserializationError("TimeRange.start_time required")
    if "endTime" in data:
        import aws_sdk_groundstation.types._prelude.timestamp

        out["end_time"] = (
            aws_sdk_groundstation.types._prelude.timestamp.deserialize_json(
                data["endTime"]
            )
        )
    else:
        raise DeserializationError("TimeRange.end_time required")
    return out
