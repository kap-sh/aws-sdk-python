"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetRelationshipType``."""

from typing import Literal, TypeAlias, cast

AssetRelationshipType: TypeAlias = Literal["HIERARCHY",]


# --- restJson1 ser/de ---
def serialize_json(value: AssetRelationshipType) -> str:
    return value


def deserialize_json(data: str) -> AssetRelationshipType:
    return cast(AssetRelationshipType, data)
