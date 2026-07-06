"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#CreateChannelFlowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.chime_arn


class CreateChannelFlowResponse(TypedDict, closed=True):
    channel_flow_arn: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    ]
    """<p>The ARN of the channel flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChannelFlowResponse) -> dict:
    out: dict = {}
    if "channel_flow_arn" in value:
        out["ChannelFlowArn"] = value["channel_flow_arn"]
    return out


def deserialize_json(data: dict) -> CreateChannelFlowResponse:
    out: CreateChannelFlowResponse = {}  # type: ignore[typeddict-item]
    if "ChannelFlowArn" in data:
        out["channel_flow_arn"] = data["ChannelFlowArn"]
    return out
