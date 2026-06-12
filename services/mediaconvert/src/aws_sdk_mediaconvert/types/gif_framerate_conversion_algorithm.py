"""Generated from Smithy shape ``com.amazonaws.mediaconvert#GifFramerateConversionAlgorithm``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Optional. Specify how the transcoder performs framerate conversion. The default behavior is to use Drop duplicate (DUPLICATE_DROP) conversion. When you choose Interpolate (INTERPOLATE) instead, the conversion produces smoother motion."""
GifFramerateConversionAlgorithm: TypeAlias = Literal[
    "DUPLICATE_DROP",
    "INTERPOLATE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DUPLICATE_DROP",
        "INTERPOLATE",
    )
)


def serialize_json(value: GifFramerateConversionAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> GifFramerateConversionAlgorithm:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GifFramerateConversionAlgorithm value: {data!r}"
        )
    return cast(GifFramerateConversionAlgorithm, data)
