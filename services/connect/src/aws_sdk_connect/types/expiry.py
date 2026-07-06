"""Generated from Smithy shape ``com.amazonaws.connect#Expiry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.duration_in_seconds
    import aws_sdk_connect.types.timestamp


class Expiry(TypedDict, closed=True):
    duration_in_seconds: NotRequired[
        "aws_sdk_connect.types.duration_in_seconds.DurationInSeconds"
    ]
    """<p>The number of seconds to wait before expiring the routing step.</p>"""
    expiry_timestamp: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp indicating when the routing step expires.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Expiry) -> dict:
    out: dict = {}
    if "duration_in_seconds" in value:
        out["DurationInSeconds"] = value["duration_in_seconds"]
    if "expiry_timestamp" in value:
        import aws_sdk_connect.types.timestamp

        out["ExpiryTimestamp"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["expiry_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> Expiry:
    out: Expiry = {}  # type: ignore[typeddict-item]
    if "DurationInSeconds" in data:
        out["duration_in_seconds"] = data["DurationInSeconds"]
    if "ExpiryTimestamp" in data:
        import aws_sdk_connect.types.timestamp

        out["expiry_timestamp"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["ExpiryTimestamp"]
        )
    return out
