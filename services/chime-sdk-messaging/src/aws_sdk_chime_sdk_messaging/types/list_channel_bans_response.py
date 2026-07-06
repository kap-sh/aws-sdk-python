"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ListChannelBansResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.channel_ban_summary_list
    import aws_sdk_chime_sdk_messaging.types.chime_arn
    import aws_sdk_chime_sdk_messaging.types.next_token


class ListChannelBansResponse(TypedDict, closed=True):
    channel_arn: NotRequired["aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the channel.</p>"""
    next_token: NotRequired["aws_sdk_chime_sdk_messaging.types.next_token.NextToken"]
    """<p>The token passed by previous API calls until all requested bans are returned.</p>"""
    channel_bans: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.channel_ban_summary_list.ChannelBanSummaryList"
    ]
    """<p>The information for each requested ban.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelBansResponse) -> dict:
    out: dict = {}
    if "channel_arn" in value:
        out["ChannelArn"] = value["channel_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "channel_bans" in value:
        import aws_sdk_chime_sdk_messaging.types.channel_ban_summary_list

        out["ChannelBans"] = (
            aws_sdk_chime_sdk_messaging.types.channel_ban_summary_list.serialize_json(
                value["channel_bans"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListChannelBansResponse:
    out: ListChannelBansResponse = {}  # type: ignore[typeddict-item]
    if "ChannelArn" in data:
        out["channel_arn"] = data["ChannelArn"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ChannelBans" in data:
        import aws_sdk_chime_sdk_messaging.types.channel_ban_summary_list

        out["channel_bans"] = (
            aws_sdk_chime_sdk_messaging.types.channel_ban_summary_list.deserialize_json(
                data["ChannelBans"]
            )
        )
    return out
