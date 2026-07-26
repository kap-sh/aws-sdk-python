"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotTypeSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.slot_type_summary

SlotTypeSummaryList: TypeAlias = list[
    "capo_lex_models_v2.types.slot_type_summary.SlotTypeSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SlotTypeSummaryList) -> list:
    import capo_lex_models_v2.types.slot_type_summary

    out: list = []
    for item in value:
        out.append(capo_lex_models_v2.types.slot_type_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> SlotTypeSummaryList:
    import capo_lex_models_v2.types.slot_type_summary

    out: SlotTypeSummaryList = []
    for item in data:
        out.append(capo_lex_models_v2.types.slot_type_summary.deserialize_json(item))
    return out
