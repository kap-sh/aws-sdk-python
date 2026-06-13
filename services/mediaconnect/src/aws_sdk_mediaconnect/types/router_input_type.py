"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

RouterInputType: TypeAlias = Literal[
    "STANDARD",
    "FAILOVER",
    "MERGE",
    "MEDIACONNECT_FLOW",
    "MEDIALIVE_CHANNEL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "FAILOVER",
        "MERGE",
        "MEDIACONNECT_FLOW",
        "MEDIALIVE_CHANNEL",
    )
)


def serialize_json(value: RouterInputType) -> str:
    return value


def deserialize_json(data: str) -> RouterInputType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouterInputType value: {data!r}")
    return cast(RouterInputType, data)
