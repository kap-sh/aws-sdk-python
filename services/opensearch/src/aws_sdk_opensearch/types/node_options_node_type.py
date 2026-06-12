"""Generated from Smithy shape ``com.amazonaws.opensearch#NodeOptionsNodeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

NodeOptionsNodeType: TypeAlias = Literal["coordinator",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("coordinator",))


def serialize_json(value: NodeOptionsNodeType) -> str:
    return value


def deserialize_json(data: str) -> NodeOptionsNodeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NodeOptionsNodeType value: {data!r}")
    return cast(NodeOptionsNodeType, data)
