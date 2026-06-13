"""Generated from Smithy shape ``com.amazonaws.neptunegraph#GraphStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_neptune_graph.errors import DeserializationError

GraphStatus: TypeAlias = Literal[
    "CREATING",
    "AVAILABLE",
    "DELETING",
    "RESETTING",
    "UPDATING",
    "SNAPSHOTTING",
    "FAILED",
    "IMPORTING",
    "STARTING",
    "STOPPING",
    "STOPPED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "AVAILABLE",
        "DELETING",
        "RESETTING",
        "UPDATING",
        "SNAPSHOTTING",
        "FAILED",
        "IMPORTING",
        "STARTING",
        "STOPPING",
        "STOPPED",
    )
)


def serialize_json(value: GraphStatus) -> str:
    return value


def deserialize_json(data: str) -> GraphStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GraphStatus value: {data!r}")
    return cast(GraphStatus, data)
