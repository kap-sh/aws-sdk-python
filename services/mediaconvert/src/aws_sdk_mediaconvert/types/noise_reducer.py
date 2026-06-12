"""Generated from Smithy shape ``com.amazonaws.mediaconvert#NoiseReducer``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.noise_reducer_filter
    import aws_sdk_mediaconvert.types.noise_reducer_filter_settings
    import aws_sdk_mediaconvert.types.noise_reducer_spatial_filter_settings
    import aws_sdk_mediaconvert.types.noise_reducer_temporal_filter_settings


class NoiseReducer(TypedDict):
    filter: NotRequired[
        "aws_sdk_mediaconvert.types.noise_reducer_filter.NoiseReducerFilter"
    ]
    """Use Noise reducer filter to select one of the following spatial image filtering functions. To use this setting, you must also enable Noise reducer. * Bilateral preserves edges while reducing noise. * Mean (softest), Gaussian, Lanczos, and Sharpen (sharpest) do convolution filtering. * Conserve does min/max noise reduction. * Spatial does frequency-domain filtering based on JND principles. * Temporal optimizes video quality for complex motion."""
    filter_settings: NotRequired[
        "aws_sdk_mediaconvert.types.noise_reducer_filter_settings.NoiseReducerFilterSettings"
    ]
    """Settings for a noise reducer filter"""
    spatial_filter_settings: NotRequired[
        "aws_sdk_mediaconvert.types.noise_reducer_spatial_filter_settings.NoiseReducerSpatialFilterSettings"
    ]
    """Noise reducer filter settings for spatial filter."""
    temporal_filter_settings: NotRequired[
        "aws_sdk_mediaconvert.types.noise_reducer_temporal_filter_settings.NoiseReducerTemporalFilterSettings"
    ]
    """Noise reducer filter settings for temporal filter."""


# --- restJson1 ser/de ---
def serialize_json(value: NoiseReducer) -> dict:
    out: dict = {}
    if "filter" in value:
        import aws_sdk_mediaconvert.types.noise_reducer_filter

        out["filter"] = aws_sdk_mediaconvert.types.noise_reducer_filter.serialize_json(
            value["filter"]
        )
    if "filter_settings" in value:
        import aws_sdk_mediaconvert.types.noise_reducer_filter_settings

        out["filterSettings"] = (
            aws_sdk_mediaconvert.types.noise_reducer_filter_settings.serialize_json(
                value["filter_settings"]
            )
        )
    if "spatial_filter_settings" in value:
        import aws_sdk_mediaconvert.types.noise_reducer_spatial_filter_settings

        out["spatialFilterSettings"] = (
            aws_sdk_mediaconvert.types.noise_reducer_spatial_filter_settings.serialize_json(
                value["spatial_filter_settings"]
            )
        )
    if "temporal_filter_settings" in value:
        import aws_sdk_mediaconvert.types.noise_reducer_temporal_filter_settings

        out["temporalFilterSettings"] = (
            aws_sdk_mediaconvert.types.noise_reducer_temporal_filter_settings.serialize_json(
                value["temporal_filter_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> NoiseReducer:
    out: NoiseReducer = {}  # type: ignore[typeddict-item]
    if "filter" in data:
        import aws_sdk_mediaconvert.types.noise_reducer_filter

        out["filter"] = (
            aws_sdk_mediaconvert.types.noise_reducer_filter.deserialize_json(
                data["filter"]
            )
        )
    if "filterSettings" in data:
        import aws_sdk_mediaconvert.types.noise_reducer_filter_settings

        out["filter_settings"] = (
            aws_sdk_mediaconvert.types.noise_reducer_filter_settings.deserialize_json(
                data["filterSettings"]
            )
        )
    if "spatialFilterSettings" in data:
        import aws_sdk_mediaconvert.types.noise_reducer_spatial_filter_settings

        out["spatial_filter_settings"] = (
            aws_sdk_mediaconvert.types.noise_reducer_spatial_filter_settings.deserialize_json(
                data["spatialFilterSettings"]
            )
        )
    if "temporalFilterSettings" in data:
        import aws_sdk_mediaconvert.types.noise_reducer_temporal_filter_settings

        out["temporal_filter_settings"] = (
            aws_sdk_mediaconvert.types.noise_reducer_temporal_filter_settings.deserialize_json(
                data["temporalFilterSettings"]
            )
        )
    return out
