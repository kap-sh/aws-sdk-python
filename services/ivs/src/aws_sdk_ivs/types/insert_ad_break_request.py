"""Generated from Smithy shape ``com.amazonaws.ivs#InsertAdBreakRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs.types.ad_duration_seconds
    import aws_sdk_ivs.types.channel_arn


class InsertAdBreakRequest(TypedDict, closed=True):
    channel_arn: "aws_sdk_ivs.types.channel_arn.ChannelArn"
    """<p>ARN of the channel into which the ad break is inserted.</p>"""
    duration_seconds: "aws_sdk_ivs.types.ad_duration_seconds.AdDurationSeconds"
    """<p>Duration of the ad break, in seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsertAdBreakRequest) -> dict:
    out: dict = {}
    out["channelArn"] = value["channel_arn"]
    out["durationSeconds"] = value["duration_seconds"]
    return out


def deserialize_json(data: dict) -> InsertAdBreakRequest:
    out: InsertAdBreakRequest = {}  # type: ignore[typeddict-item]
    if "channelArn" in data:
        out["channel_arn"] = data["channelArn"]
    else:
        raise DeserializationError("InsertAdBreakRequest.channel_arn required")
    if "durationSeconds" in data:
        out["duration_seconds"] = data["durationSeconds"]
    else:
        raise DeserializationError("InsertAdBreakRequest.duration_seconds required")
    return out
