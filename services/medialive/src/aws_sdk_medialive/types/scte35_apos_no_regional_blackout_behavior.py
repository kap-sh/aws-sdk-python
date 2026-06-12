"""Generated from Smithy shape ``com.amazonaws.medialive#Scte35AposNoRegionalBlackoutBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Scte35 Apos No Regional Blackout Behavior"""
Scte35AposNoRegionalBlackoutBehavior: TypeAlias = Literal[
    "FOLLOW",
    "IGNORE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FOLLOW",
        "IGNORE",
    )
)


def serialize_json(value: Scte35AposNoRegionalBlackoutBehavior) -> str:
    return value


def deserialize_json(data: str) -> Scte35AposNoRegionalBlackoutBehavior:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown Scte35AposNoRegionalBlackoutBehavior value: {data!r}"
        )
    return cast(Scte35AposNoRegionalBlackoutBehavior, data)
