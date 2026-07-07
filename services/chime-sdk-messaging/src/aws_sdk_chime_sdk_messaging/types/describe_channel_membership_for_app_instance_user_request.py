"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#DescribeChannelMembershipForAppInstanceUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.chime_arn


class DescribeChannelMembershipForAppInstanceUserRequest(TypedDict, closed=True):
    channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel to which the user belongs.</p>"""
    app_instance_user_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the user or bot in a channel.</p>"""
    chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeChannelMembershipForAppInstanceUserRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeChannelMembershipForAppInstanceUserRequest:
    out: DescribeChannelMembershipForAppInstanceUserRequest = {}  # type: ignore[typeddict-item]
    return out
