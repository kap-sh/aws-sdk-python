"""Generated from Smithy shape ``com.amazonaws.auditmanager#DeregisterAccountRequest``."""

from typing_extensions import TypedDict


class DeregisterAccountRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterAccountRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeregisterAccountRequest:
    out: DeregisterAccountRequest = {}  # type: ignore[typeddict-item]
    return out
