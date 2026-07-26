"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#OutputContextsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.output_context

OutputContextsList: TypeAlias = list[
    "capo_lex_models_v2.types.output_context.OutputContext"
]


# --- restJson1 ser/de ---
def serialize_json(value: OutputContextsList) -> list:
    import capo_lex_models_v2.types.output_context

    out: list = []
    for item in value:
        out.append(capo_lex_models_v2.types.output_context.serialize_json(item))
    return out


def deserialize_json(data: list) -> OutputContextsList:
    import capo_lex_models_v2.types.output_context

    out: OutputContextsList = []
    for item in data:
        out.append(capo_lex_models_v2.types.output_context.deserialize_json(item))
    return out
