"""Generated from Smithy shape ``com.amazonaws.ivs#GetChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs.types.channel_arn


class GetChannelRequest(TypedDict, closed=True):
    arn: "aws_sdk_ivs.types.channel_arn.ChannelArn"
    """<p>ARN of the channel for which the configuration is to be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChannelRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> GetChannelRequest:
    out: GetChannelRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetChannelRequest.arn required")
    return out
