"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#DescribeChannelModeratedByAppInstanceUserRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.chime_arn


class DescribeChannelModeratedByAppInstanceUserRequest(TypedDict):
    channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the moderated channel.</p>"""
    app_instance_user_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the user or bot in the moderated channel.</p>"""
    chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeChannelModeratedByAppInstanceUserRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeChannelModeratedByAppInstanceUserRequest:
    out: DescribeChannelModeratedByAppInstanceUserRequest = {}  # type: ignore[typeddict-item]
    return out
