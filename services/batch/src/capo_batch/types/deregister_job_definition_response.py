"""Generated from Smithy shape ``com.amazonaws.batch#DeregisterJobDefinitionResponse``."""

from typing_extensions import TypedDict


class DeregisterJobDefinitionResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterJobDefinitionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeregisterJobDefinitionResponse:
    out: DeregisterJobDefinitionResponse = {}  # type: ignore[typeddict-item]
    return out
