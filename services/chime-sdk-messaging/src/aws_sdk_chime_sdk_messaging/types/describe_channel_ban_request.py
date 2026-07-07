"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#DescribeChannelBanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.chime_arn


class DescribeChannelBanRequest(TypedDict, closed=True):
    channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel from which the user is banned.</p>"""
    member_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The <code>AppInstanceUserArn</code> of the member being banned.</p>"""
    chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeChannelBanRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeChannelBanRequest:
    out: DescribeChannelBanRequest = {}  # type: ignore[typeddict-item]
    return out
