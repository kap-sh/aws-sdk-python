"""Generated from Smithy shape ``com.amazonaws.resiliencehub#PhysicalIdentifierType``."""

from typing import Literal, TypeAlias, cast

PhysicalIdentifierType: TypeAlias = Literal[
    "Arn",
    "Native",
]


# --- restJson1 ser/de ---
def serialize_json(value: PhysicalIdentifierType) -> str:
    return value


def deserialize_json(data: str) -> PhysicalIdentifierType:
    return cast(PhysicalIdentifierType, data)
