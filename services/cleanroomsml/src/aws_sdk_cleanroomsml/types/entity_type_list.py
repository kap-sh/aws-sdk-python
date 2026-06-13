"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#EntityTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.entity_type

EntityTypeList: TypeAlias = list["aws_sdk_cleanroomsml.types.entity_type.EntityType"]


# --- restJson1 ser/de ---
def serialize_json(value: EntityTypeList) -> list:
    import aws_sdk_cleanroomsml.types.entity_type

    out: list = []
    for item in value:
        out.append(aws_sdk_cleanroomsml.types.entity_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> EntityTypeList:
    import aws_sdk_cleanroomsml.types.entity_type

    out: EntityTypeList = []
    for item in data:
        out.append(aws_sdk_cleanroomsml.types.entity_type.deserialize_json(item))
    return out
