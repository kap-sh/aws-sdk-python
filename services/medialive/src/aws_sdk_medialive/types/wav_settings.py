"""Generated from Smithy shape ``com.amazonaws.medialive#WavSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__double
    import aws_sdk_medialive.types.wav_coding_mode


class WavSettings(TypedDict):
    bit_depth: NotRequired["aws_sdk_medialive.types.__double.__double"]
    """Bits per sample."""
    coding_mode: NotRequired["aws_sdk_medialive.types.wav_coding_mode.WavCodingMode"]
    """The audio coding mode for the WAV audio. The mode determines the number of channels in the audio."""
    sample_rate: NotRequired["aws_sdk_medialive.types.__double.__double"]
    """Sample rate in Hz."""


# --- restJson1 ser/de ---
def serialize_json(value: WavSettings) -> dict:
    out: dict = {}
    if "bit_depth" in value:
        out["bitDepth"] = value["bit_depth"]
    if "coding_mode" in value:
        import aws_sdk_medialive.types.wav_coding_mode

        out["codingMode"] = aws_sdk_medialive.types.wav_coding_mode.serialize_json(
            value["coding_mode"]
        )
    if "sample_rate" in value:
        out["sampleRate"] = value["sample_rate"]
    return out


def deserialize_json(data: dict) -> WavSettings:
    out: WavSettings = {}  # type: ignore[typeddict-item]
    if "bitDepth" in data:
        out["bit_depth"] = data["bitDepth"]
    if "codingMode" in data:
        import aws_sdk_medialive.types.wav_coding_mode

        out["coding_mode"] = aws_sdk_medialive.types.wav_coding_mode.deserialize_json(
            data["codingMode"]
        )
    if "sampleRate" in data:
        out["sample_rate"] = data["sampleRate"]
    return out
