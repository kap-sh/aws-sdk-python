"""Generated from Smithy shape ``com.amazonaws.medialive#RtmpCacheFullBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Rtmp Cache Full Behavior"""
RtmpCacheFullBehavior: TypeAlias = Literal[
    "DISCONNECT_IMMEDIATELY",
    "WAIT_FOR_SERVER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISCONNECT_IMMEDIATELY",
        "WAIT_FOR_SERVER",
    )
)


def serialize_json(value: RtmpCacheFullBehavior) -> str:
    return value


def deserialize_json(data: str) -> RtmpCacheFullBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RtmpCacheFullBehavior value: {data!r}")
    return cast(RtmpCacheFullBehavior, data)
