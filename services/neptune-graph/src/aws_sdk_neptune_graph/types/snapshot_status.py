"""Generated from Smithy shape ``com.amazonaws.neptunegraph#SnapshotStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_neptune_graph.errors import DeserializationError

SnapshotStatus: TypeAlias = Literal[
    "CREATING",
    "AVAILABLE",
    "DELETING",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "AVAILABLE",
        "DELETING",
        "FAILED",
    )
)


def serialize_json(value: SnapshotStatus) -> str:
    return value


def deserialize_json(data: str) -> SnapshotStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SnapshotStatus value: {data!r}")
    return cast(SnapshotStatus, data)
