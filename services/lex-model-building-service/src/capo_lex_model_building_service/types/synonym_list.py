"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#SynonymList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.value

SynonymList: TypeAlias = list["capo_lex_model_building_service.types.value.Value"]


# --- restJson1 ser/de ---
def serialize_json(value: SynonymList) -> list:
    return list(value)


def deserialize_json(data: list) -> SynonymList:
    return list(data)
