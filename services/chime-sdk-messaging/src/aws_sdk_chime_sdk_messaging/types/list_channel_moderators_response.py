"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ListChannelModeratorsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.channel_moderator_summary_list
    import aws_sdk_chime_sdk_messaging.types.chime_arn
    import aws_sdk_chime_sdk_messaging.types.next_token


class ListChannelModeratorsResponse(TypedDict):
    channel_arn: NotRequired["aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the channel.</p>"""
    next_token: NotRequired["aws_sdk_chime_sdk_messaging.types.next_token.NextToken"]
    """<p>The token passed by previous API calls until all requested moderators are returned.</p>"""
    channel_moderators: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.channel_moderator_summary_list.ChannelModeratorSummaryList"
    ]
    """<p>The information about and names of each moderator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelModeratorsResponse) -> dict:
    out: dict = {}
    if "channel_arn" in value:
        out["ChannelArn"] = value["channel_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "channel_moderators" in value:
        import aws_sdk_chime_sdk_messaging.types.channel_moderator_summary_list

        out["ChannelModerators"] = (
            aws_sdk_chime_sdk_messaging.types.channel_moderator_summary_list.serialize_json(
                value["channel_moderators"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListChannelModeratorsResponse:
    out: ListChannelModeratorsResponse = {}  # type: ignore[typeddict-item]
    if "ChannelArn" in data:
        out["channel_arn"] = data["ChannelArn"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ChannelModerators" in data:
        import aws_sdk_chime_sdk_messaging.types.channel_moderator_summary_list

        out["channel_moderators"] = (
            aws_sdk_chime_sdk_messaging.types.channel_moderator_summary_list.deserialize_json(
                data["ChannelModerators"]
            )
        )
    return out
