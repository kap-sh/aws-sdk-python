"""Generated from Smithy shape ``com.amazonaws.mediaconnect#StartFlowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.flow_arn


class StartFlowRequest(TypedDict, closed=True):
    flow_arn: "capo_mediaconnect.types.flow_arn.FlowArn"
    """<p> The Amazon Resource Name (ARN) of the flow that you want to start.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartFlowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StartFlowRequest:
    out: StartFlowRequest = {}  # type: ignore[typeddict-item]
    return out
