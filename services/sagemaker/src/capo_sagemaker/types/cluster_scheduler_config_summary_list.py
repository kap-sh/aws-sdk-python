"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterSchedulerConfigSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_scheduler_config_summary

ClusterSchedulerConfigSummaryList: TypeAlias = list[
    "capo_sagemaker.types.cluster_scheduler_config_summary.ClusterSchedulerConfigSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterSchedulerConfigSummaryList) -> list:
    import capo_sagemaker.types.cluster_scheduler_config_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.cluster_scheduler_config_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ClusterSchedulerConfigSummaryList:
    import capo_sagemaker.types.cluster_scheduler_config_summary

    out: ClusterSchedulerConfigSummaryList = []
    for item in data:
        out.append(
            capo_sagemaker.types.cluster_scheduler_config_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
