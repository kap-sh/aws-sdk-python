"""Generated from Smithy shape ``com.amazonaws.ram#ResourceShareAssociationType``."""

from typing import Literal, TypeAlias, cast

ResourceShareAssociationType: TypeAlias = Literal[
    "PRINCIPAL",
    "RESOURCE",
    "SOURCE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceShareAssociationType) -> str:
    return value


def deserialize_json(data: str) -> ResourceShareAssociationType:
    return cast(ResourceShareAssociationType, data)
