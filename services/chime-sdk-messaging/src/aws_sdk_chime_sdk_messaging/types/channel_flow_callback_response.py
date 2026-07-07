"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelFlowCallbackResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.callback_id_type
    import aws_sdk_chime_sdk_messaging.types.chime_arn


class ChannelFlowCallbackResponse(TypedDict, closed=True):
    channel_arn: NotRequired["aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the channel.</p>"""
    callback_id: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.callback_id_type.CallbackIdType"
    ]
    """<p>The call back ID passed in the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelFlowCallbackResponse) -> dict:
    out: dict = {}
    if "channel_arn" in value:
        out["ChannelArn"] = value["channel_arn"]
    if "callback_id" in value:
        out["CallbackId"] = value["callback_id"]
    return out


def deserialize_json(data: dict) -> ChannelFlowCallbackResponse:
    out: ChannelFlowCallbackResponse = {}  # type: ignore[typeddict-item]
    if "ChannelArn" in data:
        out["channel_arn"] = data["ChannelArn"]
    if "CallbackId" in data:
        out["callback_id"] = data["CallbackId"]
    return out
