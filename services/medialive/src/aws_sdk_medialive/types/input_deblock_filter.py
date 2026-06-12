"""Generated from Smithy shape ``com.amazonaws.medialive#InputDeblockFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Input Deblock Filter"""
InputDeblockFilter: TypeAlias = Literal[
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


def serialize_json(value: InputDeblockFilter) -> str:
    return value


def deserialize_json(data: str) -> InputDeblockFilter:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputDeblockFilter value: {data!r}")
    return cast(InputDeblockFilter, data)
