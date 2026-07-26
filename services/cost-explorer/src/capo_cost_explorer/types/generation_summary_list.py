"""Generated from Smithy shape ``com.amazonaws.costexplorer#GenerationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_explorer.types.generation_summary

GenerationSummaryList: TypeAlias = list[
    "capo_cost_explorer.types.generation_summary.GenerationSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GenerationSummaryList) -> list:
    import capo_cost_explorer.types.generation_summary

    out: list = []
    for item in value:
        out.append(
            capo_cost_explorer.types.generation_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> GenerationSummaryList:
    import capo_cost_explorer.types.generation_summary

    out: GenerationSummaryList = []
    for item in data:
        out.append(
            capo_cost_explorer.types.generation_summary.deserialize_aws_json_1_1(item)
        )
    return out
