"""Generated from Smithy shape ``com.amazonaws.connect#CompleteAttachedFileUploadResponse``."""

from typing_extensions import TypedDict


class CompleteAttachedFileUploadResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: CompleteAttachedFileUploadResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CompleteAttachedFileUploadResponse:
    out: CompleteAttachedFileUploadResponse = {}  # type: ignore[typeddict-item]
    return out
