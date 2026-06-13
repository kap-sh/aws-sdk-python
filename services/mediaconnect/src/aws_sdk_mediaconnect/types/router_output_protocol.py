"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterOutputProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

RouterOutputProtocol: TypeAlias = Literal[
    "RTP",
    "RIST",
    "SRT_CALLER",
    "SRT_LISTENER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RTP",
        "RIST",
        "SRT_CALLER",
        "SRT_LISTENER",
    )
)


def serialize_json(value: RouterOutputProtocol) -> str:
    return value


def deserialize_json(data: str) -> RouterOutputProtocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouterOutputProtocol value: {data!r}")
    return cast(RouterOutputProtocol, data)
