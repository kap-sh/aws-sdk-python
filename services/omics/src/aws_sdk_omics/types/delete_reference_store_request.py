"""Generated from Smithy shape ``com.amazonaws.omics#DeleteReferenceStoreRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.reference_store_id


class DeleteReferenceStoreRequest(TypedDict):
    id: "aws_sdk_omics.types.reference_store_id.ReferenceStoreId"
    """<p>The store's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteReferenceStoreRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteReferenceStoreRequest:
    out: DeleteReferenceStoreRequest = {}  # type: ignore[typeddict-item]
    return out
