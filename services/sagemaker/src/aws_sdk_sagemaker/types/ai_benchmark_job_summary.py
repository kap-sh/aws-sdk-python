"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIBenchmarkJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_benchmark_job_arn
    import aws_sdk_sagemaker.types.ai_benchmark_job_status
    import aws_sdk_sagemaker.types.ai_entity_name
    import aws_sdk_sagemaker.types.timestamp


class AIBenchmarkJobSummary(TypedDict, closed=True):
    ai_benchmark_job_name: NotRequired[
        "aws_sdk_sagemaker.types.ai_entity_name.AIEntityName"
    ]
    """<p>The name of the benchmark job.</p>"""
    ai_benchmark_job_arn: NotRequired[
        "aws_sdk_sagemaker.types.ai_benchmark_job_arn.AIBenchmarkJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the benchmark job.</p>"""
    ai_benchmark_job_status: NotRequired[
        "aws_sdk_sagemaker.types.ai_benchmark_job_status.AIBenchmarkJobStatus"
    ]
    """<p>The status of the benchmark job.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the benchmark job was created.</p>"""
    end_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the benchmark job completed.</p>"""
    ai_workload_config_name: NotRequired[
        "aws_sdk_sagemaker.types.ai_entity_name.AIEntityName"
    ]
    """<p>The name of the AI workload configuration used by the benchmark job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIBenchmarkJobSummary) -> dict:
    out: dict = {}
    if "ai_benchmark_job_name" in value:
        out["AIBenchmarkJobName"] = value["ai_benchmark_job_name"]
    if "ai_benchmark_job_arn" in value:
        out["AIBenchmarkJobArn"] = value["ai_benchmark_job_arn"]
    if "ai_benchmark_job_status" in value:
        import aws_sdk_sagemaker.types.ai_benchmark_job_status

        out["AIBenchmarkJobStatus"] = (
            aws_sdk_sagemaker.types.ai_benchmark_job_status.serialize_aws_json_1_1(
                value["ai_benchmark_job_status"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "end_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["EndTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "ai_workload_config_name" in value:
        out["AIWorkloadConfigName"] = value["ai_workload_config_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AIBenchmarkJobSummary:
    out: AIBenchmarkJobSummary = {}  # type: ignore[typeddict-item]
    if "AIBenchmarkJobName" in data:
        out["ai_benchmark_job_name"] = data["AIBenchmarkJobName"]
    if "AIBenchmarkJobArn" in data:
        out["ai_benchmark_job_arn"] = data["AIBenchmarkJobArn"]
    if "AIBenchmarkJobStatus" in data:
        import aws_sdk_sagemaker.types.ai_benchmark_job_status

        out["ai_benchmark_job_status"] = (
            aws_sdk_sagemaker.types.ai_benchmark_job_status.deserialize_aws_json_1_1(
                data["AIBenchmarkJobStatus"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "EndTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["end_time"] = aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "AIWorkloadConfigName" in data:
        out["ai_workload_config_name"] = data["AIWorkloadConfigName"]
    return out
