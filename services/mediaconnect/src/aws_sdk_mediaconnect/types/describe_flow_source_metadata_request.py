"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DescribeFlowSourceMetadataRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.flow_arn

class DescribeFlowSourceMetadataRequest(TypedDict):
    flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn"
    """<p> The Amazon Resource Name (ARN) of the flow.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DescribeFlowSourceMetadataRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeFlowSourceMetadataRequest:
    out: DescribeFlowSourceMetadataRequest = {}  # type: ignore[typeddict-item]
    return out