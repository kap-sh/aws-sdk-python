"""Generated from Smithy shape ``com.amazonaws.iot#DetachThingPrincipalResponse``."""

from typing_extensions import TypedDict


class DetachThingPrincipalResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DetachThingPrincipalResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DetachThingPrincipalResponse:
    out: DetachThingPrincipalResponse = {}  # type: ignore[typeddict-item]
    return out
