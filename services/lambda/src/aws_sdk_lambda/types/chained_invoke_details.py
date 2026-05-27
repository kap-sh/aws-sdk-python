"""Generated from Smithy shape ``com.amazonaws.lambda#ChainedInvokeDetails``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.error_object
    import aws_sdk_lambda.types.operation_payload


class ChainedInvokeDetails(TypedDict):
    result: NotRequired["aws_sdk_lambda.types.operation_payload.OperationPayload"]
    """<p>The response payload from the chained invocation.</p>"""
    error: NotRequired["aws_sdk_lambda.types.error_object.ErrorObject"]
    """<p>Details about the chained invocation failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChainedInvokeDetails) -> dict:
    out: dict = {}
    if "result" in value:
        out["Result"] = value["result"]
    if "error" in value:
        import aws_sdk_lambda.types.error_object

        out["Error"] = aws_sdk_lambda.types.error_object.serialize_json(value["error"])
    return out


def deserialize_json(data: dict) -> ChainedInvokeDetails:
    out: ChainedInvokeDetails = {}  # type: ignore[typeddict-item]
    if "Result" in data:
        out["result"] = data["Result"]
    if "Error" in data:
        import aws_sdk_lambda.types.error_object

        out["error"] = aws_sdk_lambda.types.error_object.deserialize_json(data["Error"])
    return out
