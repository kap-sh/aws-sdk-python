"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ListChannelsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.channel_privacy
    import aws_sdk_chime_sdk_messaging.types.chime_arn
    import aws_sdk_chime_sdk_messaging.types.max_results
    import aws_sdk_chime_sdk_messaging.types.next_token


class ListChannelsRequest(TypedDict, closed=True):
    app_instance_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstance</code>.</p>"""
    privacy: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.channel_privacy.ChannelPrivacy"
    ]
    """<p>The privacy setting. <code>PUBLIC</code> retrieves all the public channels. <code>PRIVATE</code> retrieves private channels. Only an <code>AppInstanceAdmin</code> can retrieve private channels. </p>"""
    max_results: NotRequired["aws_sdk_chime_sdk_messaging.types.max_results.MaxResults"]
    """<p>The maximum number of channels that you want to return.</p>"""
    next_token: NotRequired["aws_sdk_chime_sdk_messaging.types.next_token.NextToken"]
    """<p>The token passed by previous API calls until all requested channels are returned.</p>"""
    chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListChannelsRequest:
    out: ListChannelsRequest = {}  # type: ignore[typeddict-item]
    return out
