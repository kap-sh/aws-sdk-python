"""Generated from Smithy shape ``com.amazonaws.securityhub#GetAdministratorAccountRequest``."""

from typing_extensions import TypedDict


class GetAdministratorAccountRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: GetAdministratorAccountRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAdministratorAccountRequest:
    out: GetAdministratorAccountRequest = {}  # type: ignore[typeddict-item]
    return out
