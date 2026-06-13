"""Generated from Smithy shape ``com.amazonaws.omics#DeleteSequenceStoreRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.sequence_store_id


class DeleteSequenceStoreRequest(TypedDict):
    id: "aws_sdk_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The sequence store's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSequenceStoreRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSequenceStoreRequest:
    out: DeleteSequenceStoreRequest = {}  # type: ignore[typeddict-item]
    return out
