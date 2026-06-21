"""Generated from Smithy shape ``com.amazonaws.medialive#Scte35AposWebDeliveryAllowedBehavior``."""

from typing import Literal, TypeAlias, cast

"""Scte35 Apos Web Delivery Allowed Behavior"""
Scte35AposWebDeliveryAllowedBehavior: TypeAlias = Literal[
    "FOLLOW",
    "IGNORE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Scte35AposWebDeliveryAllowedBehavior) -> str:
    return value


def deserialize_json(data: str) -> Scte35AposWebDeliveryAllowedBehavior:
    return cast(Scte35AposWebDeliveryAllowedBehavior, data)
