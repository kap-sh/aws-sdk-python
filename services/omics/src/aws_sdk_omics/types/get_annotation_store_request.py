"""Generated from Smithy shape ``com.amazonaws.omics#GetAnnotationStoreRequest``."""

from typing import TypedDict


class GetAnnotationStoreRequest(TypedDict):
    name: "str"
    """<p>The store's name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAnnotationStoreRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAnnotationStoreRequest:
    out: GetAnnotationStoreRequest = {}  # type: ignore[typeddict-item]
    return out
