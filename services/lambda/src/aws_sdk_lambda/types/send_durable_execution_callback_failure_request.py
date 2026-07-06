"""Generated from Smithy shape ``com.amazonaws.lambda#SendDurableExecutionCallbackFailureRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.callback_id
    import aws_sdk_lambda.types.error_object


class SendDurableExecutionCallbackFailureRequest(TypedDict, closed=True):
    callback_id: "aws_sdk_lambda.types.callback_id.CallbackId"
    """<p>The unique identifier for the callback operation.</p>"""
    error: NotRequired["aws_sdk_lambda.types.error_object.ErrorObject"]
    """<p>Error details describing why the callback operation failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendDurableExecutionCallbackFailureRequest) -> dict:
    out: dict = {}
    if "error" in value:
        import aws_sdk_lambda.types.error_object

        out["Error"] = aws_sdk_lambda.types.error_object.serialize_json(value["error"])
    return out


def deserialize_json(data: dict) -> SendDurableExecutionCallbackFailureRequest:
    out: SendDurableExecutionCallbackFailureRequest = {}  # type: ignore[typeddict-item]
    if "Error" in data:
        import aws_sdk_lambda.types.error_object

        out["error"] = aws_sdk_lambda.types.error_object.deserialize_json(data["Error"])
    return out
