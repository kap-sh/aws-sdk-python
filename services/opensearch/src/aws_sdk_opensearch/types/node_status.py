"""Generated from Smithy shape ``com.amazonaws.opensearch#NodeStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

NodeStatus: TypeAlias = Literal[
    "Active",
    "StandBy",
    "NotAvailable",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Active",
        "StandBy",
        "NotAvailable",
    )
)


def serialize_json(value: NodeStatus) -> str:
    return value


def deserialize_json(data: str) -> NodeStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NodeStatus value: {data!r}")
    return cast(NodeStatus, data)
