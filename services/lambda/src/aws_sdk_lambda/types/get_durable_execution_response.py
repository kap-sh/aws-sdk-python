"""Generated from Smithy shape ``com.amazonaws.lambda#GetDurableExecutionResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.durable_execution_arn
    import aws_sdk_lambda.types.durable_execution_name
    import aws_sdk_lambda.types.error_object
    import aws_sdk_lambda.types.execution_status
    import aws_sdk_lambda.types.execution_timestamp
    import aws_sdk_lambda.types.input_payload
    import aws_sdk_lambda.types.name_spaced_function_arn
    import aws_sdk_lambda.types.output_payload
    import aws_sdk_lambda.types.trace_header
    import aws_sdk_lambda.types.version_with_latest_published


class GetDurableExecutionResponse(TypedDict):
    durable_execution_arn: (
        "aws_sdk_lambda.types.durable_execution_arn.DurableExecutionArn"
    )
    """<p>The Amazon Resource Name (ARN) of the durable execution.</p>"""
    durable_execution_name: (
        "aws_sdk_lambda.types.durable_execution_name.DurableExecutionName"
    )
    """<p>The name of the durable execution. This is either the name you provided when invoking the function, or a system-generated unique identifier if no name was provided.</p>"""
    function_arn: "aws_sdk_lambda.types.name_spaced_function_arn.NameSpacedFunctionArn"
    """<p>The Amazon Resource Name (ARN) of the Lambda function that was invoked to start this durable execution.</p>"""
    input_payload: NotRequired["aws_sdk_lambda.types.input_payload.InputPayload"]
    """<p>The JSON input payload that was provided when the durable execution was started. For asynchronous invocations, this is limited to 256 KB. For synchronous invocations, this can be up to 6 MB.</p>"""
    result: NotRequired["aws_sdk_lambda.types.output_payload.OutputPayload"]
    """<p>The JSON result returned by the durable execution if it completed successfully. This field is only present when the execution status is <code>SUCCEEDED</code>. The result is limited to 256 KB.</p>"""
    error: NotRequired["aws_sdk_lambda.types.error_object.ErrorObject"]
    """<p>Error information if the durable execution failed. This field is only present when the execution status is <code>FAILED</code>, <code>TIMED_OUT</code>, or <code>STOPPED</code>. The combined size of all error fields is limited to 256 KB.</p>"""
    start_timestamp: "aws_sdk_lambda.types.execution_timestamp.ExecutionTimestamp"
    """<p>The date and time when the durable execution started, in Unix timestamp format.</p>"""
    status: "aws_sdk_lambda.types.execution_status.ExecutionStatus"
    """<p>The current status of the durable execution. Valid values are <code>RUNNING</code>, <code>SUCCEEDED</code>, <code>FAILED</code>, <code>TIMED_OUT</code>, and <code>STOPPED</code>.</p>"""
    end_timestamp: NotRequired[
        "aws_sdk_lambda.types.execution_timestamp.ExecutionTimestamp"
    ]
    """<p>The date and time when the durable execution ended, in Unix timestamp format. This field is only present if the execution has completed (status is <code>SUCCEEDED</code>, <code>FAILED</code>, <code>TIMED_OUT</code>, or <code>STOPPED</code>).</p>"""
    version: NotRequired[
        "aws_sdk_lambda.types.version_with_latest_published.VersionWithLatestPublished"
    ]
    """<p>The version of the Lambda function that was invoked for this durable execution. This ensures that all replays during the execution use the same function version.</p>"""
    trace_header: NotRequired["aws_sdk_lambda.types.trace_header.TraceHeader"]
    """<p>The trace headers associated with the durable execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDurableExecutionResponse) -> dict:
    out: dict = {}
    out["DurableExecutionArn"] = value["durable_execution_arn"]
    out["DurableExecutionName"] = value["durable_execution_name"]
    out["FunctionArn"] = value["function_arn"]
    if "input_payload" in value:
        out["InputPayload"] = value["input_payload"]
    if "result" in value:
        out["Result"] = value["result"]
    if "error" in value:
        import aws_sdk_lambda.types.error_object

        out["Error"] = aws_sdk_lambda.types.error_object.serialize_json(value["error"])
    import aws_sdk_lambda.types.execution_timestamp

    out["StartTimestamp"] = aws_sdk_lambda.types.execution_timestamp.serialize_json(
        value["start_timestamp"]
    )
    import aws_sdk_lambda.types.execution_status

    out["Status"] = aws_sdk_lambda.types.execution_status.serialize_json(
        value["status"]
    )
    if "end_timestamp" in value:
        import aws_sdk_lambda.types.execution_timestamp

        out["EndTimestamp"] = aws_sdk_lambda.types.execution_timestamp.serialize_json(
            value["end_timestamp"]
        )
    if "version" in value:
        out["Version"] = value["version"]
    if "trace_header" in value:
        import aws_sdk_lambda.types.trace_header

        out["TraceHeader"] = aws_sdk_lambda.types.trace_header.serialize_json(
            value["trace_header"]
        )
    return out


def deserialize_json(data: dict) -> GetDurableExecutionResponse:
    out: GetDurableExecutionResponse = {}  # type: ignore[typeddict-item]
    if "DurableExecutionArn" in data:
        out["durable_execution_arn"] = data["DurableExecutionArn"]
    else:
        raise DeserializationError(
            "GetDurableExecutionResponse.durable_execution_arn required"
        )
    if "DurableExecutionName" in data:
        out["durable_execution_name"] = data["DurableExecutionName"]
    else:
        raise DeserializationError(
            "GetDurableExecutionResponse.durable_execution_name required"
        )
    if "FunctionArn" in data:
        out["function_arn"] = data["FunctionArn"]
    else:
        raise DeserializationError("GetDurableExecutionResponse.function_arn required")
    if "InputPayload" in data:
        out["input_payload"] = data["InputPayload"]
    if "Result" in data:
        out["result"] = data["Result"]
    if "Error" in data:
        import aws_sdk_lambda.types.error_object

        out["error"] = aws_sdk_lambda.types.error_object.deserialize_json(data["Error"])
    if "StartTimestamp" in data:
        import aws_sdk_lambda.types.execution_timestamp

        out["start_timestamp"] = (
            aws_sdk_lambda.types.execution_timestamp.deserialize_json(
                data["StartTimestamp"]
            )
        )
    else:
        raise DeserializationError(
            "GetDurableExecutionResponse.start_timestamp required"
        )
    if "Status" in data:
        import aws_sdk_lambda.types.execution_status

        out["status"] = aws_sdk_lambda.types.execution_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("GetDurableExecutionResponse.status required")
    if "EndTimestamp" in data:
        import aws_sdk_lambda.types.execution_timestamp

        out["end_timestamp"] = (
            aws_sdk_lambda.types.execution_timestamp.deserialize_json(
                data["EndTimestamp"]
            )
        )
    if "Version" in data:
        out["version"] = data["Version"]
    if "TraceHeader" in data:
        import aws_sdk_lambda.types.trace_header

        out["trace_header"] = aws_sdk_lambda.types.trace_header.deserialize_json(
            data["TraceHeader"]
        )
    return out
