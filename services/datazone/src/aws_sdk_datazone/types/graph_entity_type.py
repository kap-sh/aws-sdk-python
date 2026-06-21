"""Generated from Smithy shape ``com.amazonaws.datazone#GraphEntityType``."""

from typing import Literal, TypeAlias, cast

GraphEntityType: TypeAlias = Literal["LINEAGE_NODE",]


# --- restJson1 ser/de ---
def serialize_json(value: GraphEntityType) -> str:
    return value


def deserialize_json(data: str) -> GraphEntityType:
    return cast(GraphEntityType, data)
