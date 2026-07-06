"""Generated from Smithy shape ``com.amazonaws.mediaconnect#StopFlowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.flow_arn


class StopFlowRequest(TypedDict, closed=True):
    flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn"
    """<p> The Amazon Resource Name (ARN) of the flow that you want to stop.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopFlowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopFlowRequest:
    out: StopFlowRequest = {}  # type: ignore[typeddict-item]
    return out
