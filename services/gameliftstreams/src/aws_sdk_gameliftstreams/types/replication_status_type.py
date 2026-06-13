"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#ReplicationStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gameliftstreams.errors import DeserializationError

ReplicationStatusType: TypeAlias = Literal[
    "REPLICATING",
    "COMPLETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REPLICATING",
        "COMPLETED",
    )
)


def serialize_json(value: ReplicationStatusType) -> str:
    return value


def deserialize_json(data: str) -> ReplicationStatusType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReplicationStatusType value: {data!r}")
    return cast(ReplicationStatusType, data)
