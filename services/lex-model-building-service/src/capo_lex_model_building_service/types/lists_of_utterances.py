"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#ListsOfUtterances``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.utterance_list

ListsOfUtterances: TypeAlias = list[
    "capo_lex_model_building_service.types.utterance_list.UtteranceList"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListsOfUtterances) -> list:
    import capo_lex_model_building_service.types.utterance_list

    out: list = []
    for item in value:
        out.append(
            capo_lex_model_building_service.types.utterance_list.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListsOfUtterances:
    import capo_lex_model_building_service.types.utterance_list

    out: ListsOfUtterances = []
    for item in data:
        out.append(
            capo_lex_model_building_service.types.utterance_list.deserialize_json(item)
        )
    return out
