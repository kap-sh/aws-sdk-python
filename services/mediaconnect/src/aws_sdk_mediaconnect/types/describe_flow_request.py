"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DescribeFlowRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.flow_arn

class DescribeFlowRequest(TypedDict):
    flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn"
    """<p> The ARN of the flow that you want to describe.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DescribeFlowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeFlowRequest:
    out: DescribeFlowRequest = {}  # type: ignore[typeddict-item]
    return out