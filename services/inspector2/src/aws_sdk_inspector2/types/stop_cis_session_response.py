"""Generated from Smithy shape ``com.amazonaws.inspector2#StopCisSessionResponse``."""

from typing_extensions import TypedDict


class StopCisSessionResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: StopCisSessionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopCisSessionResponse:
    out: StopCisSessionResponse = {}  # type: ignore[typeddict-item]
    return out
