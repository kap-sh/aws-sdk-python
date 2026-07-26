"""Generated from Smithy shape ``com.amazonaws.s3tables#SchemaV2FieldType``."""

from typing import Literal, TypeAlias, cast

SchemaV2FieldType: TypeAlias = Literal["struct",]


# --- restJson1 ser/de ---
def serialize_json(value: SchemaV2FieldType) -> str:
    return value


def deserialize_json(data: str) -> SchemaV2FieldType:
    return cast(SchemaV2FieldType, data)
