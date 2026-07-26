"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RemoveFlowOutputRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.flow_arn


class RemoveFlowOutputRequest(TypedDict, closed=True):
    flow_arn: "capo_mediaconnect.types.flow_arn.FlowArn"
    """<p> The Amazon Resource Name (ARN) of the flow that you want to remove an output from.</p>"""
    output_arn: "str"
    """<p> The ARN of the output that you want to remove. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveFlowOutputRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RemoveFlowOutputRequest:
    out: RemoveFlowOutputRequest = {}  # type: ignore[typeddict-item]
    return out
