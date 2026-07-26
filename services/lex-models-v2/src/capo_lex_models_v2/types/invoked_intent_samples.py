"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#InvokedIntentSamples``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.invoked_intent_sample

InvokedIntentSamples: TypeAlias = list[
    "capo_lex_models_v2.types.invoked_intent_sample.InvokedIntentSample"
]


# --- restJson1 ser/de ---
def serialize_json(value: InvokedIntentSamples) -> list:
    import capo_lex_models_v2.types.invoked_intent_sample

    out: list = []
    for item in value:
        out.append(capo_lex_models_v2.types.invoked_intent_sample.serialize_json(item))
    return out


def deserialize_json(data: list) -> InvokedIntentSamples:
    import capo_lex_models_v2.types.invoked_intent_sample

    out: InvokedIntentSamples = []
    for item in data:
        out.append(
            capo_lex_models_v2.types.invoked_intent_sample.deserialize_json(item)
        )
    return out
