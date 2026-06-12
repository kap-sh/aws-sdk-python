"""Generated from Smithy shape ``com.amazonaws.mediaconvert#NielsenSourceWatermarkStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Required. Specify whether your source content already contains Nielsen non-linear watermarks. When you set this value to Watermarked, the service fails the job. Nielsen requires that you add non-linear watermarking to only clean content that doesn't already have non-linear Nielsen watermarks."""
NielsenSourceWatermarkStatusType: TypeAlias = Literal[
    "CLEAN",
    "WATERMARKED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLEAN",
        "WATERMARKED",
    )
)


def serialize_json(value: NielsenSourceWatermarkStatusType) -> str:
    return value


def deserialize_json(data: str) -> NielsenSourceWatermarkStatusType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown NielsenSourceWatermarkStatusType value: {data!r}"
        )
    return cast(NielsenSourceWatermarkStatusType, data)
