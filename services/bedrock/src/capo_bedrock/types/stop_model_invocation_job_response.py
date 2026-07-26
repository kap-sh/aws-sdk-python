"""Generated from Smithy shape ``com.amazonaws.bedrock#StopModelInvocationJobResponse``."""

from typing_extensions import TypedDict


class StopModelInvocationJobResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: StopModelInvocationJobResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopModelInvocationJobResponse:
    out: StopModelInvocationJobResponse = {}  # type: ignore[typeddict-item]
    return out
