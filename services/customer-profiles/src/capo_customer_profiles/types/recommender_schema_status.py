"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RecommenderSchemaStatus``."""

from typing import Literal, TypeAlias, cast

RecommenderSchemaStatus: TypeAlias = Literal[
    "ACTIVE",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommenderSchemaStatus) -> str:
    return value


def deserialize_json(data: str) -> RecommenderSchemaStatus:
    return cast(RecommenderSchemaStatus, data)
