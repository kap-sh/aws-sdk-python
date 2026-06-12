"""Generated from Smithy shape ``com.amazonaws.sagemaker#PipelineExecutionStep``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cache_hit_result
    import aws_sdk_sagemaker.types.failure_reason
    import aws_sdk_sagemaker.types.integer
    import aws_sdk_sagemaker.types.pipeline_execution_step_metadata
    import aws_sdk_sagemaker.types.selective_execution_result
    import aws_sdk_sagemaker.types.step_description
    import aws_sdk_sagemaker.types.step_display_name
    import aws_sdk_sagemaker.types.step_name
    import aws_sdk_sagemaker.types.step_status
    import aws_sdk_sagemaker.types.timestamp


class PipelineExecutionStep(TypedDict):
    step_name: NotRequired["aws_sdk_sagemaker.types.step_name.StepName"]
    """<p>The name of the step that is executed.</p>"""
    step_display_name: NotRequired[
        "aws_sdk_sagemaker.types.step_display_name.StepDisplayName"
    ]
    """<p>The display name of the step.</p>"""
    step_description: NotRequired[
        "aws_sdk_sagemaker.types.step_description.StepDescription"
    ]
    """<p>The description of the step.</p>"""
    start_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The time that the step started executing.</p>"""
    end_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The time that the step stopped executing.</p>"""
    step_status: NotRequired["aws_sdk_sagemaker.types.step_status.StepStatus"]
    """<p>The status of the step execution.</p>"""
    cache_hit_result: NotRequired[
        "aws_sdk_sagemaker.types.cache_hit_result.CacheHitResult"
    ]
    """<p>If this pipeline execution step was cached, details on the cache hit.</p>"""
    failure_reason: NotRequired["aws_sdk_sagemaker.types.failure_reason.FailureReason"]
    """<p>The reason why the step failed execution. This is only returned if the step failed its execution.</p>"""
    metadata: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_execution_step_metadata.PipelineExecutionStepMetadata"
    ]
    """<p>Metadata to run the pipeline step.</p>"""
    attempt_count: NotRequired["aws_sdk_sagemaker.types.integer.Integer"]
    """<p>The current attempt of the execution step. For more information, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-retry-policy.html\">Retry Policy for SageMaker Pipelines steps</a>.</p>"""
    selective_execution_result: NotRequired[
        "aws_sdk_sagemaker.types.selective_execution_result.SelectiveExecutionResult"
    ]
    """<p>The ARN from an execution of the current pipeline from which results are reused for this step.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineExecutionStep) -> dict:
    out: dict = {}
    if "step_name" in value:
        out["StepName"] = value["step_name"]
    if "step_display_name" in value:
        out["StepDisplayName"] = value["step_display_name"]
    if "step_description" in value:
        out["StepDescription"] = value["step_description"]
    if "start_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["StartTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["EndTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "step_status" in value:
        import aws_sdk_sagemaker.types.step_status

        out["StepStatus"] = aws_sdk_sagemaker.types.step_status.serialize_aws_json_1_1(
            value["step_status"]
        )
    if "cache_hit_result" in value:
        import aws_sdk_sagemaker.types.cache_hit_result

        out["CacheHitResult"] = (
            aws_sdk_sagemaker.types.cache_hit_result.serialize_aws_json_1_1(
                value["cache_hit_result"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "metadata" in value:
        import aws_sdk_sagemaker.types.pipeline_execution_step_metadata

        out["Metadata"] = (
            aws_sdk_sagemaker.types.pipeline_execution_step_metadata.serialize_aws_json_1_1(
                value["metadata"]
            )
        )
    if "attempt_count" in value:
        out["AttemptCount"] = value["attempt_count"]
    if "selective_execution_result" in value:
        import aws_sdk_sagemaker.types.selective_execution_result

        out["SelectiveExecutionResult"] = (
            aws_sdk_sagemaker.types.selective_execution_result.serialize_aws_json_1_1(
                value["selective_execution_result"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineExecutionStep:
    out: PipelineExecutionStep = {}  # type: ignore[typeddict-item]
    if "StepName" in data:
        out["step_name"] = data["StepName"]
    if "StepDisplayName" in data:
        out["step_display_name"] = data["StepDisplayName"]
    if "StepDescription" in data:
        out["step_description"] = data["StepDescription"]
    if "StartTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["start_time"] = aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "EndTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["end_time"] = aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "StepStatus" in data:
        import aws_sdk_sagemaker.types.step_status

        out["step_status"] = (
            aws_sdk_sagemaker.types.step_status.deserialize_aws_json_1_1(
                data["StepStatus"]
            )
        )
    if "CacheHitResult" in data:
        import aws_sdk_sagemaker.types.cache_hit_result

        out["cache_hit_result"] = (
            aws_sdk_sagemaker.types.cache_hit_result.deserialize_aws_json_1_1(
                data["CacheHitResult"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "Metadata" in data:
        import aws_sdk_sagemaker.types.pipeline_execution_step_metadata

        out["metadata"] = (
            aws_sdk_sagemaker.types.pipeline_execution_step_metadata.deserialize_aws_json_1_1(
                data["Metadata"]
            )
        )
    if "AttemptCount" in data:
        out["attempt_count"] = data["AttemptCount"]
    if "SelectiveExecutionResult" in data:
        import aws_sdk_sagemaker.types.selective_execution_result

        out["selective_execution_result"] = (
            aws_sdk_sagemaker.types.selective_execution_result.deserialize_aws_json_1_1(
                data["SelectiveExecutionResult"]
            )
        )
    return out
