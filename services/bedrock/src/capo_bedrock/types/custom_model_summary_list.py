"""Generated from Smithy shape ``com.amazonaws.bedrock#CustomModelSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.custom_model_summary

CustomModelSummaryList: TypeAlias = list[
    "capo_bedrock.types.custom_model_summary.CustomModelSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomModelSummaryList) -> list:
    import capo_bedrock.types.custom_model_summary

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.custom_model_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> CustomModelSummaryList:
    import capo_bedrock.types.custom_model_summary

    out: CustomModelSummaryList = []
    for item in data:
        out.append(capo_bedrock.types.custom_model_summary.deserialize_json(item))
    return out
