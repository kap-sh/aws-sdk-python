"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetLogLevelsByResourceTypesRequest``."""

from typing_extensions import TypedDict


class GetLogLevelsByResourceTypesRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: GetLogLevelsByResourceTypesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetLogLevelsByResourceTypesRequest:
    out: GetLogLevelsByResourceTypesRequest = {}  # type: ignore[typeddict-item]
    return out
