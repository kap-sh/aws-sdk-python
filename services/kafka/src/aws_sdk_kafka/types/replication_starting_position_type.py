"""Generated from Smithy shape ``com.amazonaws.kafka#ReplicationStartingPositionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kafka.errors import DeserializationError

"""<p>The type of replication starting position.</p>"""
ReplicationStartingPositionType: TypeAlias = Literal[
    "LATEST",
    "EARLIEST",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LATEST",
        "EARLIEST",
    )
)


def serialize_json(value: ReplicationStartingPositionType) -> str:
    return value


def deserialize_json(data: str) -> ReplicationStartingPositionType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ReplicationStartingPositionType value: {data!r}"
        )
    return cast(ReplicationStartingPositionType, data)
