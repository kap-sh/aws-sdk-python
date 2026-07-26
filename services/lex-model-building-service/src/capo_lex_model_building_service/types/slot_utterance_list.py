"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#SlotUtteranceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.utterance

SlotUtteranceList: TypeAlias = list[
    "capo_lex_model_building_service.types.utterance.Utterance"
]


# --- restJson1 ser/de ---
def serialize_json(value: SlotUtteranceList) -> list:
    return list(value)


def deserialize_json(data: list) -> SlotUtteranceList:
    return list(data)
