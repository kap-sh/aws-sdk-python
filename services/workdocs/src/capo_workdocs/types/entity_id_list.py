"""Generated from Smithy shape ``com.amazonaws.workdocs#EntityIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workdocs.types.id_type

EntityIdList: TypeAlias = list["capo_workdocs.types.id_type.IdType"]


# --- restJson1 ser/de ---
def serialize_json(value: EntityIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> EntityIdList:
    return list(data)
