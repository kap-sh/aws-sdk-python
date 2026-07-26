"""Generated from Smithy shape ``com.amazonaws.omics#DeleteReferenceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_omics.types.reference_id
    import capo_omics.types.reference_store_id


class DeleteReferenceRequest(TypedDict, closed=True):
    id: "capo_omics.types.reference_id.ReferenceId"
    """<p>The reference's ID.</p>"""
    reference_store_id: "capo_omics.types.reference_store_id.ReferenceStoreId"
    """<p>The reference's store ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteReferenceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteReferenceRequest:
    out: DeleteReferenceRequest = {}  # type: ignore[typeddict-item]
    return out
