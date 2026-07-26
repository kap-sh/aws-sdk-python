"""Generated from Smithy shape ``com.amazonaws.iot#CancelAuditTaskResponse``."""

from typing_extensions import TypedDict


class CancelAuditTaskResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: CancelAuditTaskResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelAuditTaskResponse:
    out: CancelAuditTaskResponse = {}  # type: ignore[typeddict-item]
    return out
