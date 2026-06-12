"""Generated from Smithy shape ``com.amazonaws.medialive#HlsIncompleteSegmentBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Hls Incomplete Segment Behavior"""
HlsIncompleteSegmentBehavior: TypeAlias = Literal[
    "AUTO",
    "SUPPRESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO",
        "SUPPRESS",
    )
)


def serialize_json(value: HlsIncompleteSegmentBehavior) -> str:
    return value


def deserialize_json(data: str) -> HlsIncompleteSegmentBehavior:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown HlsIncompleteSegmentBehavior value: {data!r}"
        )
    return cast(HlsIncompleteSegmentBehavior, data)
