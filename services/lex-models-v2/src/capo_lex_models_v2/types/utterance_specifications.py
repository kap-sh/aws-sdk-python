"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UtteranceSpecifications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.utterance_specification

UtteranceSpecifications: TypeAlias = list[
    "capo_lex_models_v2.types.utterance_specification.UtteranceSpecification"
]


# --- restJson1 ser/de ---
def serialize_json(value: UtteranceSpecifications) -> list:
    import capo_lex_models_v2.types.utterance_specification

    out: list = []
    for item in value:
        out.append(
            capo_lex_models_v2.types.utterance_specification.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> UtteranceSpecifications:
    import capo_lex_models_v2.types.utterance_specification

    out: UtteranceSpecifications = []
    for item in data:
        out.append(
            capo_lex_models_v2.types.utterance_specification.deserialize_json(item)
        )
    return out
