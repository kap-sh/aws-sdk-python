"""Generated from Smithy shape ``com.amazonaws.medialive#RtmpCacheFullBehavior``."""

from typing import Literal, TypeAlias, cast

"""Rtmp Cache Full Behavior"""
RtmpCacheFullBehavior: TypeAlias = Literal[
    "DISCONNECT_IMMEDIATELY",
    "WAIT_FOR_SERVER",
]


# --- restJson1 ser/de ---
def serialize_json(value: RtmpCacheFullBehavior) -> str:
    return value


def deserialize_json(data: str) -> RtmpCacheFullBehavior:
    return cast(RtmpCacheFullBehavior, data)
