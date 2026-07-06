"""Generated from Smithy shape ``com.amazonaws.mgn#InitializeServiceResponse``."""

from typing_extensions import TypedDict


class InitializeServiceResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: InitializeServiceResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> InitializeServiceResponse:
    out: InitializeServiceResponse = {}  # type: ignore[typeddict-item]
    return out
