"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AvcIntraClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify the AVC-Intra class of your output. The AVC-Intra class selection determines the output video bit rate depending on the frame rate of the output. Outputs with higher class values have higher bitrates and improved image quality. Note that for Class 4K/2K, MediaConvert supports only 4:2:2 chroma subsampling."""
AvcIntraClass: TypeAlias = Literal[
    "CLASS_50",
    "CLASS_100",
    "CLASS_200",
    "CLASS_4K_2K",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLASS_50",
        "CLASS_100",
        "CLASS_200",
        "CLASS_4K_2K",
    )
)


def serialize_json(value: AvcIntraClass) -> str:
    return value


def deserialize_json(data: str) -> AvcIntraClass:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AvcIntraClass value: {data!r}")
    return cast(AvcIntraClass, data)
