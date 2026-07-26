"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ObjectType``."""

from typing import Literal, TypeAlias, cast

ObjectType: TypeAlias = Literal[
    "NODE",
    "LEAF_NODE",
    "POLICY",
    "INDEX",
]


# --- restJson1 ser/de ---
def serialize_json(value: ObjectType) -> str:
    return value


def deserialize_json(data: str) -> ObjectType:
    return cast(ObjectType, data)
