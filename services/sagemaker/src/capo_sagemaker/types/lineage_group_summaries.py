"""Generated from Smithy shape ``com.amazonaws.sagemaker#LineageGroupSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.lineage_group_summary

LineageGroupSummaries: TypeAlias = list[
    "capo_sagemaker.types.lineage_group_summary.LineageGroupSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LineageGroupSummaries) -> list:
    import capo_sagemaker.types.lineage_group_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.lineage_group_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LineageGroupSummaries:
    import capo_sagemaker.types.lineage_group_summary

    out: LineageGroupSummaries = []
    for item in data:
        out.append(
            capo_sagemaker.types.lineage_group_summary.deserialize_aws_json_1_1(item)
        )
    return out
