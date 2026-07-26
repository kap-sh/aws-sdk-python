"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SubSlotTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.sub_slot_type_composition

SubSlotTypeList: TypeAlias = list[
    "capo_lex_models_v2.types.sub_slot_type_composition.SubSlotTypeComposition"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubSlotTypeList) -> list:
    import capo_lex_models_v2.types.sub_slot_type_composition

    out: list = []
    for item in value:
        out.append(
            capo_lex_models_v2.types.sub_slot_type_composition.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SubSlotTypeList:
    import capo_lex_models_v2.types.sub_slot_type_composition

    out: SubSlotTypeList = []
    for item in data:
        out.append(
            capo_lex_models_v2.types.sub_slot_type_composition.deserialize_json(item)
        )
    return out
