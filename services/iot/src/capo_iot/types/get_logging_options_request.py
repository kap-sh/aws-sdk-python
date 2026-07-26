"""Generated from Smithy shape ``com.amazonaws.iot#GetLoggingOptionsRequest``."""

from typing_extensions import TypedDict


class GetLoggingOptionsRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: GetLoggingOptionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetLoggingOptionsRequest:
    out: GetLoggingOptionsRequest = {}  # type: ignore[typeddict-item]
    return out
