"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#DescribeChannelMembershipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.sub_channel_id


class DescribeChannelMembershipRequest(TypedDict, closed=True):
    channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel.</p>"""
    member_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The <code>AppInstanceUserArn</code> of the member.</p>"""
    chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>"""
    sub_channel_id: NotRequired[
        "capo_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
    ]
    """<p>The ID of the SubChannel in the request. The response contains an <code>ElasticChannelConfiguration</code> object.</p> <note> <p>Only required to get a user’s SubChannel membership details.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeChannelMembershipRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeChannelMembershipRequest:
    out: DescribeChannelMembershipRequest = {}  # type: ignore[typeddict-item]
    return out
