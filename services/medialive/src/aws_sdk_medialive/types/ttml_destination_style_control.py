"""Generated from Smithy shape ``com.amazonaws.medialive#TtmlDestinationStyleControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Ttml Destination Style Control"""
TtmlDestinationStyleControl: TypeAlias = Literal[
    "PASSTHROUGH",
    "USE_CONFIGURED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PASSTHROUGH",
        "USE_CONFIGURED",
    )
)


def serialize_json(value: TtmlDestinationStyleControl) -> str:
    return value


def deserialize_json(data: str) -> TtmlDestinationStyleControl:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TtmlDestinationStyleControl value: {data!r}"
        )
    return cast(TtmlDestinationStyleControl, data)
