"""Generated from Smithy shape ``com.amazonaws.connect#AssociateContactWithUserResponse``."""

from typing_extensions import TypedDict


class AssociateContactWithUserResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: AssociateContactWithUserResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AssociateContactWithUserResponse:
    out: AssociateContactWithUserResponse = {}  # type: ignore[typeddict-item]
    return out
