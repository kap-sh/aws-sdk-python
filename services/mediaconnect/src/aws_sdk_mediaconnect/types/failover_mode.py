"""Generated from Smithy shape ``com.amazonaws.mediaconnect#FailoverMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

FailoverMode: TypeAlias = Literal[
    "MERGE",
    "FAILOVER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MERGE",
        "FAILOVER",
    )
)


def serialize_json(value: FailoverMode) -> str:
    return value


def deserialize_json(data: str) -> FailoverMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FailoverMode value: {data!r}")
    return cast(FailoverMode, data)
