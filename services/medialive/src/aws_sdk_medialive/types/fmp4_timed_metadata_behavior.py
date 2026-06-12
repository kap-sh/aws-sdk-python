"""Generated from Smithy shape ``com.amazonaws.medialive#Fmp4TimedMetadataBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Fmp4 Timed Metadata Behavior"""
Fmp4TimedMetadataBehavior: TypeAlias = Literal[
    "NO_PASSTHROUGH",
    "PASSTHROUGH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_PASSTHROUGH",
        "PASSTHROUGH",
    )
)


def serialize_json(value: Fmp4TimedMetadataBehavior) -> str:
    return value


def deserialize_json(data: str) -> Fmp4TimedMetadataBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Fmp4TimedMetadataBehavior value: {data!r}")
    return cast(Fmp4TimedMetadataBehavior, data)
