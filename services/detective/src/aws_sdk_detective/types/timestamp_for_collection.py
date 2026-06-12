"""Generated from Smithy shape ``com.amazonaws.detective#TimestampForCollection``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_detective.types.timestamp


class TimestampForCollection(TypedDict):
    timestamp: NotRequired["aws_sdk_detective.types.timestamp.Timestamp"]
    """<p>The data and time when data collection began for a source package. The value is an ISO8601 formatted string. For example, <code>2021-08-18T16:35:56.284Z</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimestampForCollection) -> dict:
    out: dict = {}
    if "timestamp" in value:
        import aws_sdk_detective.types.timestamp

        out["Timestamp"] = aws_sdk_detective.types.timestamp.serialize_json(
            value["timestamp"]
        )
    return out


def deserialize_json(data: dict) -> TimestampForCollection:
    out: TimestampForCollection = {}  # type: ignore[typeddict-item]
    if "Timestamp" in data:
        import aws_sdk_detective.types.timestamp

        out["timestamp"] = aws_sdk_detective.types.timestamp.deserialize_json(
            data["Timestamp"]
        )
    return out
