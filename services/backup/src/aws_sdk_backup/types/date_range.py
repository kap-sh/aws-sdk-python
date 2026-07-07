"""Generated from Smithy shape ``com.amazonaws.backup#DateRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_backup.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_backup.types.timestamp


class DateRange(TypedDict, closed=True):
    from_date: "aws_sdk_backup.types.timestamp.timestamp"
    """<p>This value is the beginning date, inclusive.</p> <p>The date and time are in Unix format and Coordinated Universal Time (UTC), and it is accurate to milliseconds (milliseconds are optional).</p>"""
    to_date: "aws_sdk_backup.types.timestamp.timestamp"
    """<p>This value is the end date, inclusive.</p> <p>The date and time are in Unix format and Coordinated Universal Time (UTC), and it is accurate to milliseconds (milliseconds are optional).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DateRange) -> dict:
    out: dict = {}
    import aws_sdk_backup.types.timestamp

    out["FromDate"] = aws_sdk_backup.types.timestamp.serialize_json(value["from_date"])
    import aws_sdk_backup.types.timestamp

    out["ToDate"] = aws_sdk_backup.types.timestamp.serialize_json(value["to_date"])
    return out


def deserialize_json(data: dict) -> DateRange:
    out: DateRange = {}  # type: ignore[typeddict-item]
    if "FromDate" in data:
        import aws_sdk_backup.types.timestamp

        out["from_date"] = aws_sdk_backup.types.timestamp.deserialize_json(
            data["FromDate"]
        )
    else:
        raise DeserializationError("DateRange.from_date required")
    if "ToDate" in data:
        import aws_sdk_backup.types.timestamp

        out["to_date"] = aws_sdk_backup.types.timestamp.deserialize_json(data["ToDate"])
    else:
        raise DeserializationError("DateRange.to_date required")
    return out
