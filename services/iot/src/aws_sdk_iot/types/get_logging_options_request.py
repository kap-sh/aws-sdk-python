"""Generated from Smithy shape ``com.amazonaws.iot#GetLoggingOptionsRequest``."""

from typing import TypedDict


class GetLoggingOptionsRequest(TypedDict):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: GetLoggingOptionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetLoggingOptionsRequest:
    out: GetLoggingOptionsRequest = {}  # type: ignore[typeddict-item]
    return out
