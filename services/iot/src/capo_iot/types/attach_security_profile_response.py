"""Generated from Smithy shape ``com.amazonaws.iot#AttachSecurityProfileResponse``."""

from typing_extensions import TypedDict


class AttachSecurityProfileResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: AttachSecurityProfileResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AttachSecurityProfileResponse:
    out: AttachSecurityProfileResponse = {}  # type: ignore[typeddict-item]
    return out
