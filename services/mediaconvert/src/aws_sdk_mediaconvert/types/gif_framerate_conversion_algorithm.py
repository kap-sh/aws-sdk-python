"""Generated from Smithy shape ``com.amazonaws.mediaconvert#GifFramerateConversionAlgorithm``."""

from typing import Literal, TypeAlias, cast

"""Optional. Specify how the transcoder performs framerate conversion. The default behavior is to use Drop duplicate (DUPLICATE_DROP) conversion. When you choose Interpolate (INTERPOLATE) instead, the conversion produces smoother motion."""
GifFramerateConversionAlgorithm: TypeAlias = Literal[
    "DUPLICATE_DROP",
    "INTERPOLATE",
]


# --- restJson1 ser/de ---
def serialize_json(value: GifFramerateConversionAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> GifFramerateConversionAlgorithm:
    return cast(GifFramerateConversionAlgorithm, data)
