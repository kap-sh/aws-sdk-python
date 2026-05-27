"""Generated from Smithy shape ``com.amazonaws.lambda#ExecutionDetails``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.input_payload


class ExecutionDetails(TypedDict):
    input_payload: NotRequired["aws_sdk_lambda.types.input_payload.InputPayload"]
    """<p>The original input payload provided for the durable execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionDetails) -> dict:
    out: dict = {}
    if "input_payload" in value:
        out["InputPayload"] = value["input_payload"]
    return out


def deserialize_json(data: dict) -> ExecutionDetails:
    out: ExecutionDetails = {}  # type: ignore[typeddict-item]
    if "InputPayload" in data:
        out["input_payload"] = data["InputPayload"]
    return out
