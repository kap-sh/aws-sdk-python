"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RemoveFlowMediaStreamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.flow_arn


class RemoveFlowMediaStreamRequest(TypedDict, closed=True):
    flow_arn: "capo_mediaconnect.types.flow_arn.FlowArn"
    """<p> The Amazon Resource Name (ARN) of the flow that you want to update.</p>"""
    media_stream_name: "str"
    """<p> The name of the media stream that you want to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveFlowMediaStreamRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RemoveFlowMediaStreamRequest:
    out: RemoveFlowMediaStreamRequest = {}  # type: ignore[typeddict-item]
    return out
