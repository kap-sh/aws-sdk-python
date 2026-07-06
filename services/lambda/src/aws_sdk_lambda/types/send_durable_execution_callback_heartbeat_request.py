"""Generated from Smithy shape ``com.amazonaws.lambda#SendDurableExecutionCallbackHeartbeatRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.callback_id


class SendDurableExecutionCallbackHeartbeatRequest(TypedDict, closed=True):
    callback_id: "aws_sdk_lambda.types.callback_id.CallbackId"
    """<p>The unique identifier for the callback operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendDurableExecutionCallbackHeartbeatRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> SendDurableExecutionCallbackHeartbeatRequest:
    out: SendDurableExecutionCallbackHeartbeatRequest = {}  # type: ignore[typeddict-item]
    return out
