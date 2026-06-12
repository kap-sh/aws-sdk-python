"""Generated from Smithy shape ``com.amazonaws.medialive#Algorithm``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Placeholder documentation for Algorithm"""
Algorithm: TypeAlias = Literal[
    "AES128",
    "AES192",
    "AES256",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AES128",
        "AES192",
        "AES256",
    )
)


def serialize_json(value: Algorithm) -> str:
    return value


def deserialize_json(data: str) -> Algorithm:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Algorithm value: {data!r}")
    return cast(Algorithm, data)
