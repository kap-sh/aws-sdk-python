"""Generated from Smithy shape ``com.amazonaws.kafka#ClusterState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kafka.errors import DeserializationError

"""<p>The state of the Apache Kafka cluster.</p>"""
ClusterState: TypeAlias = Literal[
    "ACTIVE",
    "CREATING",
    "DELETING",
    "FAILED",
    "HEALING",
    "MAINTENANCE",
    "REBOOTING_BROKER",
    "UPDATING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "CREATING",
        "DELETING",
        "FAILED",
        "HEALING",
        "MAINTENANCE",
        "REBOOTING_BROKER",
        "UPDATING",
    )
)


def serialize_json(value: ClusterState) -> str:
    return value


def deserialize_json(data: str) -> ClusterState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterState value: {data!r}")
    return cast(ClusterState, data)
