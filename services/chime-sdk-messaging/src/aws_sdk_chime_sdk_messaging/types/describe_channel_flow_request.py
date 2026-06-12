"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#DescribeChannelFlowRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.chime_arn


class DescribeChannelFlowRequest(TypedDict):
    channel_flow_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeChannelFlowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeChannelFlowRequest:
    out: DescribeChannelFlowRequest = {}  # type: ignore[typeddict-item]
    return out
