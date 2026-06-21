"""Generated from Smithy shape ``com.amazonaws.networkmanager#SegmentActionServiceInsertion``."""

from typing import Literal, TypeAlias, cast

SegmentActionServiceInsertion: TypeAlias = Literal[
    "send-via",
    "send-to",
]


# --- restJson1 ser/de ---
def serialize_json(value: SegmentActionServiceInsertion) -> str:
    return value


def deserialize_json(data: str) -> SegmentActionServiceInsertion:
    return cast(SegmentActionServiceInsertion, data)
