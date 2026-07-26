"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetServicesInScopeRequest``."""

from typing_extensions import TypedDict


class GetServicesInScopeRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: GetServicesInScopeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetServicesInScopeRequest:
    out: GetServicesInScopeRequest = {}  # type: ignore[typeddict-item]
    return out
