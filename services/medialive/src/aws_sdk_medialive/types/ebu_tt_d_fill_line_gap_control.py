"""Generated from Smithy shape ``com.amazonaws.medialive#EbuTtDFillLineGapControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Ebu Tt DFill Line Gap Control"""
EbuTtDFillLineGapControl: TypeAlias = Literal[
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


def serialize_json(value: EbuTtDFillLineGapControl) -> str:
    return value


def deserialize_json(data: str) -> EbuTtDFillLineGapControl:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EbuTtDFillLineGapControl value: {data!r}")
    return cast(EbuTtDFillLineGapControl, data)
