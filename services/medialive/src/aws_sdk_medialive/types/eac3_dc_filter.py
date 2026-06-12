"""Generated from Smithy shape ``com.amazonaws.medialive#Eac3DcFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Eac3 Dc Filter"""
Eac3DcFilter: TypeAlias = Literal[
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


def serialize_json(value: Eac3DcFilter) -> str:
    return value


def deserialize_json(data: str) -> Eac3DcFilter:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Eac3DcFilter value: {data!r}")
    return cast(Eac3DcFilter, data)
