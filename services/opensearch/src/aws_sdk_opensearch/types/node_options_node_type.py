"""Generated from Smithy shape ``com.amazonaws.opensearch#NodeOptionsNodeType``."""

from typing import Literal, TypeAlias, cast

NodeOptionsNodeType: TypeAlias = Literal["coordinator",]


# --- restJson1 ser/de ---
def serialize_json(value: NodeOptionsNodeType) -> str:
    return value


def deserialize_json(data: str) -> NodeOptionsNodeType:
    return cast(NodeOptionsNodeType, data)
