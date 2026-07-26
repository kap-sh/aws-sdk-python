"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AvcIntraUhdSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.avc_intra_uhd_quality_tuning_level


class AvcIntraUhdSettings(TypedDict, closed=True):
    quality_tuning_level: NotRequired[
        "capo_mediaconvert.types.avc_intra_uhd_quality_tuning_level.AvcIntraUhdQualityTuningLevel"
    ]
    """Optional. Use Quality tuning level to choose how many transcoding passes MediaConvert does with your video. When you choose Multi-pass, your video quality is better and your output bitrate is more accurate. That is, the actual bitrate of your output is closer to the target bitrate defined in the specification. When you choose Single-pass, your encoding time is faster. The default behavior is Single-pass."""


# --- restJson1 ser/de ---
def serialize_json(value: AvcIntraUhdSettings) -> dict:
    out: dict = {}
    if "quality_tuning_level" in value:
        import capo_mediaconvert.types.avc_intra_uhd_quality_tuning_level

        out["qualityTuningLevel"] = (
            capo_mediaconvert.types.avc_intra_uhd_quality_tuning_level.serialize_json(
                value["quality_tuning_level"]
            )
        )
    return out


def deserialize_json(data: dict) -> AvcIntraUhdSettings:
    out: AvcIntraUhdSettings = {}  # type: ignore[typeddict-item]
    if "qualityTuningLevel" in data:
        import capo_mediaconvert.types.avc_intra_uhd_quality_tuning_level

        out["quality_tuning_level"] = (
            capo_mediaconvert.types.avc_intra_uhd_quality_tuning_level.deserialize_json(
                data["qualityTuningLevel"]
            )
        )
    return out
