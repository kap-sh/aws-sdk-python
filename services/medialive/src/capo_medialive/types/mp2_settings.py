"""Generated from Smithy shape ``com.amazonaws.medialive#Mp2Settings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__double
    import capo_medialive.types.mp2_coding_mode


class Mp2Settings(TypedDict, closed=True):
    bitrate: NotRequired["capo_medialive.types.__double.__double"]
    """Average bitrate in bits/second."""
    coding_mode: NotRequired["capo_medialive.types.mp2_coding_mode.Mp2CodingMode"]
    """The MPEG2 Audio coding mode. Valid values are codingMode10 (for mono) or codingMode20 (for stereo)."""
    sample_rate: NotRequired["capo_medialive.types.__double.__double"]
    """Sample rate in Hz."""


# --- restJson1 ser/de ---
def serialize_json(value: Mp2Settings) -> dict:
    out: dict = {}
    if "bitrate" in value:
        out["bitrate"] = value["bitrate"]
    if "coding_mode" in value:
        import capo_medialive.types.mp2_coding_mode

        out["codingMode"] = capo_medialive.types.mp2_coding_mode.serialize_json(
            value["coding_mode"]
        )
    if "sample_rate" in value:
        out["sampleRate"] = value["sample_rate"]
    return out


def deserialize_json(data: dict) -> Mp2Settings:
    out: Mp2Settings = {}  # type: ignore[typeddict-item]
    if "bitrate" in data:
        out["bitrate"] = data["bitrate"]
    if "codingMode" in data:
        import capo_medialive.types.mp2_coding_mode

        out["coding_mode"] = capo_medialive.types.mp2_coding_mode.deserialize_json(
            data["codingMode"]
        )
    if "sampleRate" in data:
        out["sample_rate"] = data["sampleRate"]
    return out
