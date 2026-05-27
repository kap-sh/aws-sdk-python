"""Generated from Smithy shape ``com.amazonaws.lambda#StepFailedDetails``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.event_error
    import aws_sdk_lambda.types.retry_details


class StepFailedDetails(TypedDict):
    error: "aws_sdk_lambda.types.event_error.EventError"
    """<p>Details about the step failure.</p>"""
    retry_details: "aws_sdk_lambda.types.retry_details.RetryDetails"
    """<p>Information about retry attempts for this step operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StepFailedDetails) -> dict:
    out: dict = {}
    import aws_sdk_lambda.types.event_error

    out["Error"] = aws_sdk_lambda.types.event_error.serialize_json(value["error"])
    import aws_sdk_lambda.types.retry_details

    out["RetryDetails"] = aws_sdk_lambda.types.retry_details.serialize_json(
        value["retry_details"]
    )
    return out


def deserialize_json(data: dict) -> StepFailedDetails:
    out: StepFailedDetails = {}  # type: ignore[typeddict-item]
    if "Error" in data:
        import aws_sdk_lambda.types.event_error

        out["error"] = aws_sdk_lambda.types.event_error.deserialize_json(data["Error"])
    else:
        raise DeserializationError("StepFailedDetails.error required")
    if "RetryDetails" in data:
        import aws_sdk_lambda.types.retry_details

        out["retry_details"] = aws_sdk_lambda.types.retry_details.deserialize_json(
            data["RetryDetails"]
        )
    else:
        raise DeserializationError("StepFailedDetails.retry_details required")
    return out
