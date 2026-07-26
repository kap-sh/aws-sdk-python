"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SchemaConfiguration``."""

from typing import Literal, TypeAlias, cast

SchemaConfiguration: TypeAlias = Literal["DIFFERENTIAL_PRIVACY",]


# --- restJson1 ser/de ---
def serialize_json(value: SchemaConfiguration) -> str:
    return value


def deserialize_json(data: str) -> SchemaConfiguration:
    return cast(SchemaConfiguration, data)
