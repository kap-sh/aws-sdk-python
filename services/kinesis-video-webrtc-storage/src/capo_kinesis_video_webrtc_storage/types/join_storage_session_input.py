"""Generated from Smithy shape ``com.amazonaws.kinesisvideowebrtcstorage#JoinStorageSessionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_video_webrtc_storage.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_video_webrtc_storage.types.channel_arn


class JoinStorageSessionInput(TypedDict, closed=True):
    channel_arn: "capo_kinesis_video_webrtc_storage.types.channel_arn.ChannelArn"
    """<p> The Amazon Resource Name (ARN) of the signaling channel. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JoinStorageSessionInput) -> dict:
    out: dict = {}
    out["channelArn"] = value["channel_arn"]
    return out


def deserialize_json(data: dict) -> JoinStorageSessionInput:
    out: JoinStorageSessionInput = {}  # type: ignore[typeddict-item]
    if "channelArn" in data:
        out["channel_arn"] = data["channelArn"]
    else:
        raise DeserializationError("JoinStorageSessionInput.channel_arn required")
    return out
