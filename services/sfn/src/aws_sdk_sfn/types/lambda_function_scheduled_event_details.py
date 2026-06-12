"""Generated from Smithy shape ``com.amazonaws.sfn#LambdaFunctionScheduledEventDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.arn
    import aws_sdk_sfn.types.history_event_execution_data_details
    import aws_sdk_sfn.types.sensitive_data
    import aws_sdk_sfn.types.task_credentials
    import aws_sdk_sfn.types.timeout_in_seconds


class LambdaFunctionScheduledEventDetails(TypedDict):
    resource: "aws_sdk_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the scheduled Lambda function.</p>"""
    input: NotRequired["aws_sdk_sfn.types.sensitive_data.SensitiveData"]
    """<p>The JSON data input to the Lambda function. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.</p>"""
    input_details: NotRequired[
        "aws_sdk_sfn.types.history_event_execution_data_details.HistoryEventExecutionDataDetails"
    ]
    """<p>Contains details about input for an execution history event.</p>"""
    timeout_in_seconds: NotRequired[
        "aws_sdk_sfn.types.timeout_in_seconds.TimeoutInSeconds"
    ]
    """<p>The maximum allowed duration of the Lambda function.</p>"""
    task_credentials: NotRequired["aws_sdk_sfn.types.task_credentials.TaskCredentials"]
    """<p>The credentials that Step Functions uses for the task.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaFunctionScheduledEventDetails) -> dict:
    out: dict = {}
    out["resource"] = value["resource"]
    if "input" in value:
        out["input"] = value["input"]
    if "input_details" in value:
        import aws_sdk_sfn.types.history_event_execution_data_details

        out["inputDetails"] = (
            aws_sdk_sfn.types.history_event_execution_data_details.serialize_aws_json_1_0(
                value["input_details"]
            )
        )
    if "timeout_in_seconds" in value:
        out["timeoutInSeconds"] = value["timeout_in_seconds"]
    if "task_credentials" in value:
        import aws_sdk_sfn.types.task_credentials

        out["taskCredentials"] = (
            aws_sdk_sfn.types.task_credentials.serialize_aws_json_1_0(
                value["task_credentials"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> LambdaFunctionScheduledEventDetails:
    out: LambdaFunctionScheduledEventDetails = {}  # type: ignore[typeddict-item]
    if "resource" in data:
        out["resource"] = data["resource"]
    else:
        raise DeserializationError(
            "LambdaFunctionScheduledEventDetails.resource required"
        )
    if "input" in data:
        out["input"] = data["input"]
    if "inputDetails" in data:
        import aws_sdk_sfn.types.history_event_execution_data_details

        out["input_details"] = (
            aws_sdk_sfn.types.history_event_execution_data_details.deserialize_aws_json_1_0(
                data["inputDetails"]
            )
        )
    if "timeoutInSeconds" in data:
        out["timeout_in_seconds"] = data["timeoutInSeconds"]
    if "taskCredentials" in data:
        import aws_sdk_sfn.types.task_credentials

        out["task_credentials"] = (
            aws_sdk_sfn.types.task_credentials.deserialize_aws_json_1_0(
                data["taskCredentials"]
            )
        )
    return out
