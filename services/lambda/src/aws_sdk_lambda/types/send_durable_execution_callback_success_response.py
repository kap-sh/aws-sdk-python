"""Generated from Smithy shape ``com.amazonaws.lambda#SendDurableExecutionCallbackSuccessResponse``."""

from typing import TypedDict


class SendDurableExecutionCallbackSuccessResponse(TypedDict):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: SendDurableExecutionCallbackSuccessResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> SendDurableExecutionCallbackSuccessResponse:
    out: SendDurableExecutionCallbackSuccessResponse = {}  # type: ignore[typeddict-item]
    return out
