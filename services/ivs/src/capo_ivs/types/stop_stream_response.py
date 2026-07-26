"""Generated from Smithy shape ``com.amazonaws.ivs#StopStreamResponse``."""

from typing_extensions import TypedDict


class StopStreamResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: StopStreamResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopStreamResponse:
    out: StopStreamResponse = {}  # type: ignore[typeddict-item]
    return out
