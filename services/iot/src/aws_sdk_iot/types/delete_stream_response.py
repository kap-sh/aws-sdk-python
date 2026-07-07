"""Generated from Smithy shape ``com.amazonaws.iot#DeleteStreamResponse``."""

from typing_extensions import TypedDict


class DeleteStreamResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeleteStreamResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteStreamResponse:
    out: DeleteStreamResponse = {}  # type: ignore[typeddict-item]
    return out
