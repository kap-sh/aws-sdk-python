"""Generated from Smithy shape ``com.amazonaws.omics#GetAnnotationStoreVersionRequest``."""

from typing import TypedDict


class GetAnnotationStoreVersionRequest(TypedDict):
    name: "str"
    """<p> The name given to an annotation store version to distinguish it from others. </p>"""
    version_name: "str"
    """<p> The name given to an annotation store version to distinguish it from others. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAnnotationStoreVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAnnotationStoreVersionRequest:
    out: GetAnnotationStoreVersionRequest = {}  # type: ignore[typeddict-item]
    return out
