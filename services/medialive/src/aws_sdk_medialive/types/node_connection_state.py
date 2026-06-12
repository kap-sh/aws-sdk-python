"""Generated from Smithy shape ``com.amazonaws.medialive#NodeConnectionState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Used in DescribeNodeSummary."""
NodeConnectionState: TypeAlias = Literal[
    "CONNECTED",
    "DISCONNECTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONNECTED",
        "DISCONNECTED",
    )
)


def serialize_json(value: NodeConnectionState) -> str:
    return value


def deserialize_json(data: str) -> NodeConnectionState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NodeConnectionState value: {data!r}")
    return cast(NodeConnectionState, data)
