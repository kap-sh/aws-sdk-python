"""Generated from Smithy shape ``com.amazonaws.omics#DeleteVariantStoreResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_omics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_omics.types.store_status


class DeleteVariantStoreResponse(TypedDict, closed=True):
    status: "capo_omics.types.store_status.StoreStatus"
    """<p>The store's status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVariantStoreResponse) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> DeleteVariantStoreResponse:
    out: DeleteVariantStoreResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("DeleteVariantStoreResponse.status required")
    return out
