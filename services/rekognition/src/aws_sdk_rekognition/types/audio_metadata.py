"""Generated from Smithy shape ``com.amazonaws.rekognition#AudioMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.string
    import aws_sdk_rekognition.types.u_long


class AudioMetadata(TypedDict, closed=True):
    codec: NotRequired["aws_sdk_rekognition.types.string.String"]
    """<p>The audio codec used to encode or decode the audio stream. </p>"""
    duration_millis: NotRequired["aws_sdk_rekognition.types.u_long.ULong"]
    """<p>The duration of the audio stream in milliseconds.</p>"""
    sample_rate: NotRequired["aws_sdk_rekognition.types.u_long.ULong"]
    """<p>The sample rate for the audio stream.</p>"""
    number_of_channels: NotRequired["aws_sdk_rekognition.types.u_long.ULong"]
    """<p>The number of audio channels in the segment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AudioMetadata) -> dict:
    out: dict = {}
    if "codec" in value:
        out["Codec"] = value["codec"]
    if "duration_millis" in value:
        out["DurationMillis"] = value["duration_millis"]
    if "sample_rate" in value:
        out["SampleRate"] = value["sample_rate"]
    if "number_of_channels" in value:
        out["NumberOfChannels"] = value["number_of_channels"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AudioMetadata:
    out: AudioMetadata = {}  # type: ignore[typeddict-item]
    if "Codec" in data:
        out["codec"] = data["Codec"]
    if "DurationMillis" in data:
        out["duration_millis"] = data["DurationMillis"]
    if "SampleRate" in data:
        out["sample_rate"] = data["SampleRate"]
    if "NumberOfChannels" in data:
        out["number_of_channels"] = data["NumberOfChannels"]
    return out
