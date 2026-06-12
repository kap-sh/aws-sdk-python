"""Generated from Smithy shape ``com.amazonaws.medialive#Ac3LfeFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Ac3 Lfe Filter"""
Ac3LfeFilter: TypeAlias = Literal[
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


def serialize_json(value: Ac3LfeFilter) -> str:
    return value


def deserialize_json(data: str) -> Ac3LfeFilter:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Ac3LfeFilter value: {data!r}")
    return cast(Ac3LfeFilter, data)
