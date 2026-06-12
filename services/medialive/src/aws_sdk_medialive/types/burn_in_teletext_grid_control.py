"""Generated from Smithy shape ``com.amazonaws.medialive#BurnInTeletextGridControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Burn In Teletext Grid Control"""
BurnInTeletextGridControl: TypeAlias = Literal[
    "FIXED",
    "SCALED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FIXED",
        "SCALED",
    )
)


def serialize_json(value: BurnInTeletextGridControl) -> str:
    return value


def deserialize_json(data: str) -> BurnInTeletextGridControl:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BurnInTeletextGridControl value: {data!r}")
    return cast(BurnInTeletextGridControl, data)
