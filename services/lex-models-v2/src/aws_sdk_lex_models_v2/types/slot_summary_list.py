"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.slot_summary

SlotSummaryList: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.slot_summary.SlotSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SlotSummaryList) -> list:
    import aws_sdk_lex_models_v2.types.slot_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_lex_models_v2.types.slot_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> SlotSummaryList:
    import aws_sdk_lex_models_v2.types.slot_summary

    out: SlotSummaryList = []
    for item in data:
        out.append(aws_sdk_lex_models_v2.types.slot_summary.deserialize_json(item))
    return out
