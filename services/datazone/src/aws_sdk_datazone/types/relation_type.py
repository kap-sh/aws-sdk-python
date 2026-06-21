"""Generated from Smithy shape ``com.amazonaws.datazone#RelationType``."""

from typing import Literal, TypeAlias, cast

RelationType: TypeAlias = Literal["LINEAGE",]


# --- restJson1 ser/de ---
def serialize_json(value: RelationType) -> str:
    return value


def deserialize_json(data: str) -> RelationType:
    return cast(RelationType, data)
