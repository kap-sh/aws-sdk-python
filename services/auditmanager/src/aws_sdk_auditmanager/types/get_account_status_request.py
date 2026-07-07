"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetAccountStatusRequest``."""

from typing_extensions import TypedDict


class GetAccountStatusRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: GetAccountStatusRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAccountStatusRequest:
    out: GetAccountStatusRequest = {}  # type: ignore[typeddict-item]
    return out
