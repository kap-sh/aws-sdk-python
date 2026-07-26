"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#RuntimeHintValuesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.runtime_hint_value

RuntimeHintValuesList: TypeAlias = list[
    "capo_lex_models_v2.types.runtime_hint_value.RuntimeHintValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeHintValuesList) -> list:
    import capo_lex_models_v2.types.runtime_hint_value

    out: list = []
    for item in value:
        out.append(capo_lex_models_v2.types.runtime_hint_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> RuntimeHintValuesList:
    import capo_lex_models_v2.types.runtime_hint_value

    out: RuntimeHintValuesList = []
    for item in data:
        out.append(capo_lex_models_v2.types.runtime_hint_value.deserialize_json(item))
    return out
