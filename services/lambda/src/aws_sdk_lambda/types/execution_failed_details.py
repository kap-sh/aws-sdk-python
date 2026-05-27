"""Generated from Smithy shape ``com.amazonaws.lambda#ExecutionFailedDetails``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.event_error


class ExecutionFailedDetails(TypedDict):
    error: "aws_sdk_lambda.types.event_error.EventError"
    """<p>Details about the execution failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionFailedDetails) -> dict:
    out: dict = {}
    import aws_sdk_lambda.types.event_error

    out["Error"] = aws_sdk_lambda.types.event_error.serialize_json(value["error"])
    return out


def deserialize_json(data: dict) -> ExecutionFailedDetails:
    out: ExecutionFailedDetails = {}  # type: ignore[typeddict-item]
    if "Error" in data:
        import aws_sdk_lambda.types.event_error

        out["error"] = aws_sdk_lambda.types.event_error.deserialize_json(data["Error"])
    else:
        raise DeserializationError("ExecutionFailedDetails.error required")
    return out
