"""Generated from Smithy shape ``com.amazonaws.databrew#EntityTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_databrew.types.entity_type

EntityTypeList: TypeAlias = list["aws_sdk_databrew.types.entity_type.EntityType"]


# --- restJson1 ser/de ---
def serialize_json(value: EntityTypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> EntityTypeList:
    return list(data)
