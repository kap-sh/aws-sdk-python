"""Generated from Smithy shape ``com.amazonaws.medialive#Scte35AposWebDeliveryAllowedBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Scte35 Apos Web Delivery Allowed Behavior"""
Scte35AposWebDeliveryAllowedBehavior: TypeAlias = Literal[
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


def serialize_json(value: Scte35AposWebDeliveryAllowedBehavior) -> str:
    return value


def deserialize_json(data: str) -> Scte35AposWebDeliveryAllowedBehavior:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown Scte35AposWebDeliveryAllowedBehavior value: {data!r}"
        )
    return cast(Scte35AposWebDeliveryAllowedBehavior, data)
