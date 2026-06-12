"""Generated from Smithy shape ``com.amazonaws.medialive#AvailBlankingState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Avail Blanking State"""
AvailBlankingState: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_json(value: AvailBlankingState) -> str:
    return value


def deserialize_json(data: str) -> AvailBlankingState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AvailBlankingState value: {data!r}")
    return cast(AvailBlankingState, data)
