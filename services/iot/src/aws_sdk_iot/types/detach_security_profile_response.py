"""Generated from Smithy shape ``com.amazonaws.iot#DetachSecurityProfileResponse``."""

from typing_extensions import TypedDict


class DetachSecurityProfileResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DetachSecurityProfileResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DetachSecurityProfileResponse:
    out: DetachSecurityProfileResponse = {}  # type: ignore[typeddict-item]
    return out
