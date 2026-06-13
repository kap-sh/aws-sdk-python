"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#StreamSessionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gameliftstreams.errors import DeserializationError

StreamSessionStatus: TypeAlias = Literal[
    "ACTIVATING",
    "ACTIVE",
    "CONNECTED",
    "PENDING_CLIENT_RECONNECTION",
    "RECONNECTING",
    "TERMINATING",
    "TERMINATED",
    "ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVATING",
        "ACTIVE",
        "CONNECTED",
        "PENDING_CLIENT_RECONNECTION",
        "RECONNECTING",
        "TERMINATING",
        "TERMINATED",
        "ERROR",
    )
)


def serialize_json(value: StreamSessionStatus) -> str:
    return value


def deserialize_json(data: str) -> StreamSessionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StreamSessionStatus value: {data!r}")
    return cast(StreamSessionStatus, data)
