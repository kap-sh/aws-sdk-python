"""Generated from Smithy shape ``com.amazonaws.appflow#UnregisterConnectorResponse``."""

from typing_extensions import TypedDict


class UnregisterConnectorResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: UnregisterConnectorResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UnregisterConnectorResponse:
    out: UnregisterConnectorResponse = {}  # type: ignore[typeddict-item]
    return out
