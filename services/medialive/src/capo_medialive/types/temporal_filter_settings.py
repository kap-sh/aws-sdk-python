"""Generated from Smithy shape ``com.amazonaws.medialive#TemporalFilterSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.temporal_filter_post_filter_sharpening
    import capo_medialive.types.temporal_filter_strength


class TemporalFilterSettings(TypedDict, closed=True):
    post_filter_sharpening: NotRequired[
        "capo_medialive.types.temporal_filter_post_filter_sharpening.TemporalFilterPostFilterSharpening"
    ]
    """If you enable this filter, the results are the following: - If the source content is noisy (it contains excessive digital artifacts), the filter cleans up the source. - If the source content is already clean, the filter tends to decrease the bitrate, especially when the rate control mode is QVBR."""
    strength: NotRequired[
        "capo_medialive.types.temporal_filter_strength.TemporalFilterStrength"
    ]
    """Choose a filter strength. We recommend a strength of 1 or 2. A higher strength might take out good information, resulting in an image that is overly soft."""


# --- restJson1 ser/de ---
def serialize_json(value: TemporalFilterSettings) -> dict:
    out: dict = {}
    if "post_filter_sharpening" in value:
        import capo_medialive.types.temporal_filter_post_filter_sharpening

        out["postFilterSharpening"] = (
            capo_medialive.types.temporal_filter_post_filter_sharpening.serialize_json(
                value["post_filter_sharpening"]
            )
        )
    if "strength" in value:
        import capo_medialive.types.temporal_filter_strength

        out["strength"] = capo_medialive.types.temporal_filter_strength.serialize_json(
            value["strength"]
        )
    return out


def deserialize_json(data: dict) -> TemporalFilterSettings:
    out: TemporalFilterSettings = {}  # type: ignore[typeddict-item]
    if "postFilterSharpening" in data:
        import capo_medialive.types.temporal_filter_post_filter_sharpening

        out["post_filter_sharpening"] = (
            capo_medialive.types.temporal_filter_post_filter_sharpening.deserialize_json(
                data["postFilterSharpening"]
            )
        )
    if "strength" in data:
        import capo_medialive.types.temporal_filter_strength

        out["strength"] = (
            capo_medialive.types.temporal_filter_strength.deserialize_json(
                data["strength"]
            )
        )
    return out
