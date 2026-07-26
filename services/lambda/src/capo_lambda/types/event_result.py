"""Generated from Smithy shape ``com.amazonaws.lambda#EventResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.operation_payload
    import capo_lambda.types.truncated


class EventResult(TypedDict, closed=True):
    payload: NotRequired["capo_lambda.types.operation_payload.OperationPayload"]
    """<p>The result payload.</p>"""
    truncated: NotRequired["capo_lambda.types.truncated.Truncated"]
    """<p>Indicates if the error payload was truncated due to size limits.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventResult) -> dict:
    out: dict = {}
    if "payload" in value:
        out["Payload"] = value["payload"]
    if "truncated" in value:
        out["Truncated"] = value["truncated"]
    return out


def deserialize_json(data: dict) -> EventResult:
    out: EventResult = {}  # type: ignore[typeddict-item]
    if "Payload" in data:
        out["payload"] = data["Payload"]
    if "Truncated" in data:
        out["truncated"] = data["Truncated"]
    return out
