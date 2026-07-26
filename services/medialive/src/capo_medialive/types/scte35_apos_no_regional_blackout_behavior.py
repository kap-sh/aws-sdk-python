"""Generated from Smithy shape ``com.amazonaws.medialive#Scte35AposNoRegionalBlackoutBehavior``."""

from typing import Literal, TypeAlias, cast

"""Scte35 Apos No Regional Blackout Behavior"""
Scte35AposNoRegionalBlackoutBehavior: TypeAlias = Literal[
    "FOLLOW",
    "IGNORE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Scte35AposNoRegionalBlackoutBehavior) -> str:
    return value


def deserialize_json(data: str) -> Scte35AposNoRegionalBlackoutBehavior:
    return cast(Scte35AposNoRegionalBlackoutBehavior, data)
