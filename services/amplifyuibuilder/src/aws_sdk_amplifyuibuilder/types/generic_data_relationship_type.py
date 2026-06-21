"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#GenericDataRelationshipType``."""

from typing import Literal, TypeAlias, cast

GenericDataRelationshipType: TypeAlias = Literal[
    "HAS_MANY",
    "HAS_ONE",
    "BELONGS_TO",
]


# --- restJson1 ser/de ---
def serialize_json(value: GenericDataRelationshipType) -> str:
    return value


def deserialize_json(data: str) -> GenericDataRelationshipType:
    return cast(GenericDataRelationshipType, data)
