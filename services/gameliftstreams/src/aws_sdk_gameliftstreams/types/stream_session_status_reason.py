"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#StreamSessionStatusReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gameliftstreams.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: StreamSessionStatusReason) -> str:
    return value


def deserialize_json(data: str) -> StreamSessionStatusReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StreamSessionStatusReason value: {data!r}")
    return cast(StreamSessionStatusReason, data)
