"""Generated from Smithy shape ``com.amazonaws.medialive#WebvttDestinationStyleControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Webvtt Destination Style Control"""
WebvttDestinationStyleControl: TypeAlias = Literal[
    "NO_STYLE_DATA",
    "PASSTHROUGH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_STYLE_DATA",
        "PASSTHROUGH",
    )
)


def serialize_json(value: WebvttDestinationStyleControl) -> str:
    return value


def deserialize_json(data: str) -> WebvttDestinationStyleControl:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown WebvttDestinationStyleControl value: {data!r}"
        )
    return cast(WebvttDestinationStyleControl, data)
