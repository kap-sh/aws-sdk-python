"""Generated from Smithy shape ``com.amazonaws.devopsguru#EventTimeRange``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_devops_guru.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.timestamp


class EventTimeRange(TypedDict):
    from_time: "aws_sdk_devops_guru.types.timestamp.Timestamp"
    """<p> The time when the event started. </p>"""
    to_time: "aws_sdk_devops_guru.types.timestamp.Timestamp"
    """<p> The time when the event ended. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventTimeRange) -> dict:
    out: dict = {}
    import aws_sdk_devops_guru.types.timestamp

    out["FromTime"] = aws_sdk_devops_guru.types.timestamp.serialize_json(
        value["from_time"]
    )
    import aws_sdk_devops_guru.types.timestamp

    out["ToTime"] = aws_sdk_devops_guru.types.timestamp.serialize_json(value["to_time"])
    return out


def deserialize_json(data: dict) -> EventTimeRange:
    out: EventTimeRange = {}  # type: ignore[typeddict-item]
    if "FromTime" in data:
        import aws_sdk_devops_guru.types.timestamp

        out["from_time"] = aws_sdk_devops_guru.types.timestamp.deserialize_json(
            data["FromTime"]
        )
    else:
        raise DeserializationError("EventTimeRange.from_time required")
    if "ToTime" in data:
        import aws_sdk_devops_guru.types.timestamp

        out["to_time"] = aws_sdk_devops_guru.types.timestamp.deserialize_json(
            data["ToTime"]
        )
    else:
        raise DeserializationError("EventTimeRange.to_time required")
    return out
