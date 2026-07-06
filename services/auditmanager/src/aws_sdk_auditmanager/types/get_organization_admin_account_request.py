"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetOrganizationAdminAccountRequest``."""

from typing_extensions import TypedDict


class GetOrganizationAdminAccountRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: GetOrganizationAdminAccountRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetOrganizationAdminAccountRequest:
    out: GetOrganizationAdminAccountRequest = {}  # type: ignore[typeddict-item]
    return out
