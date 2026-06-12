"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#CreateChannelModeratorResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.chime_arn
    import aws_sdk_chime_sdk_messaging.types.identity


class CreateChannelModeratorResponse(TypedDict):
    channel_arn: NotRequired["aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the channel.</p>"""
    channel_moderator: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.identity.Identity"
    ]
    """<p>The ARNs of the channel and the moderator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChannelModeratorResponse) -> dict:
    out: dict = {}
    if "channel_arn" in value:
        out["ChannelArn"] = value["channel_arn"]
    if "channel_moderator" in value:
        import aws_sdk_chime_sdk_messaging.types.identity

        out["ChannelModerator"] = (
            aws_sdk_chime_sdk_messaging.types.identity.serialize_json(
                value["channel_moderator"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateChannelModeratorResponse:
    out: CreateChannelModeratorResponse = {}  # type: ignore[typeddict-item]
    if "ChannelArn" in data:
        out["channel_arn"] = data["ChannelArn"]
    if "ChannelModerator" in data:
        import aws_sdk_chime_sdk_messaging.types.identity

        out["channel_moderator"] = (
            aws_sdk_chime_sdk_messaging.types.identity.deserialize_json(
                data["ChannelModerator"]
            )
        )
    return out
