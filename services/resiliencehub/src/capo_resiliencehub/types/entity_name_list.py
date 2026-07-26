"""Generated from Smithy shape ``com.amazonaws.resiliencehub#EntityNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehub.types.entity_name

EntityNameList: TypeAlias = list["capo_resiliencehub.types.entity_name.EntityName"]


# --- restJson1 ser/de ---
def serialize_json(value: EntityNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> EntityNameList:
    return list(data)
