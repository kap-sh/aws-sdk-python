"""Generated from Smithy shape ``com.amazonaws.medialive#DvbSubDestinationTeletextGridControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Dvb Sub Destination Teletext Grid Control"""
DvbSubDestinationTeletextGridControl: TypeAlias = Literal[
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


def serialize_json(value: DvbSubDestinationTeletextGridControl) -> str:
    return value


def deserialize_json(data: str) -> DvbSubDestinationTeletextGridControl:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DvbSubDestinationTeletextGridControl value: {data!r}"
        )
    return cast(DvbSubDestinationTeletextGridControl, data)
