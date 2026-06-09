"""Generated from Smithy shape ``com.amazonaws.lambda#CallbackTimedOutDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.event_error


class CallbackTimedOutDetails(TypedDict):
    error: "aws_sdk_lambda.types.event_error.EventError"
    """<p>Details about the callback timeout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CallbackTimedOutDetails) -> dict:
    out: dict = {}
    import aws_sdk_lambda.types.event_error

    out["Error"] = aws_sdk_lambda.types.event_error.serialize_json(value["error"])
    return out


def deserialize_json(data: dict) -> CallbackTimedOutDetails:
    out: CallbackTimedOutDetails = {}  # type: ignore[typeddict-item]
    if "Error" in data:
        import aws_sdk_lambda.types.event_error

        out["error"] = aws_sdk_lambda.types.event_error.deserialize_json(data["Error"])
    else:
        raise DeserializationError("CallbackTimedOutDetails.error required")
    return out
