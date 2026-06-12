"""Generated from Smithy shape ``com.amazonaws.medialive#AacProfile``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Aac Profile"""
AacProfile: TypeAlias = Literal[
    "HEV1",
    "HEV2",
    "LC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HEV1",
        "HEV2",
        "LC",
    )
)


def serialize_json(value: AacProfile) -> str:
    return value


def deserialize_json(data: str) -> AacProfile:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AacProfile value: {data!r}")
    return cast(AacProfile, data)
