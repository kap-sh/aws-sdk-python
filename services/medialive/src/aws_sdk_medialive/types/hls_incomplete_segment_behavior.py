"""Generated from Smithy shape ``com.amazonaws.medialive#HlsIncompleteSegmentBehavior``."""

from typing import Literal, TypeAlias, cast

"""Hls Incomplete Segment Behavior"""
HlsIncompleteSegmentBehavior: TypeAlias = Literal[
    "AUTO",
    "SUPPRESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsIncompleteSegmentBehavior) -> str:
    return value


def deserialize_json(data: str) -> HlsIncompleteSegmentBehavior:
    return cast(HlsIncompleteSegmentBehavior, data)
