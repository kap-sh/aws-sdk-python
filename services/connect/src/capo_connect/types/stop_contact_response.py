"""Generated from Smithy shape ``com.amazonaws.connect#StopContactResponse``."""

from typing_extensions import TypedDict


class StopContactResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: StopContactResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopContactResponse:
    out: StopContactResponse = {}  # type: ignore[typeddict-item]
    return out
