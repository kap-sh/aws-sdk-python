"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BuiltInSlotTypeSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.built_in_slot_type_summary

BuiltInSlotTypeSummaryList: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.built_in_slot_type_summary.BuiltInSlotTypeSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: BuiltInSlotTypeSummaryList) -> list:
    import aws_sdk_lex_models_v2.types.built_in_slot_type_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.built_in_slot_type_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BuiltInSlotTypeSummaryList:
    import aws_sdk_lex_models_v2.types.built_in_slot_type_summary

    out: BuiltInSlotTypeSummaryList = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.built_in_slot_type_summary.deserialize_json(
                item
            )
        )
    return out
