"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdMappingType``."""

from typing import Literal, TypeAlias, cast

IdMappingType: TypeAlias = Literal[
    "PROVIDER",
    "RULE_BASED",
]


# --- restJson1 ser/de ---
def serialize_json(value: IdMappingType) -> str:
    return value


def deserialize_json(data: str) -> IdMappingType:
    return cast(IdMappingType, data)
