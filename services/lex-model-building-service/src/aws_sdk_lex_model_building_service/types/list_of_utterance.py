"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#ListOfUtterance``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.utterance_data

ListOfUtterance: TypeAlias = list[
    "aws_sdk_lex_model_building_service.types.utterance_data.UtteranceData"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfUtterance) -> list:
    import aws_sdk_lex_model_building_service.types.utterance_data

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_model_building_service.types.utterance_data.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListOfUtterance:
    import aws_sdk_lex_model_building_service.types.utterance_data

    out: ListOfUtterance = []
    for item in data:
        out.append(
            aws_sdk_lex_model_building_service.types.utterance_data.deserialize_json(
                item
            )
        )
    return out
