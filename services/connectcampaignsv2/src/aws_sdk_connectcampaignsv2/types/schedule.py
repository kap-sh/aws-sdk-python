"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#Schedule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.iso8601_duration
    import aws_sdk_connectcampaignsv2.types.time_stamp


class Schedule(TypedDict):
    start_time: "aws_sdk_connectcampaignsv2.types.time_stamp.TimeStamp"
    end_time: "aws_sdk_connectcampaignsv2.types.time_stamp.TimeStamp"
    refresh_frequency: NotRequired[
        "aws_sdk_connectcampaignsv2.types.iso8601_duration.Iso8601Duration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: Schedule) -> dict:
    out: dict = {}
    import aws_sdk_connectcampaignsv2.types.time_stamp

    out["startTime"] = aws_sdk_connectcampaignsv2.types.time_stamp.serialize_json(
        value["start_time"]
    )
    import aws_sdk_connectcampaignsv2.types.time_stamp

    out["endTime"] = aws_sdk_connectcampaignsv2.types.time_stamp.serialize_json(
        value["end_time"]
    )
    if "refresh_frequency" in value:
        out["refreshFrequency"] = value["refresh_frequency"]
    return out


def deserialize_json(data: dict) -> Schedule:
    out: Schedule = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        import aws_sdk_connectcampaignsv2.types.time_stamp

        out["start_time"] = (
            aws_sdk_connectcampaignsv2.types.time_stamp.deserialize_json(
                data["startTime"]
            )
        )
    else:
        raise DeserializationError("Schedule.start_time required")
    if "endTime" in data:
        import aws_sdk_connectcampaignsv2.types.time_stamp

        out["end_time"] = aws_sdk_connectcampaignsv2.types.time_stamp.deserialize_json(
            data["endTime"]
        )
    else:
        raise DeserializationError("Schedule.end_time required")
    if "refreshFrequency" in data:
        out["refresh_frequency"] = data["refreshFrequency"]
    return out
