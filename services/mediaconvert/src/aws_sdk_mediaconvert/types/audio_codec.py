"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AudioCodec``."""

from typing import Literal, TypeAlias, cast

"""Choose the audio codec for this output. Note that the option Dolby Digital passthrough applies only to Dolby Digital and Dolby Digital Plus audio inputs. Make sure that you choose a codec that's supported with your output container: https://docs.aws.amazon.com/mediaconvert/latest/ug/reference-codecs-containers.html#reference-codecs-containers-output-audio For audio-only outputs, make sure that both your input audio codec and your output audio codec are supported for audio-only workflows. For more information, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/reference-codecs-containers-input.html#reference-codecs-containers-input-audio-only and https://docs.aws.amazon.com/mediaconvert/latest/ug/reference-codecs-containers.html#audio-only-output"""
AudioCodec: TypeAlias = Literal[
    "AAC",
    "MP2",
    "MP3",
    "WAV",
    "AIFF",
    "AC3",
    "AC4",
    "EAC3",
    "EAC3_ATMOS",
    "VORBIS",
    "OPUS",
    "PASSTHROUGH",
    "FLAC",
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioCodec) -> str:
    return value


def deserialize_json(data: str) -> AudioCodec:
    return cast(AudioCodec, data)
