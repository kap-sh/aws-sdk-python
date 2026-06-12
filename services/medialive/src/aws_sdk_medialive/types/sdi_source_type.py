"""Generated from Smithy shape ``com.amazonaws.medialive#SdiSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Used in SdiSource, CreateSdiSourceRequest, UpdateSdiSourceRequest."""
SdiSourceType: TypeAlias = Literal[
    "SINGLE",
    "QUAD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SINGLE",
        "QUAD",
    )
)


def serialize_json(value: SdiSourceType) -> str:
    return value


def deserialize_json(data: str) -> SdiSourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SdiSourceType value: {data!r}")
    return cast(SdiSourceType, data)
