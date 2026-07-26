"""Generated from Smithy shape ``com.amazonaws.sagemaker#FeatureGroupSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.feature_group_summary

FeatureGroupSummaries: TypeAlias = list[
    "capo_sagemaker.types.feature_group_summary.FeatureGroupSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeatureGroupSummaries) -> list:
    import capo_sagemaker.types.feature_group_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.feature_group_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FeatureGroupSummaries:
    import capo_sagemaker.types.feature_group_summary

    out: FeatureGroupSummaries = []
    for item in data:
        out.append(
            capo_sagemaker.types.feature_group_summary.deserialize_aws_json_1_1(item)
        )
    return out
