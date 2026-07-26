"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#SlotHintsSlotMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.name
    import capo_lex_runtime_v2.types.runtime_hint_details

SlotHintsSlotMap: TypeAlias = dict[
    "capo_lex_runtime_v2.types.name.Name",
    "capo_lex_runtime_v2.types.runtime_hint_details.RuntimeHintDetails",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: SlotHintsSlotMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_lex_runtime_v2.types.runtime_hint_details

        out[key] = capo_lex_runtime_v2.types.runtime_hint_details.serialize_json(value)
    return out


def deserialize_json(data: dict) -> SlotHintsSlotMap:
    out: SlotHintsSlotMap = {}
    for key, value in data.items():
        import capo_lex_runtime_v2.types.runtime_hint_details

        out[key] = capo_lex_runtime_v2.types.runtime_hint_details.deserialize_json(
            value
        )
    return out
