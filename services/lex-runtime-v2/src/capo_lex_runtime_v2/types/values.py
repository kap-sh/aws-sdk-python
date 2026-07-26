"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#Values``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.slot

Values: TypeAlias = list["capo_lex_runtime_v2.types.slot.Slot"]


# --- restJson1 ser/de ---
def serialize_json(value: Values) -> list:
    import capo_lex_runtime_v2.types.slot

    out: list = []
    for item in value:
        out.append(capo_lex_runtime_v2.types.slot.serialize_json(item))
    return out


def deserialize_json(data: list) -> Values:
    import capo_lex_runtime_v2.types.slot

    out: Values = []
    for item in data:
        out.append(capo_lex_runtime_v2.types.slot.deserialize_json(item))
    return out
