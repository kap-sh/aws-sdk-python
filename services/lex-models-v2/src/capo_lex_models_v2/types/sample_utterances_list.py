"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SampleUtterancesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.sample_utterance

SampleUtterancesList: TypeAlias = list[
    "capo_lex_models_v2.types.sample_utterance.SampleUtterance"
]


# --- restJson1 ser/de ---
def serialize_json(value: SampleUtterancesList) -> list:
    import capo_lex_models_v2.types.sample_utterance

    out: list = []
    for item in value:
        out.append(capo_lex_models_v2.types.sample_utterance.serialize_json(item))
    return out


def deserialize_json(data: list) -> SampleUtterancesList:
    import capo_lex_models_v2.types.sample_utterance

    out: SampleUtterancesList = []
    for item in data:
        out.append(capo_lex_models_v2.types.sample_utterance.deserialize_json(item))
    return out
