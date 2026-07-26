"""Generated from Smithy shape ``com.amazonaws.lambda#SendDurableExecutionCallbackFailureResponse``."""

from typing_extensions import TypedDict


class SendDurableExecutionCallbackFailureResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: SendDurableExecutionCallbackFailureResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> SendDurableExecutionCallbackFailureResponse:
    out: SendDurableExecutionCallbackFailureResponse = {}  # type: ignore[typeddict-item]
    return out
