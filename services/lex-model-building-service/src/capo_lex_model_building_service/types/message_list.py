"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#MessageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.message

MessageList: TypeAlias = list["capo_lex_model_building_service.types.message.Message"]


# --- restJson1 ser/de ---
def serialize_json(value: MessageList) -> list:
    import capo_lex_model_building_service.types.message

    out: list = []
    for item in value:
        out.append(capo_lex_model_building_service.types.message.serialize_json(item))
    return out


def deserialize_json(data: list) -> MessageList:
    import capo_lex_model_building_service.types.message

    out: MessageList = []
    for item in data:
        out.append(capo_lex_model_building_service.types.message.deserialize_json(item))
    return out
