"""Generated from Smithy shape ``com.amazonaws.medialive#AacSpec``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Aac Spec"""
AacSpec: TypeAlias = Literal[
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


def serialize_json(value: AacSpec) -> str:
    return value


def deserialize_json(data: str) -> AacSpec:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AacSpec value: {data!r}")
    return cast(AacSpec, data)
