"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#IntentUtteranceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.utterance

IntentUtteranceList: TypeAlias = list[
    "capo_lex_model_building_service.types.utterance.Utterance"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntentUtteranceList) -> list:
    return list(value)


def deserialize_json(data: list) -> IntentUtteranceList:
    return list(data)
