"""Generated from Smithy shape ``com.amazonaws.groundstation#ISO8601TimeRange``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import datetime


class ISO8601TimeRange(TypedDict):
    start_time: "datetime.datetime"
    """<p>Start time in ISO 8601 format in Coordinated Universal Time (UTC).</p> <p>Example: <code>2026-11-15T10:28:48.000Z</code> </p>"""
    end_time: "datetime.datetime"
    """<p>End time in ISO 8601 format in Coordinated Universal Time (UTC).</p> <p>Example: <code>2024-01-15T12:00:00.000Z</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ISO8601TimeRange) -> dict:
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


def deserialize_json(data: dict) -> ISO8601TimeRange:
    out: ISO8601TimeRange = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        import aws_sdk_groundstation.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_groundstation.types._prelude.timestamp.deserialize_json(
                data["startTime"]
            )
        )
    else:
        raise DeserializationError("ISO8601TimeRange.start_time required")
    if "endTime" in data:
        import aws_sdk_groundstation.types._prelude.timestamp

        out["end_time"] = (
            aws_sdk_groundstation.types._prelude.timestamp.deserialize_json(
                data["endTime"]
            )
        )
    else:
        raise DeserializationError("ISO8601TimeRange.end_time required")
    return out
