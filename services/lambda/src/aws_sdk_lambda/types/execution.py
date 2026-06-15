"""Generated from Smithy shape ``com.amazonaws.lambda#Execution``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.durable_execution_arn
    import aws_sdk_lambda.types.durable_execution_name
    import aws_sdk_lambda.types.execution_status
    import aws_sdk_lambda.types.execution_timestamp
    import aws_sdk_lambda.types.name_spaced_function_arn


class Execution(TypedDict):
    durable_execution_arn: (
        "aws_sdk_lambda.types.durable_execution_arn.DurableExecutionArn"
    )
    """<p>The Amazon Resource Name (ARN) of the durable execution, if this execution is a durable execution.</p>"""
    durable_execution_name: (
        "aws_sdk_lambda.types.durable_execution_name.DurableExecutionName"
    )
    """<p>The unique name of the durable execution, if one was provided when the execution was started.</p>"""
    function_arn: "aws_sdk_lambda.types.name_spaced_function_arn.NameSpacedFunctionArn"
    """<p>The Amazon Resource Name (ARN) of the Lambda function.</p>"""
    status: "aws_sdk_lambda.types.execution_status.ExecutionStatus"
    """<p>The current status of the durable execution.</p>"""
    start_timestamp: "aws_sdk_lambda.types.execution_timestamp.ExecutionTimestamp"
    r"""<p>The date and time when the durable execution started, in <a href=\"https://www.w3.org/TR/NOTE-datetime\">ISO-8601 format</a> (YYYY-MM-DDThh:mm:ss.sTZD).</p>"""
    end_timestamp: NotRequired[
        "aws_sdk_lambda.types.execution_timestamp.ExecutionTimestamp"
    ]
    r"""<p>The date and time when the durable execution ended, in <a href=\"https://www.w3.org/TR/NOTE-datetime\">ISO-8601 format</a> (YYYY-MM-DDThh:mm:ss.sTZD).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Execution) -> dict:
    out: dict = {}
    out["DurableExecutionArn"] = value["durable_execution_arn"]
    out["DurableExecutionName"] = value["durable_execution_name"]
    out["FunctionArn"] = value["function_arn"]
    import aws_sdk_lambda.types.execution_status

    out["Status"] = aws_sdk_lambda.types.execution_status.serialize_json(
        value["status"]
    )
    import aws_sdk_lambda.types.execution_timestamp

    out["StartTimestamp"] = aws_sdk_lambda.types.execution_timestamp.serialize_json(
        value["start_timestamp"]
    )
    if "end_timestamp" in value:
        import aws_sdk_lambda.types.execution_timestamp

        out["EndTimestamp"] = aws_sdk_lambda.types.execution_timestamp.serialize_json(
            value["end_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> Execution:
    out: Execution = {}  # type: ignore[typeddict-item]
    if "DurableExecutionArn" in data:
        out["durable_execution_arn"] = data["DurableExecutionArn"]
    else:
        raise DeserializationError("Execution.durable_execution_arn required")
    if "DurableExecutionName" in data:
        out["durable_execution_name"] = data["DurableExecutionName"]
    else:
        raise DeserializationError("Execution.durable_execution_name required")
    if "FunctionArn" in data:
        out["function_arn"] = data["FunctionArn"]
    else:
        raise DeserializationError("Execution.function_arn required")
    if "Status" in data:
        import aws_sdk_lambda.types.execution_status

        out["status"] = aws_sdk_lambda.types.execution_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("Execution.status required")
    if "StartTimestamp" in data:
        import aws_sdk_lambda.types.execution_timestamp

        out["start_timestamp"] = (
            aws_sdk_lambda.types.execution_timestamp.deserialize_json(
                data["StartTimestamp"]
            )
        )
    else:
        raise DeserializationError("Execution.start_timestamp required")
    if "EndTimestamp" in data:
        import aws_sdk_lambda.types.execution_timestamp

        out["end_timestamp"] = (
            aws_sdk_lambda.types.execution_timestamp.deserialize_json(
                data["EndTimestamp"]
            )
        )
    return out
