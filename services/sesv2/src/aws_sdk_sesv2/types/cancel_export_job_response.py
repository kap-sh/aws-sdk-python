"""Generated from Smithy shape ``com.amazonaws.sesv2#CancelExportJobResponse``."""

from typing_extensions import TypedDict


class CancelExportJobResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: CancelExportJobResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelExportJobResponse:
    out: CancelExportJobResponse = {}  # type: ignore[typeddict-item]
    return out
