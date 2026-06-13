"""Generated from Smithy shape ``com.amazonaws.omics#GetVariantStoreRequest``."""

from typing import TypedDict


class GetVariantStoreRequest(TypedDict):
    name: "str"
    """<p>The store's name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVariantStoreRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetVariantStoreRequest:
    out: GetVariantStoreRequest = {}  # type: ignore[typeddict-item]
    return out
