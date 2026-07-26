"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#ListOfUtterance``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.utterance_data

ListOfUtterance: TypeAlias = list[
    "capo_lex_model_building_service.types.utterance_data.UtteranceData"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfUtterance) -> list:
    import capo_lex_model_building_service.types.utterance_data

    out: list = []
    for item in value:
        out.append(
            capo_lex_model_building_service.types.utterance_data.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListOfUtterance:
    import capo_lex_model_building_service.types.utterance_data

    out: ListOfUtterance = []
    for item in data:
        out.append(
            capo_lex_model_building_service.types.utterance_data.deserialize_json(item)
        )
    return out
