"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DescribeFlowSourceThumbnailRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.flow_arn


class DescribeFlowSourceThumbnailRequest(TypedDict, closed=True):
    flow_arn: "capo_mediaconnect.types.flow_arn.FlowArn"
    """<p> The Amazon Resource Name (ARN) of the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeFlowSourceThumbnailRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeFlowSourceThumbnailRequest:
    out: DescribeFlowSourceThumbnailRequest = {}  # type: ignore[typeddict-item]
    return out
