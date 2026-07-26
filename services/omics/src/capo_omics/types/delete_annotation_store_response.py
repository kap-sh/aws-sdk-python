"""Generated from Smithy shape ``com.amazonaws.omics#DeleteAnnotationStoreResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_omics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_omics.types.store_status


class DeleteAnnotationStoreResponse(TypedDict, closed=True):
    status: "capo_omics.types.store_status.StoreStatus"
    """<p>The store's status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAnnotationStoreResponse) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> DeleteAnnotationStoreResponse:
    out: DeleteAnnotationStoreResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("DeleteAnnotationStoreResponse.status required")
    return out
