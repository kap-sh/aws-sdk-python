"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#StringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.string

StringList: TypeAlias = list["capo_lex_model_building_service.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: StringList) -> list:
    return list(value)


def deserialize_json(data: list) -> StringList:
    return list(data)
