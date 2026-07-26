"""Generated from Smithy shape ``com.amazonaws.connect#PauseContactResponse``."""

from typing_extensions import TypedDict


class PauseContactResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: PauseContactResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PauseContactResponse:
    out: PauseContactResponse = {}  # type: ignore[typeddict-item]
    return out
