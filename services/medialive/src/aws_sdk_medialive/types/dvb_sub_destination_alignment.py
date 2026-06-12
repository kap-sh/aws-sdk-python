"""Generated from Smithy shape ``com.amazonaws.medialive#DvbSubDestinationAlignment``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Dvb Sub Destination Alignment"""
DvbSubDestinationAlignment: TypeAlias = Literal[
    "CENTERED",
    "LEFT",
    "SMART",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CENTERED",
        "LEFT",
        "SMART",
    )
)


def serialize_json(value: DvbSubDestinationAlignment) -> str:
    return value


def deserialize_json(data: str) -> DvbSubDestinationAlignment:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DvbSubDestinationAlignment value: {data!r}"
        )
    return cast(DvbSubDestinationAlignment, data)
