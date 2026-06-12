"""Generated from Smithy shape ``com.amazonaws.medialive#Scte35InputMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Whether the SCTE-35 input should be the active input or a fixed input."""
Scte35InputMode: TypeAlias = Literal[
    "FIXED",
    "FOLLOW_ACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FIXED",
        "FOLLOW_ACTIVE",
    )
)


def serialize_json(value: Scte35InputMode) -> str:
    return value


def deserialize_json(data: str) -> Scte35InputMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Scte35InputMode value: {data!r}")
    return cast(Scte35InputMode, data)
