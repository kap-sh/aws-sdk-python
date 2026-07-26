"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#UpdateChannelFlowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn


class UpdateChannelFlowResponse(TypedDict, closed=True):
    channel_flow_arn: NotRequired["capo_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the channel flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChannelFlowResponse) -> dict:
    out: dict = {}
    if "channel_flow_arn" in value:
        out["ChannelFlowArn"] = value["channel_flow_arn"]
    return out


def deserialize_json(data: dict) -> UpdateChannelFlowResponse:
    out: UpdateChannelFlowResponse = {}  # type: ignore[typeddict-item]
    if "ChannelFlowArn" in data:
        out["channel_flow_arn"] = data["ChannelFlowArn"]
    return out
