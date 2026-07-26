"""Generated from Smithy shape ``com.amazonaws.omics#CancelAnnotationImportResponse``."""

from typing_extensions import TypedDict


class CancelAnnotationImportResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: CancelAnnotationImportResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelAnnotationImportResponse:
    out: CancelAnnotationImportResponse = {}  # type: ignore[typeddict-item]
    return out
