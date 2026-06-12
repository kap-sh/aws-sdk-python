"""Generated from Smithy shape ``com.amazonaws.mediaconvert#UncompressedFourcc``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""The four character code for the uncompressed video."""
UncompressedFourcc: TypeAlias = Literal[
    "I420",
    "I422",
    "I444",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "I420",
        "I422",
        "I444",
    )
)


def serialize_json(value: UncompressedFourcc) -> str:
    return value


def deserialize_json(data: str) -> UncompressedFourcc:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UncompressedFourcc value: {data!r}")
    return cast(UncompressedFourcc, data)
