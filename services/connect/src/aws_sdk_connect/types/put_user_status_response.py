"""Generated from Smithy shape ``com.amazonaws.connect#PutUserStatusResponse``."""

from typing_extensions import TypedDict


class PutUserStatusResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: PutUserStatusResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PutUserStatusResponse:
    out: PutUserStatusResponse = {}  # type: ignore[typeddict-item]
    return out
