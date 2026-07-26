"""Generated from Smithy shape ``com.amazonaws.inspector2#SendCisSessionHealthResponse``."""

from typing_extensions import TypedDict


class SendCisSessionHealthResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: SendCisSessionHealthResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> SendCisSessionHealthResponse:
    out: SendCisSessionHealthResponse = {}  # type: ignore[typeddict-item]
    return out
