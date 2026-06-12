"""Generated from Smithy shape ``com.amazonaws.mediaconvert#NoiseReducerFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Use Noise reducer filter to select one of the following spatial image filtering functions. To use this setting, you must also enable Noise reducer. * Bilateral preserves edges while reducing noise. * Mean (softest), Gaussian, Lanczos, and Sharpen (sharpest) do convolution filtering. * Conserve does min/max noise reduction. * Spatial does frequency-domain filtering based on JND principles. * Temporal optimizes video quality for complex motion."""
NoiseReducerFilter: TypeAlias = Literal[
    "BILATERAL",
    "MEAN",
    "GAUSSIAN",
    "LANCZOS",
    "SHARPEN",
    "CONSERVE",
    "SPATIAL",
    "TEMPORAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BILATERAL",
        "MEAN",
        "GAUSSIAN",
        "LANCZOS",
        "SHARPEN",
        "CONSERVE",
        "SPATIAL",
        "TEMPORAL",
    )
)


def serialize_json(value: NoiseReducerFilter) -> str:
    return value


def deserialize_json(data: str) -> NoiseReducerFilter:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NoiseReducerFilter value: {data!r}")
    return cast(NoiseReducerFilter, data)
