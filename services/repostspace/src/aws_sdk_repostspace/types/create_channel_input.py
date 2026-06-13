"""Generated from Smithy shape ``com.amazonaws.repostspace#CreateChannelInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_repostspace.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_repostspace.types.channel_description
    import aws_sdk_repostspace.types.channel_name
    import aws_sdk_repostspace.types.space_id


class CreateChannelInput(TypedDict):
    space_id: "aws_sdk_repostspace.types.space_id.SpaceId"
    """<p>The unique ID of the private re:Post.</p>"""
    channel_name: "aws_sdk_repostspace.types.channel_name.ChannelName"
    """<p>The name for the channel. This must be unique per private re:Post.</p>"""
    channel_description: NotRequired[
        "aws_sdk_repostspace.types.channel_description.ChannelDescription"
    ]
    """<p>A description for the channel. This is used only to help you identify this channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChannelInput) -> dict:
    out: dict = {}
    out["channelName"] = value["channel_name"]
    if "channel_description" in value:
        out["channelDescription"] = value["channel_description"]
    return out


def deserialize_json(data: dict) -> CreateChannelInput:
    out: CreateChannelInput = {}  # type: ignore[typeddict-item]
    if "channelName" in data:
        out["channel_name"] = data["channelName"]
    else:
        raise DeserializationError("CreateChannelInput.channel_name required")
    if "channelDescription" in data:
        out["channel_description"] = data["channelDescription"]
    return out
