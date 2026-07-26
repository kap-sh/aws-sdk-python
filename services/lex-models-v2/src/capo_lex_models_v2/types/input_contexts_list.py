"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#InputContextsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.input_context

InputContextsList: TypeAlias = list[
    "capo_lex_models_v2.types.input_context.InputContext"
]


# --- restJson1 ser/de ---
def serialize_json(value: InputContextsList) -> list:
    import capo_lex_models_v2.types.input_context

    out: list = []
    for item in value:
        out.append(capo_lex_models_v2.types.input_context.serialize_json(item))
    return out


def deserialize_json(data: list) -> InputContextsList:
    import capo_lex_models_v2.types.input_context

    out: InputContextsList = []
    for item in data:
        out.append(capo_lex_models_v2.types.input_context.deserialize_json(item))
    return out
