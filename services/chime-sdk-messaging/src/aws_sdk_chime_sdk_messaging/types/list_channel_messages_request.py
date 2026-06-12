"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ListChannelMessagesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.chime_arn
    import aws_sdk_chime_sdk_messaging.types.max_results
    import aws_sdk_chime_sdk_messaging.types.next_token
    import aws_sdk_chime_sdk_messaging.types.sort_order
    import aws_sdk_chime_sdk_messaging.types.sub_channel_id
    import aws_sdk_chime_sdk_messaging.types.timestamp


class ListChannelMessagesRequest(TypedDict):
    channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel.</p>"""
    sort_order: NotRequired["aws_sdk_chime_sdk_messaging.types.sort_order.SortOrder"]
    """<p>The order in which you want messages sorted. Default is Descending, based on time created.</p>"""
    not_before: NotRequired["aws_sdk_chime_sdk_messaging.types.timestamp.Timestamp"]
    """<p>The initial or starting time stamp for your requested messages.</p>"""
    not_after: NotRequired["aws_sdk_chime_sdk_messaging.types.timestamp.Timestamp"]
    """<p>The final or ending time stamp for your requested messages.</p>"""
    max_results: NotRequired["aws_sdk_chime_sdk_messaging.types.max_results.MaxResults"]
    """<p>The maximum number of messages that you want returned.</p>"""
    next_token: NotRequired["aws_sdk_chime_sdk_messaging.types.next_token.NextToken"]
    """<p>The token passed by previous API calls until all requested messages are returned.</p>"""
    chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>"""
    sub_channel_id: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
    ]
    """<p>The ID of the SubChannel in the request.</p> <note> <p>Only required when listing the messages in a SubChannel that the user belongs to.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelMessagesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListChannelMessagesRequest:
    out: ListChannelMessagesRequest = {}  # type: ignore[typeddict-item]
    return out
