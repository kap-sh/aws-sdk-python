"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ListChannelMessagesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.channel_message_summary_list
    import aws_sdk_chime_sdk_messaging.types.chime_arn
    import aws_sdk_chime_sdk_messaging.types.next_token
    import aws_sdk_chime_sdk_messaging.types.sub_channel_id


class ListChannelMessagesResponse(TypedDict, closed=True):
    channel_arn: NotRequired["aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the channel containing the requested messages.</p>"""
    next_token: NotRequired["aws_sdk_chime_sdk_messaging.types.next_token.NextToken"]
    """<p>The token passed by previous API calls until all requested messages are returned.</p>"""
    channel_messages: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.channel_message_summary_list.ChannelMessageSummaryList"
    ]
    """<p>The information about, and content of, each requested message.</p>"""
    sub_channel_id: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
    ]
    """<p>The ID of the SubChannel in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelMessagesResponse) -> dict:
    out: dict = {}
    if "channel_arn" in value:
        out["ChannelArn"] = value["channel_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "channel_messages" in value:
        import aws_sdk_chime_sdk_messaging.types.channel_message_summary_list

        out["ChannelMessages"] = (
            aws_sdk_chime_sdk_messaging.types.channel_message_summary_list.serialize_json(
                value["channel_messages"]
            )
        )
    if "sub_channel_id" in value:
        out["SubChannelId"] = value["sub_channel_id"]
    return out


def deserialize_json(data: dict) -> ListChannelMessagesResponse:
    out: ListChannelMessagesResponse = {}  # type: ignore[typeddict-item]
    if "ChannelArn" in data:
        out["channel_arn"] = data["ChannelArn"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ChannelMessages" in data:
        import aws_sdk_chime_sdk_messaging.types.channel_message_summary_list

        out["channel_messages"] = (
            aws_sdk_chime_sdk_messaging.types.channel_message_summary_list.deserialize_json(
                data["ChannelMessages"]
            )
        )
    if "SubChannelId" in data:
        out["sub_channel_id"] = data["SubChannelId"]
    return out
