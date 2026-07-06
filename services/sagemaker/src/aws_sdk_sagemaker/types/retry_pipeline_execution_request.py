"""Generated from Smithy shape ``com.amazonaws.sagemaker#RetryPipelineExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.idempotency_token
    import aws_sdk_sagemaker.types.parallelism_configuration
    import aws_sdk_sagemaker.types.pipeline_execution_arn


class RetryPipelineExecutionRequest(TypedDict, closed=True):
    pipeline_execution_arn: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_execution_arn.PipelineExecutionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the pipeline execution.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_sagemaker.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the operation. An idempotent operation completes no more than once.</p>"""
    parallelism_configuration: NotRequired[
        "aws_sdk_sagemaker.types.parallelism_configuration.ParallelismConfiguration"
    ]
    """<p>This configuration, if specified, overrides the parallelism configuration of the parent pipeline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetryPipelineExecutionRequest) -> dict:
    out: dict = {}
    if "pipeline_execution_arn" in value:
        out["PipelineExecutionArn"] = value["pipeline_execution_arn"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "parallelism_configuration" in value:
        import aws_sdk_sagemaker.types.parallelism_configuration

        out["ParallelismConfiguration"] = (
            aws_sdk_sagemaker.types.parallelism_configuration.serialize_aws_json_1_1(
                value["parallelism_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RetryPipelineExecutionRequest:
    out: RetryPipelineExecutionRequest = {}  # type: ignore[typeddict-item]
    if "PipelineExecutionArn" in data:
        out["pipeline_execution_arn"] = data["PipelineExecutionArn"]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "ParallelismConfiguration" in data:
        import aws_sdk_sagemaker.types.parallelism_configuration

        out["parallelism_configuration"] = (
            aws_sdk_sagemaker.types.parallelism_configuration.deserialize_aws_json_1_1(
                data["ParallelismConfiguration"]
            )
        )
    return out
