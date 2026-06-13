"""Generated from Smithy shape ``com.amazonaws.dsql#ClusterStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dsql.errors import DeserializationError

"""<p>The current status of a cluster.</p>"""
ClusterStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "IDLE",
    "INACTIVE",
    "UPDATING",
    "DELETING",
    "DELETED",
    "FAILED",
    "PENDING_SETUP",
    "PENDING_DELETE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "IDLE",
        "INACTIVE",
        "UPDATING",
        "DELETING",
        "DELETED",
        "FAILED",
        "PENDING_SETUP",
        "PENDING_DELETE",
    )
)


def serialize_json(value: ClusterStatus) -> str:
    return value


def deserialize_json(data: str) -> ClusterStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterStatus value: {data!r}")
    return cast(ClusterStatus, data)
