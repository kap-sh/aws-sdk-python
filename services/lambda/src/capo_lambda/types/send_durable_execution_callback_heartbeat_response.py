"""Generated from Smithy shape ``com.amazonaws.lambda#SendDurableExecutionCallbackHeartbeatResponse``."""

from typing_extensions import TypedDict


class SendDurableExecutionCallbackHeartbeatResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: SendDurableExecutionCallbackHeartbeatResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> SendDurableExecutionCallbackHeartbeatResponse:
    out: SendDurableExecutionCallbackHeartbeatResponse = {}  # type: ignore[typeddict-item]
    return out
