"""Generated from Smithy shape ``com.amazonaws.mediaconnect#EncodingConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.encoding_profile


class EncodingConfig(TypedDict):
    encoding_profile: NotRequired[
        "aws_sdk_mediaconnect.types.encoding_profile.EncodingProfile"
    ]
    """<p> The encoding profile to use when transcoding the NDI source content to a transport stream. You can change this value while the flow is running. </p>"""
    video_max_bitrate: NotRequired["int"]
    """<p> The maximum video bitrate to use when transcoding the NDI source to a transport stream. This parameter enables you to override the default video bitrate within the encoding profile's supported range. </p> <p> The supported range is 10,000,000 - 50,000,000 bits per second (bps). If you don't specify a value, MediaConnect uses the default value of 20,000,000 bps. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncodingConfig) -> dict:
    out: dict = {}
    if "encoding_profile" in value:
        import aws_sdk_mediaconnect.types.encoding_profile

        out["encodingProfile"] = (
            aws_sdk_mediaconnect.types.encoding_profile.serialize_json(
                value["encoding_profile"]
            )
        )
    if "video_max_bitrate" in value:
        out["videoMaxBitrate"] = value["video_max_bitrate"]
    return out


def deserialize_json(data: dict) -> EncodingConfig:
    out: EncodingConfig = {}  # type: ignore[typeddict-item]
    if "encodingProfile" in data:
        import aws_sdk_mediaconnect.types.encoding_profile

        out["encoding_profile"] = (
            aws_sdk_mediaconnect.types.encoding_profile.deserialize_json(
                data["encodingProfile"]
            )
        )
    if "videoMaxBitrate" in data:
        out["video_max_bitrate"] = data["videoMaxBitrate"]
    return out
