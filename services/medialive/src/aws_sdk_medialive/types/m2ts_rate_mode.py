"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsRateMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""M2ts Rate Mode"""
M2tsRateMode: TypeAlias = Literal[
    "CBR",
    "VBR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CBR",
        "VBR",
    )
)


def serialize_json(value: M2tsRateMode) -> str:
    return value


def deserialize_json(data: str) -> M2tsRateMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown M2tsRateMode value: {data!r}")
    return cast(M2tsRateMode, data)
