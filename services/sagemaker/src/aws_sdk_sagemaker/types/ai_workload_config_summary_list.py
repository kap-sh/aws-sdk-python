"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIWorkloadConfigSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_workload_config_summary

AIWorkloadConfigSummaryList: TypeAlias = list[
    "aws_sdk_sagemaker.types.ai_workload_config_summary.AIWorkloadConfigSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIWorkloadConfigSummaryList) -> list:
    import aws_sdk_sagemaker.types.ai_workload_config_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.ai_workload_config_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AIWorkloadConfigSummaryList:
    import aws_sdk_sagemaker.types.ai_workload_config_summary

    out: AIWorkloadConfigSummaryList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.ai_workload_config_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
