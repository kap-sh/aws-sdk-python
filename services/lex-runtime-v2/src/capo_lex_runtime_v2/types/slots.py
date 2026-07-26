"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#Slots``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.non_empty_string
    import capo_lex_runtime_v2.types.slot

Slots: TypeAlias = dict[
    "capo_lex_runtime_v2.types.non_empty_string.NonEmptyString",
    "capo_lex_runtime_v2.types.slot.Slot",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Slots) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_lex_runtime_v2.types.slot

        out[key] = capo_lex_runtime_v2.types.slot.serialize_json(value)
    return out


def deserialize_json(data: dict) -> Slots:
    out: Slots = {}
    for key, value in data.items():
        import capo_lex_runtime_v2.types.slot

        out[key] = capo_lex_runtime_v2.types.slot.deserialize_json(value)
    return out
