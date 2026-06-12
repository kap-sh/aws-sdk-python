"""Generated from Smithy shape ``com.amazonaws.kafka#NodeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kafka.errors import DeserializationError

"""<p>The broker or Zookeeper node.</p>"""
NodeType: TypeAlias = Literal["BROKER",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("BROKER",))


def serialize_json(value: NodeType) -> str:
    return value


def deserialize_json(data: str) -> NodeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NodeType value: {data!r}")
    return cast(NodeType, data)
