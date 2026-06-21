"""Generated from Smithy shape ``com.amazonaws.kafka#NodeType``."""

from typing import Literal, TypeAlias, cast

"""<p>The broker or Zookeeper node.</p>"""
NodeType: TypeAlias = Literal["BROKER",]


# --- restJson1 ser/de ---
def serialize_json(value: NodeType) -> str:
    return value


def deserialize_json(data: str) -> NodeType:
    return cast(NodeType, data)
