"""Generated from Smithy shape ``com.amazonaws.lambda#InvocationCompletedDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.event_error
    import aws_sdk_lambda.types.execution_timestamp
    import aws_sdk_lambda.types.string


class InvocationCompletedDetails(TypedDict):
    start_timestamp: "aws_sdk_lambda.types.execution_timestamp.ExecutionTimestamp"
    r"""<p>The date and time when the invocation started, in <a href=\"https://www.w3.org/TR/NOTE-datetime\">ISO-8601 format</a> (YYYY-MM-DDThh:mm:ss.sTZD).</p>"""
    end_timestamp: "aws_sdk_lambda.types.execution_timestamp.ExecutionTimestamp"
    r"""<p>The date and time when the invocation ended, in <a href=\"https://www.w3.org/TR/NOTE-datetime\">ISO-8601 format</a> (YYYY-MM-DDThh:mm:ss.sTZD).</p>"""
    request_id: "aws_sdk_lambda.types.string.String"
    """<p>The request ID for the invocation.</p>"""
    error: NotRequired["aws_sdk_lambda.types.event_error.EventError"]
    """<p>Details about the invocation failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvocationCompletedDetails) -> dict:
    out: dict = {}
    import aws_sdk_lambda.types.execution_timestamp

    out["StartTimestamp"] = aws_sdk_lambda.types.execution_timestamp.serialize_json(
        value["start_timestamp"]
    )
    import aws_sdk_lambda.types.execution_timestamp

    out["EndTimestamp"] = aws_sdk_lambda.types.execution_timestamp.serialize_json(
        value["end_timestamp"]
    )
    out["RequestId"] = value["request_id"]
    if "error" in value:
        import aws_sdk_lambda.types.event_error

        out["Error"] = aws_sdk_lambda.types.event_error.serialize_json(value["error"])
    return out


def deserialize_json(data: dict) -> InvocationCompletedDetails:
    out: InvocationCompletedDetails = {}  # type: ignore[typeddict-item]
    if "StartTimestamp" in data:
        import aws_sdk_lambda.types.execution_timestamp

        out["start_timestamp"] = (
            aws_sdk_lambda.types.execution_timestamp.deserialize_json(
                data["StartTimestamp"]
            )
        )
    else:
        raise DeserializationError(
            "InvocationCompletedDetails.start_timestamp required"
        )
    if "EndTimestamp" in data:
        import aws_sdk_lambda.types.execution_timestamp

        out["end_timestamp"] = (
            aws_sdk_lambda.types.execution_timestamp.deserialize_json(
                data["EndTimestamp"]
            )
        )
    else:
        raise DeserializationError("InvocationCompletedDetails.end_timestamp required")
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    else:
        raise DeserializationError("InvocationCompletedDetails.request_id required")
    if "Error" in data:
        import aws_sdk_lambda.types.event_error

        out["error"] = aws_sdk_lambda.types.event_error.deserialize_json(data["Error"])
    return out
