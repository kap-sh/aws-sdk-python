"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIBenchmarkJobSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.ai_benchmark_job_summary

AIBenchmarkJobSummaryList: TypeAlias = list[
    "capo_sagemaker.types.ai_benchmark_job_summary.AIBenchmarkJobSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIBenchmarkJobSummaryList) -> list:
    import capo_sagemaker.types.ai_benchmark_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.ai_benchmark_job_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AIBenchmarkJobSummaryList:
    import capo_sagemaker.types.ai_benchmark_job_summary

    out: AIBenchmarkJobSummaryList = []
    for item in data:
        out.append(
            capo_sagemaker.types.ai_benchmark_job_summary.deserialize_aws_json_1_1(item)
        )
    return out
