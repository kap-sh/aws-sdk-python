"""Generated from Smithy shape ``com.amazonaws.omics#GetSequenceStoreRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.sequence_store_id


class GetSequenceStoreRequest(TypedDict):
    id: "aws_sdk_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The store's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSequenceStoreRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSequenceStoreRequest:
    out: GetSequenceStoreRequest = {}  # type: ignore[typeddict-item]
    return out
