"""Generated from Smithy shape ``com.amazonaws.kafka#ReplicatorState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kafka.errors import DeserializationError

"""<p>The state of a replicator.</p>"""
ReplicatorState: TypeAlias = Literal[
    "RUNNING",
    "CREATING",
    "UPDATING",
    "DELETING",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "CREATING",
        "UPDATING",
        "DELETING",
        "FAILED",
    )
)


def serialize_json(value: ReplicatorState) -> str:
    return value


def deserialize_json(data: str) -> ReplicatorState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReplicatorState value: {data!r}")
    return cast(ReplicatorState, data)
