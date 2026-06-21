"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#StreamSessionStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: StreamSessionStatus) -> str:
    return value


def deserialize_json(data: str) -> StreamSessionStatus:
    return cast(StreamSessionStatus, data)
