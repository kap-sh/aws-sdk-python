"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UtteranceBotResponses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.utterance_bot_response

UtteranceBotResponses: TypeAlias = list[
    "capo_lex_models_v2.types.utterance_bot_response.UtteranceBotResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: UtteranceBotResponses) -> list:
    import capo_lex_models_v2.types.utterance_bot_response

    out: list = []
    for item in value:
        out.append(capo_lex_models_v2.types.utterance_bot_response.serialize_json(item))
    return out


def deserialize_json(data: list) -> UtteranceBotResponses:
    import capo_lex_models_v2.types.utterance_bot_response

    out: UtteranceBotResponses = []
    for item in data:
        out.append(
            capo_lex_models_v2.types.utterance_bot_response.deserialize_json(item)
        )
    return out
