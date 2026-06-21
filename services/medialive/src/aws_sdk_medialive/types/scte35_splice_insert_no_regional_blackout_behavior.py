"""Generated from Smithy shape ``com.amazonaws.medialive#Scte35SpliceInsertNoRegionalBlackoutBehavior``."""

from typing import Literal, TypeAlias, cast

"""Scte35 Splice Insert No Regional Blackout Behavior"""
Scte35SpliceInsertNoRegionalBlackoutBehavior: TypeAlias = Literal[
    "FOLLOW",
    "IGNORE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Scte35SpliceInsertNoRegionalBlackoutBehavior) -> str:
    return value


def deserialize_json(data: str) -> Scte35SpliceInsertNoRegionalBlackoutBehavior:
    return cast(Scte35SpliceInsertNoRegionalBlackoutBehavior, data)
