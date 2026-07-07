"""Generated from Smithy shape ``com.amazonaws.iot#AttachThingPrincipalResponse``."""

from typing_extensions import TypedDict


class AttachThingPrincipalResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: AttachThingPrincipalResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AttachThingPrincipalResponse:
    out: AttachThingPrincipalResponse = {}  # type: ignore[typeddict-item]
    return out
