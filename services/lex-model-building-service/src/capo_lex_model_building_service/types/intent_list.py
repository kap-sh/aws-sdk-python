"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#IntentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.intent

IntentList: TypeAlias = list["capo_lex_model_building_service.types.intent.Intent"]


# --- restJson1 ser/de ---
def serialize_json(value: IntentList) -> list:
    import capo_lex_model_building_service.types.intent

    out: list = []
    for item in value:
        out.append(capo_lex_model_building_service.types.intent.serialize_json(item))
    return out


def deserialize_json(data: list) -> IntentList:
    import capo_lex_model_building_service.types.intent

    out: IntentList = []
    for item in data:
        out.append(capo_lex_model_building_service.types.intent.deserialize_json(item))
    return out
