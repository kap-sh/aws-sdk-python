"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ButtonsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.button

ButtonsList: TypeAlias = list["capo_lex_models_v2.types.button.Button"]


# --- restJson1 ser/de ---
def serialize_json(value: ButtonsList) -> list:
    import capo_lex_models_v2.types.button

    out: list = []
    for item in value:
        out.append(capo_lex_models_v2.types.button.serialize_json(item))
    return out


def deserialize_json(data: list) -> ButtonsList:
    import capo_lex_models_v2.types.button

    out: ButtonsList = []
    for item in data:
        out.append(capo_lex_models_v2.types.button.deserialize_json(item))
    return out
