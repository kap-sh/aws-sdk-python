"""Generated from Smithy shape ``com.amazonaws.greengrassv2#GetServiceRoleForAccountRequest``."""

from typing_extensions import TypedDict


class GetServiceRoleForAccountRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceRoleForAccountRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetServiceRoleForAccountRequest:
    out: GetServiceRoleForAccountRequest = {}  # type: ignore[typeddict-item]
    return out
