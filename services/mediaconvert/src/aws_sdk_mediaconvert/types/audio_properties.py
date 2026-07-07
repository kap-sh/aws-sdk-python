"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AudioProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer
    import aws_sdk_mediaconvert.types.__long
    import aws_sdk_mediaconvert.types.__string
    import aws_sdk_mediaconvert.types.frame_rate


class AudioProperties(TypedDict, closed=True):
    bit_depth: NotRequired["aws_sdk_mediaconvert.types.__integer.__integer"]
    """The bit depth of the audio track."""
    bit_rate: NotRequired["aws_sdk_mediaconvert.types.__long.__long"]
    """The bit rate of the audio track, in bits per second."""
    channels: NotRequired["aws_sdk_mediaconvert.types.__integer.__integer"]
    """The number of audio channels in the audio track."""
    frame_rate: NotRequired["aws_sdk_mediaconvert.types.frame_rate.FrameRate"]
    """The frame rate of the video or audio track, expressed as a fraction with numerator and denominator values."""
    language_code: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """The language code of the audio track, in three character ISO 639-3 format."""
    object_count: NotRequired["aws_sdk_mediaconvert.types.__integer.__integer"]
    """The number of audio objects in an object-based or immersive audio track. This field is present for codecs that support object-based audio, such as E-AC-3 with Joint Object Coding (JOC) or IAMF. This field is null when the audio track does not contain object-based audio metadata."""
    sample_rate: NotRequired["aws_sdk_mediaconvert.types.__integer.__integer"]
    """The sample rate of the audio track."""


# --- restJson1 ser/de ---
def serialize_json(value: AudioProperties) -> dict:
    out: dict = {}
    if "bit_depth" in value:
        out["bitDepth"] = value["bit_depth"]
    if "bit_rate" in value:
        out["bitRate"] = value["bit_rate"]
    if "channels" in value:
        out["channels"] = value["channels"]
    if "frame_rate" in value:
        import aws_sdk_mediaconvert.types.frame_rate

        out["frameRate"] = aws_sdk_mediaconvert.types.frame_rate.serialize_json(
            value["frame_rate"]
        )
    if "language_code" in value:
        out["languageCode"] = value["language_code"]
    if "object_count" in value:
        out["objectCount"] = value["object_count"]
    if "sample_rate" in value:
        out["sampleRate"] = value["sample_rate"]
    return out


def deserialize_json(data: dict) -> AudioProperties:
    out: AudioProperties = {}  # type: ignore[typeddict-item]
    if "bitDepth" in data:
        out["bit_depth"] = data["bitDepth"]
    if "bitRate" in data:
        out["bit_rate"] = data["bitRate"]
    if "channels" in data:
        out["channels"] = data["channels"]
    if "frameRate" in data:
        import aws_sdk_mediaconvert.types.frame_rate

        out["frame_rate"] = aws_sdk_mediaconvert.types.frame_rate.deserialize_json(
            data["frameRate"]
        )
    if "languageCode" in data:
        out["language_code"] = data["languageCode"]
    if "objectCount" in data:
        out["object_count"] = data["objectCount"]
    if "sampleRate" in data:
        out["sample_rate"] = data["sampleRate"]
    return out
