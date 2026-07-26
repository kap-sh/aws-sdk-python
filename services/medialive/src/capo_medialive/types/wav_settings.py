"""Generated from Smithy shape ``com.amazonaws.medialive#WavSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__double
    import capo_medialive.types.wav_coding_mode


class WavSettings(TypedDict, closed=True):
    bit_depth: NotRequired["capo_medialive.types.__double.__double"]
    """Bits per sample."""
    coding_mode: NotRequired["capo_medialive.types.wav_coding_mode.WavCodingMode"]
    """The audio coding mode for the WAV audio. The mode determines the number of channels in the audio."""
    sample_rate: NotRequired["capo_medialive.types.__double.__double"]
    """Sample rate in Hz."""


# --- restJson1 ser/de ---
def serialize_json(value: WavSettings) -> dict:
    out: dict = {}
    if "bit_depth" in value:
        out["bitDepth"] = value["bit_depth"]
    if "coding_mode" in value:
        import capo_medialive.types.wav_coding_mode

        out["codingMode"] = capo_medialive.types.wav_coding_mode.serialize_json(
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
        import capo_medialive.types.wav_coding_mode

        out["coding_mode"] = capo_medialive.types.wav_coding_mode.deserialize_json(
            data["codingMode"]
        )
    if "sampleRate" in data:
        out["sample_rate"] = data["sampleRate"]
    return out
