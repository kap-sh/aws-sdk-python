"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#TimeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.iso8601_time


class TimeRange(TypedDict, closed=True):
    start_time: "aws_sdk_connectcampaignsv2.types.iso8601_time.Iso8601Time"
    end_time: "aws_sdk_connectcampaignsv2.types.iso8601_time.Iso8601Time"


# --- restJson1 ser/de ---
def serialize_json(value: TimeRange) -> dict:
    out: dict = {}
    out["startTime"] = value["start_time"]
    out["endTime"] = value["end_time"]
    return out


def deserialize_json(data: dict) -> TimeRange:
    out: TimeRange = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        out["start_time"] = data["startTime"]
    else:
        raise DeserializationError("TimeRange.start_time required")
    if "endTime" in data:
        out["end_time"] = data["endTime"]
    else:
        raise DeserializationError("TimeRange.end_time required")
    return out
