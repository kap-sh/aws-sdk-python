"""Generated from Smithy shape ``com.amazonaws.mediaconvert#StatusUpdateInterval``."""

from typing import Literal, TypeAlias, cast

"""Specify how often MediaConvert sends STATUS_UPDATE events to Amazon CloudWatch Events. Set the interval, in seconds, between status updates. MediaConvert sends an update at this interval from the time the service begins processing your job to the time it completes the transcode or encounters an error."""
StatusUpdateInterval: TypeAlias = Literal[
    "SECONDS_10",
    "SECONDS_12",
    "SECONDS_15",
    "SECONDS_20",
    "SECONDS_30",
    "SECONDS_60",
    "SECONDS_120",
    "SECONDS_180",
    "SECONDS_240",
    "SECONDS_300",
    "SECONDS_360",
    "SECONDS_420",
    "SECONDS_480",
    "SECONDS_540",
    "SECONDS_600",
]


# --- restJson1 ser/de ---
def serialize_json(value: StatusUpdateInterval) -> str:
    return value


def deserialize_json(data: str) -> StatusUpdateInterval:
    return cast(StatusUpdateInterval, data)
