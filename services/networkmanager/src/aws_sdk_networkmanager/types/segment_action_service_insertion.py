"""Generated from Smithy shape ``com.amazonaws.networkmanager#SegmentActionServiceInsertion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

SegmentActionServiceInsertion: TypeAlias = Literal[
    "send-via",
    "send-to",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "send-via",
        "send-to",
    )
)


def serialize_json(value: SegmentActionServiceInsertion) -> str:
    return value


def deserialize_json(data: str) -> SegmentActionServiceInsertion:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SegmentActionServiceInsertion value: {data!r}"
        )
    return cast(SegmentActionServiceInsertion, data)
