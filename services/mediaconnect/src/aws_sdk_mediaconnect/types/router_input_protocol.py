"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

RouterInputProtocol: TypeAlias = Literal[
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


def serialize_json(value: RouterInputProtocol) -> str:
    return value


def deserialize_json(data: str) -> RouterInputProtocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouterInputProtocol value: {data!r}")
    return cast(RouterInputProtocol, data)
