"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#StreamSessionStatusReason``."""

from typing import Literal, TypeAlias, cast

StreamSessionStatusReason: TypeAlias = Literal[
    "internalError",
    "invalidSignalRequest",
    "placementTimeout",
    "applicationLogS3DestinationError",
    "applicationExit",
    "connectionTimeout",
    "reconnectionTimeout",
    "maxSessionLengthTimeout",
    "idleTimeout",
    "apiTerminated",
]


# --- restJson1 ser/de ---
def serialize_json(value: StreamSessionStatusReason) -> str:
    return value


def deserialize_json(data: str) -> StreamSessionStatusReason:
    return cast(StreamSessionStatusReason, data)
