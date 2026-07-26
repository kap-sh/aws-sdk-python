"""Generated from Smithy shape ``com.amazonaws.omics#GetReferenceStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_omics.types.reference_store_id


class GetReferenceStoreRequest(TypedDict, closed=True):
    id: "capo_omics.types.reference_store_id.ReferenceStoreId"
    """<p>The store's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReferenceStoreRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetReferenceStoreRequest:
    out: GetReferenceStoreRequest = {}  # type: ignore[typeddict-item]
    return out
