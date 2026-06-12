"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AacSpecification``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Use MPEG-2 AAC instead of MPEG-4 AAC audio for raw or MPEG-2 Transport Stream containers."""
AacSpecification: TypeAlias = Literal[
    "MPEG2",
    "MPEG4",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MPEG2",
        "MPEG4",
    )
)


def serialize_json(value: AacSpecification) -> str:
    return value


def deserialize_json(data: str) -> AacSpecification:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AacSpecification value: {data!r}")
    return cast(AacSpecification, data)
