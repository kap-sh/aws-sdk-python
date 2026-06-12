"""Generated from Smithy shape ``com.amazonaws.medialive#SdiSourceMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Used in SdiSource, CreateSdiSourceRequest, UpdateSdiSourceRequest."""
SdiSourceMode: TypeAlias = Literal[
    "QUADRANT",
    "INTERLEAVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUADRANT",
        "INTERLEAVE",
    )
)


def serialize_json(value: SdiSourceMode) -> str:
    return value


def deserialize_json(data: str) -> SdiSourceMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SdiSourceMode value: {data!r}")
    return cast(SdiSourceMode, data)
