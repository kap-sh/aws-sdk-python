"""Generated from Smithy shape ``com.amazonaws.kinesisvideosignaling#SendAlexaOfferToMasterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video_signaling.types.client_id
    import capo_kinesis_video_signaling.types.message_payload
    import capo_kinesis_video_signaling.types.resource_arn


class SendAlexaOfferToMasterRequest(TypedDict, closed=True):
    channel_arn: NotRequired[
        "capo_kinesis_video_signaling.types.resource_arn.ResourceARN"
    ]
    """<p>The ARN of the signaling channel by which Alexa and the master peer communicate.</p>"""
    sender_client_id: NotRequired[
        "capo_kinesis_video_signaling.types.client_id.ClientId"
    ]
    """<p>The unique identifier for the sender client.</p>"""
    message_payload: NotRequired[
        "capo_kinesis_video_signaling.types.message_payload.MessagePayload"
    ]
    """<p>The base64-encoded SDP offer content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendAlexaOfferToMasterRequest) -> dict:
    out: dict = {}
    if "channel_arn" in value:
        out["ChannelARN"] = value["channel_arn"]
    if "sender_client_id" in value:
        out["SenderClientId"] = value["sender_client_id"]
    if "message_payload" in value:
        out["MessagePayload"] = value["message_payload"]
    return out


def deserialize_json(data: dict) -> SendAlexaOfferToMasterRequest:
    out: SendAlexaOfferToMasterRequest = {}  # type: ignore[typeddict-item]
    if "ChannelARN" in data:
        out["channel_arn"] = data["ChannelARN"]
    if "SenderClientId" in data:
        out["sender_client_id"] = data["SenderClientId"]
    if "MessagePayload" in data:
        out["message_payload"] = data["MessagePayload"]
    return out
