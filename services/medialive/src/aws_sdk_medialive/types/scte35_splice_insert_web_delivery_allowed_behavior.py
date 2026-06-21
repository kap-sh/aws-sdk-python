"""Generated from Smithy shape ``com.amazonaws.medialive#Scte35SpliceInsertWebDeliveryAllowedBehavior``."""

from typing import Literal, TypeAlias, cast

"""Scte35 Splice Insert Web Delivery Allowed Behavior"""
Scte35SpliceInsertWebDeliveryAllowedBehavior: TypeAlias = Literal[
    "FOLLOW",
    "IGNORE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Scte35SpliceInsertWebDeliveryAllowedBehavior) -> str:
    return value


def deserialize_json(data: str) -> Scte35SpliceInsertWebDeliveryAllowedBehavior:
    return cast(Scte35SpliceInsertWebDeliveryAllowedBehavior, data)
