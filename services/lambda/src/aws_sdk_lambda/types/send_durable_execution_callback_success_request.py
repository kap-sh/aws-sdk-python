"""Generated from Smithy shape ``com.amazonaws.lambda#SendDurableExecutionCallbackSuccessRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.binary_operation_payload
    import aws_sdk_lambda.types.callback_id


class SendDurableExecutionCallbackSuccessRequest(TypedDict):
    callback_id: "aws_sdk_lambda.types.callback_id.CallbackId"
    """<p>The unique identifier for the callback operation.</p>"""
    result: NotRequired[
        "aws_sdk_lambda.types.binary_operation_payload.BinaryOperationPayload"
    ]
    """<p>The result data from the successful callback operation. Maximum size is 256 KB.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendDurableExecutionCallbackSuccessRequest) -> dict:
    out: dict = {}
    if "result" in value:
        import aws_sdk_lambda.types.binary_operation_payload

        out["Result"] = aws_sdk_lambda.types.binary_operation_payload.serialize_json(
            value["result"]
        )
    return out


def deserialize_json(data: dict) -> SendDurableExecutionCallbackSuccessRequest:
    out: SendDurableExecutionCallbackSuccessRequest = {}  # type: ignore[typeddict-item]
    if "Result" in data:
        import aws_sdk_lambda.types.binary_operation_payload

        out["result"] = aws_sdk_lambda.types.binary_operation_payload.deserialize_json(
            data["Result"]
        )
    return out
