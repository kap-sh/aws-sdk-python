"""Generated from Smithy shape ``com.amazonaws.medialive#EbuTtDDestinationStyleControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Ebu Tt DDestination Style Control"""
EbuTtDDestinationStyleControl: TypeAlias = Literal[
    "EXCLUDE",
    "INCLUDE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EXCLUDE",
        "INCLUDE",
    )
)


def serialize_json(value: EbuTtDDestinationStyleControl) -> str:
    return value


def deserialize_json(data: str) -> EbuTtDDestinationStyleControl:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EbuTtDDestinationStyleControl value: {data!r}"
        )
    return cast(EbuTtDDestinationStyleControl, data)
