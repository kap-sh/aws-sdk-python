"""Generated from Smithy shape ``com.amazonaws.mpa#CancelSessionResponse``."""

from typing_extensions import TypedDict


class CancelSessionResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: CancelSessionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelSessionResponse:
    out: CancelSessionResponse = {}  # type: ignore[typeddict-item]
    return out
