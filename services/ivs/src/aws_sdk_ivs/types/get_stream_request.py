"""Generated from Smithy shape ``com.amazonaws.ivs#GetStreamRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs.types.channel_arn


class GetStreamRequest(TypedDict):
    channel_arn: "aws_sdk_ivs.types.channel_arn.ChannelArn"
    """<p>Channel ARN for stream to be accessed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStreamRequest) -> dict:
    out: dict = {}
    out["channelArn"] = value["channel_arn"]
    return out


def deserialize_json(data: dict) -> GetStreamRequest:
    out: GetStreamRequest = {}  # type: ignore[typeddict-item]
    if "channelArn" in data:
        out["channel_arn"] = data["channelArn"]
    else:
        raise DeserializationError("GetStreamRequest.channel_arn required")
    return out
