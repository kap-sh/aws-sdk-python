"""Generated from Smithy shape ``com.amazonaws.omics#GetReferenceMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_omics.types.reference_id
    import capo_omics.types.reference_store_id


class GetReferenceMetadataRequest(TypedDict, closed=True):
    id: "capo_omics.types.reference_id.ReferenceId"
    """<p>The reference's ID.</p>"""
    reference_store_id: "capo_omics.types.reference_store_id.ReferenceStoreId"
    """<p>The reference's reference store ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReferenceMetadataRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetReferenceMetadataRequest:
    out: GetReferenceMetadataRequest = {}  # type: ignore[typeddict-item]
    return out
