"""Generated from Smithy shape ``com.amazonaws.medialive#NodeRole``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Used in CreateNodeRequest, CreateNodeRegistrationScriptRequest, DescribeNodeResult, DescribeNodeSummary, UpdateNodeRequest."""
NodeRole: TypeAlias = Literal[
    "BACKUP",
    "ACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BACKUP",
        "ACTIVE",
    )
)


def serialize_json(value: NodeRole) -> str:
    return value


def deserialize_json(data: str) -> NodeRole:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NodeRole value: {data!r}")
    return cast(NodeRole, data)
