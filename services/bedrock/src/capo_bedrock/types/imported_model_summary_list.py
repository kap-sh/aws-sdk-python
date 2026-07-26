"""Generated from Smithy shape ``com.amazonaws.bedrock#ImportedModelSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.imported_model_summary

ImportedModelSummaryList: TypeAlias = list[
    "capo_bedrock.types.imported_model_summary.ImportedModelSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImportedModelSummaryList) -> list:
    import capo_bedrock.types.imported_model_summary

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.imported_model_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImportedModelSummaryList:
    import capo_bedrock.types.imported_model_summary

    out: ImportedModelSummaryList = []
    for item in data:
        out.append(capo_bedrock.types.imported_model_summary.deserialize_json(item))
    return out
