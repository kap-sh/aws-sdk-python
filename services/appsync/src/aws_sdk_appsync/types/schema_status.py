"""Generated from Smithy shape ``com.amazonaws.appsync#SchemaStatus``."""

from typing import Literal, TypeAlias, cast

SchemaStatus: TypeAlias = Literal[
    "PROCESSING",
    "ACTIVE",
    "DELETING",
    "FAILED",
    "SUCCESS",
    "NOT_APPLICABLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SchemaStatus) -> str:
    return value


def deserialize_json(data: str) -> SchemaStatus:
    return cast(SchemaStatus, data)
