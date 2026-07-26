"""Generated from Smithy shape ``com.amazonaws.kafka#ClusterState``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: ClusterState) -> str:
    return value


def deserialize_json(data: str) -> ClusterState:
    return cast(ClusterState, data)
