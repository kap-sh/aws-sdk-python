"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateAIBenchmarkJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.ai_benchmark_network_config
    import capo_sagemaker.types.ai_benchmark_output_config
    import capo_sagemaker.types.ai_benchmark_target
    import capo_sagemaker.types.ai_entity_name
    import capo_sagemaker.types.ai_resource_identifier
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.tag_list


class CreateAIBenchmarkJobRequest(TypedDict, closed=True):
    ai_benchmark_job_name: NotRequired[
        "capo_sagemaker.types.ai_entity_name.AIEntityName"
    ]
    """<p>The name of the AI benchmark job. The name must be unique within your Amazon Web Services account in the current Amazon Web Services Region.</p>"""
    benchmark_target: NotRequired[
        "capo_sagemaker.types.ai_benchmark_target.AIBenchmarkTarget"
    ]
    """<p>The target endpoint to benchmark. Specify a SageMaker endpoint by providing its name or Amazon Resource Name (ARN).</p>"""
    output_config: NotRequired[
        "capo_sagemaker.types.ai_benchmark_output_config.AIBenchmarkOutputConfig"
    ]
    """<p>The output configuration for the benchmark job, including the Amazon S3 location where benchmark results are stored.</p>"""
    ai_workload_config_identifier: NotRequired[
        "capo_sagemaker.types.ai_resource_identifier.AIResourceIdentifier"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the AI workload configuration to use for this benchmark job.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role that enables Amazon SageMaker AI to perform tasks on your behalf.</p>"""
    network_config: NotRequired[
        "capo_sagemaker.types.ai_benchmark_network_config.AIBenchmarkNetworkConfig"
    ]
    """<p>The network configuration for the benchmark job, including VPC settings.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>The metadata that you apply to Amazon Web Services resources to help you categorize and organize them. Each tag consists of a key and a value, both of which you define.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAIBenchmarkJobRequest) -> dict:
    out: dict = {}
    if "ai_benchmark_job_name" in value:
        out["AIBenchmarkJobName"] = value["ai_benchmark_job_name"]
    if "benchmark_target" in value:
        import capo_sagemaker.types.ai_benchmark_target

        out["BenchmarkTarget"] = (
            capo_sagemaker.types.ai_benchmark_target.serialize_aws_json_1_1(
                value["benchmark_target"]
            )
        )
    if "output_config" in value:
        import capo_sagemaker.types.ai_benchmark_output_config

        out["OutputConfig"] = (
            capo_sagemaker.types.ai_benchmark_output_config.serialize_aws_json_1_1(
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
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAIBenchmarkJobRequest:
    out: CreateAIBenchmarkJobRequest = {}  # type: ignore[typeddict-item]
    if "AIBenchmarkJobName" in data:
        out["ai_benchmark_job_name"] = data["AIBenchmarkJobName"]
    if "BenchmarkTarget" in data:
        import capo_sagemaker.types.ai_benchmark_target

        out["benchmark_target"] = (
            capo_sagemaker.types.ai_benchmark_target.deserialize_aws_json_1_1(
                data["BenchmarkTarget"]
            )
        )
    if "OutputConfig" in data:
        import capo_sagemaker.types.ai_benchmark_output_config

        out["output_config"] = (
            capo_sagemaker.types.ai_benchmark_output_config.deserialize_aws_json_1_1(
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
    if "Tags" in data:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
