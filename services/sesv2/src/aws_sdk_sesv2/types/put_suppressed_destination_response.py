"""Generated from Smithy shape ``com.amazonaws.sesv2#PutSuppressedDestinationResponse``."""

from typing_extensions import TypedDict


class PutSuppressedDestinationResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: PutSuppressedDestinationResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PutSuppressedDestinationResponse:
    out: PutSuppressedDestinationResponse = {}  # type: ignore[typeddict-item]
    return out
