"""Generated from Smithy shape ``com.amazonaws.omics#GetSequenceStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_omics.types.sequence_store_id


class GetSequenceStoreRequest(TypedDict, closed=True):
    id: "capo_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The store's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSequenceStoreRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSequenceStoreRequest:
    out: GetSequenceStoreRequest = {}  # type: ignore[typeddict-item]
    return out
