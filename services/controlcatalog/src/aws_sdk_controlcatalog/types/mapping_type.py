"""Generated from Smithy shape ``com.amazonaws.controlcatalog#MappingType``."""

from typing import Literal, TypeAlias, cast

MappingType: TypeAlias = Literal[
    "FRAMEWORK",
    "COMMON_CONTROL",
    "RELATED_CONTROL",
]


# --- restJson1 ser/de ---
def serialize_json(value: MappingType) -> str:
    return value


def deserialize_json(data: str) -> MappingType:
    return cast(MappingType, data)
