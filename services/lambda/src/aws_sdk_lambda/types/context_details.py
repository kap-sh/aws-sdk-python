"""Generated from Smithy shape ``com.amazonaws.lambda#ContextDetails``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.error_object
    import aws_sdk_lambda.types.operation_payload
    import aws_sdk_lambda.types.replay_children


class ContextDetails(TypedDict):
    replay_children: NotRequired["aws_sdk_lambda.types.replay_children.ReplayChildren"]
    """<p>Whether the state data of child operations of this completed context should be included in the invoke payload and <code>GetDurableExecutionState</code> response.</p>"""
    result: NotRequired["aws_sdk_lambda.types.operation_payload.OperationPayload"]
    """<p>The response payload from the context.</p>"""
    error: NotRequired["aws_sdk_lambda.types.error_object.ErrorObject"]
    """<p>Details about the context failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContextDetails) -> dict:
    out: dict = {}
    if "replay_children" in value:
        out["ReplayChildren"] = value["replay_children"]
    if "result" in value:
        out["Result"] = value["result"]
    if "error" in value:
        import aws_sdk_lambda.types.error_object

        out["Error"] = aws_sdk_lambda.types.error_object.serialize_json(value["error"])
    return out


def deserialize_json(data: dict) -> ContextDetails:
    out: ContextDetails = {}  # type: ignore[typeddict-item]
    if "ReplayChildren" in data:
        out["replay_children"] = data["ReplayChildren"]
    if "Result" in data:
        out["result"] = data["Result"]
    if "Error" in data:
        import aws_sdk_lambda.types.error_object

        out["error"] = aws_sdk_lambda.types.error_object.deserialize_json(data["Error"])
    return out
