"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeAIBenchmarkJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.ai_benchmark_job_arn
    import capo_sagemaker.types.ai_benchmark_job_status
    import capo_sagemaker.types.ai_benchmark_network_config
    import capo_sagemaker.types.ai_benchmark_output_result
    import capo_sagemaker.types.ai_benchmark_target
    import capo_sagemaker.types.ai_entity_name
    import capo_sagemaker.types.ai_resource_identifier
    import capo_sagemaker.types.failure_reason
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.tag_list
    import capo_sagemaker.types.timestamp


class DescribeAIBenchmarkJobResponse(TypedDict, closed=True):
    ai_benchmark_job_name: NotRequired[
        "capo_sagemaker.types.ai_entity_name.AIEntityName"
    ]
    """<p>The name of the AI benchmark job.</p>"""
    ai_benchmark_job_arn: NotRequired[
        "capo_sagemaker.types.ai_benchmark_job_arn.AIBenchmarkJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the AI benchmark job.</p>"""
    ai_benchmark_job_status: NotRequired[
        "capo_sagemaker.types.ai_benchmark_job_status.AIBenchmarkJobStatus"
    ]
    """<p>The status of the AI benchmark job.</p>"""
    failure_reason: NotRequired["capo_sagemaker.types.failure_reason.FailureReason"]
    """<p>If the benchmark job failed, the reason it failed.</p>"""
    benchmark_target: NotRequired[
        "capo_sagemaker.types.ai_benchmark_target.AIBenchmarkTarget"
    ]
    """<p>The target endpoint that was benchmarked.</p>"""
    output_config: NotRequired[
        "capo_sagemaker.types.ai_benchmark_output_result.AIBenchmarkOutputResult"
    ]
    """<p>The output configuration for the benchmark job, including the Amazon S3 output location and CloudWatch log information.</p>"""
    ai_workload_config_identifier: NotRequired[
        "capo_sagemaker.types.ai_resource_identifier.AIResourceIdentifier"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the AI workload configuration used for this benchmark job.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role used by the benchmark job.</p>"""
    network_config: NotRequired[
        "capo_sagemaker.types.ai_benchmark_network_config.AIBenchmarkNetworkConfig"
    ]
    """<p>The network configuration for the benchmark job.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the benchmark job was created.</p>"""
    start_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the benchmark job started running.</p>"""
    end_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the benchmark job completed.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>The tags associated with the benchmark job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAIBenchmarkJobResponse) -> dict:
    out: dict = {}
    if "ai_benchmark_job_name" in value:
        out["AIBenchmarkJobName"] = value["ai_benchmark_job_name"]
    if "ai_benchmark_job_arn" in value:
        out["AIBenchmarkJobArn"] = value["ai_benchmark_job_arn"]
    if "ai_benchmark_job_status" in value:
        import capo_sagemaker.types.ai_benchmark_job_status

        out["AIBenchmarkJobStatus"] = (
            capo_sagemaker.types.ai_benchmark_job_status.serialize_aws_json_1_1(
                value["ai_benchmark_job_status"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "benchmark_target" in value:
        import capo_sagemaker.types.ai_benchmark_target

        out["BenchmarkTarget"] = (
            capo_sagemaker.types.ai_benchmark_target.serialize_aws_json_1_1(
                value["benchmark_target"]
            )
        )
    if "output_config" in value:
        import capo_sagemaker.types.ai_benchmark_output_result

        out["OutputConfig"] = (
            capo_sagemaker.types.ai_benchmark_output_result.serialize_aws_json_1_1(
                value["output_config"]
            )
        )
    if "ai_workload_config_identifier" in value:
        out["AIWorkloadConfigIdentifier"] = value["ai_workload_config_identifier"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "network_config" in value:
        import capo_sagemaker.types.ai_benchmark_network_config

        out["NetworkConfig"] = (
            capo_sagemaker.types.ai_benchmark_network_config.serialize_aws_json_1_1(
                value["network_config"]
            )
        )
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "start_time" in value:
        import capo_sagemaker.types.timestamp

        out["StartTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_sagemaker.types.timestamp

        out["EndTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAIBenchmarkJobResponse:
    out: DescribeAIBenchmarkJobResponse = {}  # type: ignore[typeddict-item]
    if "AIBenchmarkJobName" in data:
        out["ai_benchmark_job_name"] = data["AIBenchmarkJobName"]
    if "AIBenchmarkJobArn" in data:
        out["ai_benchmark_job_arn"] = data["AIBenchmarkJobArn"]
    if "AIBenchmarkJobStatus" in data:
        import capo_sagemaker.types.ai_benchmark_job_status

        out["ai_benchmark_job_status"] = (
            capo_sagemaker.types.ai_benchmark_job_status.deserialize_aws_json_1_1(
                data["AIBenchmarkJobStatus"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "BenchmarkTarget" in data:
        import capo_sagemaker.types.ai_benchmark_target

        out["benchmark_target"] = (
            capo_sagemaker.types.ai_benchmark_target.deserialize_aws_json_1_1(
                data["BenchmarkTarget"]
            )
        )
    if "OutputConfig" in data:
        import capo_sagemaker.types.ai_benchmark_output_result

        out["output_config"] = (
            capo_sagemaker.types.ai_benchmark_output_result.deserialize_aws_json_1_1(
                data["OutputConfig"]
            )
        )
    if "AIWorkloadConfigIdentifier" in data:
        out["ai_workload_config_identifier"] = data["AIWorkloadConfigIdentifier"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "NetworkConfig" in data:
        import capo_sagemaker.types.ai_benchmark_network_config

        out["network_config"] = (
            capo_sagemaker.types.ai_benchmark_network_config.deserialize_aws_json_1_1(
                data["NetworkConfig"]
            )
        )
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "StartTime" in data:
        import capo_sagemaker.types.timestamp

        out["start_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "EndTime" in data:
        import capo_sagemaker.types.timestamp

        out["end_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "Tags" in data:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
