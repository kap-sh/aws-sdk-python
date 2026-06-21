"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterOutputProtocol``."""

from typing import Literal, TypeAlias, cast

RouterOutputProtocol: TypeAlias = Literal[
    "RTP",
    "RIST",
    "SRT_CALLER",
    "SRT_LISTENER",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouterOutputProtocol) -> str:
    return value


def deserialize_json(data: str) -> RouterOutputProtocol:
    return cast(RouterOutputProtocol, data)
