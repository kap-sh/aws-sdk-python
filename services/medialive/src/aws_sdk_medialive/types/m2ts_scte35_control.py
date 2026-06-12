"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsScte35Control``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""M2ts Scte35 Control"""
M2tsScte35Control: TypeAlias = Literal[
    "NONE",
    "PASSTHROUGH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "PASSTHROUGH",
    )
)


def serialize_json(value: M2tsScte35Control) -> str:
    return value


def deserialize_json(data: str) -> M2tsScte35Control:
    if data not in _VALUES:
        raise DeserializationError(f"unknown M2tsScte35Control value: {data!r}")
    return cast(M2tsScte35Control, data)
