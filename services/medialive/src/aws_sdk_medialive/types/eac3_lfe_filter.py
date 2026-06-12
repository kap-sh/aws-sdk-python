"""Generated from Smithy shape ``com.amazonaws.medialive#Eac3LfeFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Eac3 Lfe Filter"""
Eac3LfeFilter: TypeAlias = Literal[
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


def serialize_json(value: Eac3LfeFilter) -> str:
    return value


def deserialize_json(data: str) -> Eac3LfeFilter:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Eac3LfeFilter value: {data!r}")
    return cast(Eac3LfeFilter, data)
