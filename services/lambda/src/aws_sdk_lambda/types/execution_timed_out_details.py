"""Generated from Smithy shape ``com.amazonaws.lambda#ExecutionTimedOutDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.event_error


class ExecutionTimedOutDetails(TypedDict):
    error: NotRequired["aws_sdk_lambda.types.event_error.EventError"]
    """<p>Details about the execution timeout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionTimedOutDetails) -> dict:
    out: dict = {}
    if "error" in value:
        import aws_sdk_lambda.types.event_error

        out["Error"] = aws_sdk_lambda.types.event_error.serialize_json(value["error"])
    return out


def deserialize_json(data: dict) -> ExecutionTimedOutDetails:
    out: ExecutionTimedOutDetails = {}  # type: ignore[typeddict-item]
    if "Error" in data:
        import aws_sdk_lambda.types.event_error

        out["error"] = aws_sdk_lambda.types.event_error.deserialize_json(data["Error"])
    return out
