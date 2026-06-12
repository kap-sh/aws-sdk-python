"""Generated from Smithy shape ``com.amazonaws.eventbridge#BatchParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.batch_array_properties
    import aws_sdk_eventbridge.types.batch_retry_strategy
    import aws_sdk_eventbridge.types.string


class BatchParameters(TypedDict):
    job_definition: "aws_sdk_eventbridge.types.string.String"
    """<p>The ARN or name of the job definition to use if the event target is an Batch job. This job definition must already exist.</p>"""
    job_name: "aws_sdk_eventbridge.types.string.String"
    """<p>The name to use for this execution of the job, if the target is an Batch job.</p>"""
    array_properties: NotRequired[
        "aws_sdk_eventbridge.types.batch_array_properties.BatchArrayProperties"
    ]
    """<p>The array properties for the submitted job, such as the size of the array. The array size can be between 2 and 10,000. If you specify array properties for a job, it becomes an array job. This parameter is used only if the target is an Batch job.</p>"""
    retry_strategy: NotRequired[
        "aws_sdk_eventbridge.types.batch_retry_strategy.BatchRetryStrategy"
    ]
    """<p>The retry strategy to use for failed jobs, if the target is an Batch job. The retry strategy is the number of times to retry the failed job execution. Valid values are 1–10. When you specify a retry strategy here, it overrides the retry strategy defined in the job definition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchParameters) -> dict:
    out: dict = {}
    out["JobDefinition"] = value["job_definition"]
    out["JobName"] = value["job_name"]
    if "array_properties" in value:
        import aws_sdk_eventbridge.types.batch_array_properties

        out["ArrayProperties"] = (
            aws_sdk_eventbridge.types.batch_array_properties.serialize_aws_json_1_1(
                value["array_properties"]
            )
        )
    if "retry_strategy" in value:
        import aws_sdk_eventbridge.types.batch_retry_strategy

        out["RetryStrategy"] = (
            aws_sdk_eventbridge.types.batch_retry_strategy.serialize_aws_json_1_1(
                value["retry_strategy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchParameters:
    out: BatchParameters = {}  # type: ignore[typeddict-item]
    if "JobDefinition" in data:
        out["job_definition"] = data["JobDefinition"]
    else:
        raise DeserializationError("BatchParameters.job_definition required")
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    else:
        raise DeserializationError("BatchParameters.job_name required")
    if "ArrayProperties" in data:
        import aws_sdk_eventbridge.types.batch_array_properties

        out["array_properties"] = (
            aws_sdk_eventbridge.types.batch_array_properties.deserialize_aws_json_1_1(
                data["ArrayProperties"]
            )
        )
    if "RetryStrategy" in data:
        import aws_sdk_eventbridge.types.batch_retry_strategy

        out["retry_strategy"] = (
            aws_sdk_eventbridge.types.batch_retry_strategy.deserialize_aws_json_1_1(
                data["RetryStrategy"]
            )
        )
    return out
