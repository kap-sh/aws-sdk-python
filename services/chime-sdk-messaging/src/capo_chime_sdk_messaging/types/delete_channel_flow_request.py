"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#DeleteChannelFlowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn


class DeleteChannelFlowRequest(TypedDict, closed=True):
    channel_flow_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteChannelFlowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteChannelFlowRequest:
    out: DeleteChannelFlowRequest = {}  # type: ignore[typeddict-item]
    return out
