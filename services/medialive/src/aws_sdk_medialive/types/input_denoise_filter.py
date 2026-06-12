"""Generated from Smithy shape ``com.amazonaws.medialive#InputDenoiseFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Input Denoise Filter"""
InputDenoiseFilter: TypeAlias = Literal[
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


def serialize_json(value: InputDenoiseFilter) -> str:
    return value


def deserialize_json(data: str) -> InputDenoiseFilter:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputDenoiseFilter value: {data!r}")
    return cast(InputDenoiseFilter, data)
