"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ProresChromaSampling``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""This setting applies only to ProRes 4444 and ProRes 4444 XQ outputs that you create from inputs that use 4:4:4 chroma sampling. Set Preserve 4:4:4 sampling to allow outputs to also use 4:4:4 chroma sampling. You must specify a value for this setting when your output codec profile supports 4:4:4 chroma sampling. Related Settings: For Apple ProRes outputs with 4:4:4 chroma sampling: Choose Preserve 4:4:4 sampling. Use when your input has 4:4:4 chroma sampling and your output codec Profile is Apple ProRes 4444 or 4444 XQ. Note that when you choose Preserve 4:4:4 sampling, you cannot include any of the following Preprocessors: Dolby Vision, HDR10+, or Noise reducer."""
ProresChromaSampling: TypeAlias = Literal[
    "PRESERVE_444_SAMPLING",
    "SUBSAMPLE_TO_422",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRESERVE_444_SAMPLING",
        "SUBSAMPLE_TO_422",
    )
)


def serialize_json(value: ProresChromaSampling) -> str:
    return value


def deserialize_json(data: str) -> ProresChromaSampling:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProresChromaSampling value: {data!r}")
    return cast(ProresChromaSampling, data)
