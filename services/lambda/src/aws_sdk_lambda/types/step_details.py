"""Generated from Smithy shape ``com.amazonaws.lambda#StepDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.attempt_count
    import aws_sdk_lambda.types.error_object
    import aws_sdk_lambda.types.execution_timestamp
    import aws_sdk_lambda.types.operation_payload


class StepDetails(TypedDict):
    attempt: "aws_sdk_lambda.types.attempt_count.AttemptCount"
    """<p>The current attempt number for this step.</p>"""
    next_attempt_timestamp: NotRequired[
        "aws_sdk_lambda.types.execution_timestamp.ExecutionTimestamp"
    ]
    r"""<p>The date and time when the next attempt is scheduled, in <a href=\"https://www.w3.org/TR/NOTE-datetime\">ISO-8601 format</a> (YYYY-MM-DDThh:mm:ss.sTZD). Only populated when the step is in a pending state.</p>"""
    result: NotRequired["aws_sdk_lambda.types.operation_payload.OperationPayload"]
    """<p>The JSON response payload from the step operation.</p>"""
    error: NotRequired["aws_sdk_lambda.types.error_object.ErrorObject"]
    """<p>Details about the step failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StepDetails) -> dict:
    out: dict = {}
    out["Attempt"] = value.get("attempt", 0)
    if "next_attempt_timestamp" in value:
        import aws_sdk_lambda.types.execution_timestamp

        out["NextAttemptTimestamp"] = (
            aws_sdk_lambda.types.execution_timestamp.serialize_json(
                value["next_attempt_timestamp"]
            )
        )
    if "result" in value:
        out["Result"] = value["result"]
    if "error" in value:
        import aws_sdk_lambda.types.error_object

        out["Error"] = aws_sdk_lambda.types.error_object.serialize_json(value["error"])
    return out


def deserialize_json(data: dict) -> StepDetails:
    out: StepDetails = {}  # type: ignore[typeddict-item]
    if "Attempt" in data:
        out["attempt"] = data["Attempt"]
    else:
        out["attempt"] = 0
    if "NextAttemptTimestamp" in data:
        import aws_sdk_lambda.types.execution_timestamp

        out["next_attempt_timestamp"] = (
            aws_sdk_lambda.types.execution_timestamp.deserialize_json(
                data["NextAttemptTimestamp"]
            )
        )
    if "Result" in data:
        out["result"] = data["Result"]
    if "Error" in data:
        import aws_sdk_lambda.types.error_object

        out["error"] = aws_sdk_lambda.types.error_object.deserialize_json(data["Error"])
    return out
