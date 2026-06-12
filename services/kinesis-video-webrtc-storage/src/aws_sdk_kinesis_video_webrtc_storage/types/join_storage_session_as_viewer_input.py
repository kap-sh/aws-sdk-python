"""Generated from Smithy shape ``com.amazonaws.kinesisvideowebrtcstorage#JoinStorageSessionAsViewerInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kinesis_video_webrtc_storage.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_video_webrtc_storage.types.channel_arn
    import aws_sdk_kinesis_video_webrtc_storage.types.client_id


class JoinStorageSessionAsViewerInput(TypedDict):
    channel_arn: "aws_sdk_kinesis_video_webrtc_storage.types.channel_arn.ChannelArn"
    """<p> The Amazon Resource Name (ARN) of the signaling channel. </p>"""
    client_id: "aws_sdk_kinesis_video_webrtc_storage.types.client_id.ClientId"
    """<p> The unique identifier for the sender client. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JoinStorageSessionAsViewerInput) -> dict:
    out: dict = {}
    out["channelArn"] = value["channel_arn"]
    out["clientId"] = value["client_id"]
    return out


def deserialize_json(data: dict) -> JoinStorageSessionAsViewerInput:
    out: JoinStorageSessionAsViewerInput = {}  # type: ignore[typeddict-item]
    if "channelArn" in data:
        out["channel_arn"] = data["channelArn"]
    else:
        raise DeserializationError(
            "JoinStorageSessionAsViewerInput.channel_arn required"
        )
    if "clientId" in data:
        out["client_id"] = data["clientId"]
    else:
        raise DeserializationError("JoinStorageSessionAsViewerInput.client_id required")
    return out
