"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BridgePlacement``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

BridgePlacement: TypeAlias = Literal[
    "AVAILABLE",
    "LOCKED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "LOCKED",
    )
)


def serialize_json(value: BridgePlacement) -> str:
    return value


def deserialize_json(data: str) -> BridgePlacement:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BridgePlacement value: {data!r}")
    return cast(BridgePlacement, data)
