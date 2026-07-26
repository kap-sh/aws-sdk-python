"""Generated from Smithy shape ``com.amazonaws.clouddirectory#FacetAttributeType``."""

from typing import Literal, TypeAlias, cast

FacetAttributeType: TypeAlias = Literal[
    "STRING",
    "BINARY",
    "BOOLEAN",
    "NUMBER",
    "DATETIME",
    "VARIANT",
]


# --- restJson1 ser/de ---
def serialize_json(value: FacetAttributeType) -> str:
    return value


def deserialize_json(data: str) -> FacetAttributeType:
    return cast(FacetAttributeType, data)
