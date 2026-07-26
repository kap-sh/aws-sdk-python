"""Generated from Smithy shape ``com.amazonaws.mgn#InitializeServiceRequest``."""

from typing_extensions import TypedDict


class InitializeServiceRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: InitializeServiceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> InitializeServiceRequest:
    out: InitializeServiceRequest = {}  # type: ignore[typeddict-item]
    return out
