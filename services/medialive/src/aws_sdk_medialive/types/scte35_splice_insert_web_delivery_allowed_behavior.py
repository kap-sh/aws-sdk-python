"""Generated from Smithy shape ``com.amazonaws.medialive#Scte35SpliceInsertWebDeliveryAllowedBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Scte35 Splice Insert Web Delivery Allowed Behavior"""
Scte35SpliceInsertWebDeliveryAllowedBehavior: TypeAlias = Literal[
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


def serialize_json(value: Scte35SpliceInsertWebDeliveryAllowedBehavior) -> str:
    return value


def deserialize_json(data: str) -> Scte35SpliceInsertWebDeliveryAllowedBehavior:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown Scte35SpliceInsertWebDeliveryAllowedBehavior value: {data!r}"
        )
    return cast(Scte35SpliceInsertWebDeliveryAllowedBehavior, data)
