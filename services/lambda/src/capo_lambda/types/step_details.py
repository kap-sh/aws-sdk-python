"""Generated from Smithy shape ``com.amazonaws.lambda#StepDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.attempt_count
    import capo_lambda.types.error_object
    import capo_lambda.types.execution_timestamp
    import capo_lambda.types.operation_payload


class StepDetails(TypedDict, closed=True):
    attempt: "capo_lambda.types.attempt_count.AttemptCount"
    """<p>The current attempt number for this step.</p>"""
    next_attempt_timestamp: NotRequired[
        "capo_lambda.types.execution_timestamp.ExecutionTimestamp"
    ]
    r"""<p>The date and time when the next attempt is scheduled, in <a href=\"https://www.w3.org/TR/NOTE-datetime\">ISO-8601 format</a> (YYYY-MM-DDThh:mm:ss.sTZD). Only populated when the step is in a pending state.</p>"""
    result: NotRequired["capo_lambda.types.operation_payload.OperationPayload"]
    """<p>The JSON response payload from the step operation.</p>"""
    error: NotRequired["capo_lambda.types.error_object.ErrorObject"]
    """<p>Details about the step failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StepDetails) -> dict:
    out: dict = {}
    out["Attempt"] = value.get("attempt", 0)
    if "next_attempt_timestamp" in value:
        import capo_lambda.types.execution_timestamp

        out["NextAttemptTimestamp"] = (
            capo_lambda.types.execution_timestamp.serialize_json(
                value["next_attempt_timestamp"]
            )
        )
    if "result" in value:
        out["Result"] = value["result"]
    if "error" in value:
        import capo_lambda.types.error_object

        out["Error"] = capo_lambda.types.error_object.serialize_json(value["error"])
    return out


def deserialize_json(data: dict) -> StepDetails:
    out: StepDetails = {}  # type: ignore[typeddict-item]
    if "Attempt" in data:
        out["attempt"] = data["Attempt"]
    else:
        out["attempt"] = 0
    if "NextAttemptTimestamp" in data:
        import capo_lambda.types.execution_timestamp

        out["next_attempt_timestamp"] = (
            capo_lambda.types.execution_timestamp.deserialize_json(
                data["NextAttemptTimestamp"]
            )
        )
    if "Result" in data:
        out["result"] = data["Result"]
    if "Error" in data:
        import capo_lambda.types.error_object

        out["error"] = capo_lambda.types.error_object.deserialize_json(data["Error"])
    return out
