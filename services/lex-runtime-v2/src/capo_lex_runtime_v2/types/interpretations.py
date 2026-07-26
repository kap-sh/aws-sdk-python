"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#Interpretations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.interpretation

Interpretations: TypeAlias = list[
    "capo_lex_runtime_v2.types.interpretation.Interpretation"
]


# --- restJson1 ser/de ---
def serialize_json(value: Interpretations) -> list:
    import capo_lex_runtime_v2.types.interpretation

    out: list = []
    for item in value:
        out.append(capo_lex_runtime_v2.types.interpretation.serialize_json(item))
    return out


def deserialize_json(data: list) -> Interpretations:
    import capo_lex_runtime_v2.types.interpretation

    out: Interpretations = []
    for item in data:
        out.append(capo_lex_runtime_v2.types.interpretation.deserialize_json(item))
    return out
