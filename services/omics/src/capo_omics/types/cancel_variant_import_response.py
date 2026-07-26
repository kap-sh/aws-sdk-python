"""Generated from Smithy shape ``com.amazonaws.omics#CancelVariantImportResponse``."""

from typing_extensions import TypedDict


class CancelVariantImportResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: CancelVariantImportResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelVariantImportResponse:
    out: CancelVariantImportResponse = {}  # type: ignore[typeddict-item]
    return out
