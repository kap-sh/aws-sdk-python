"""Generated from Smithy shape ``com.amazonaws.repostspace#CreateChannelOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_repostspace.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_repostspace.types.channel_id


class CreateChannelOutput(TypedDict):
    channel_id: "aws_sdk_repostspace.types.channel_id.ChannelId"
    """<p>The unique ID of the private re:Post channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChannelOutput) -> dict:
    out: dict = {}
    out["channelId"] = value["channel_id"]
    return out


def deserialize_json(data: dict) -> CreateChannelOutput:
    out: CreateChannelOutput = {}  # type: ignore[typeddict-item]
    if "channelId" in data:
        out["channel_id"] = data["channelId"]
    else:
        raise DeserializationError("CreateChannelOutput.channel_id required")
    return out
