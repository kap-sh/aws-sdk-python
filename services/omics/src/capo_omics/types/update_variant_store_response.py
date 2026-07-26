"""Generated from Smithy shape ``com.amazonaws.omics#UpdateVariantStoreResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_omics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_omics.types.creation_time
    import capo_omics.types.description
    import capo_omics.types.reference_item
    import capo_omics.types.resource_id
    import capo_omics.types.store_status
    import capo_omics.types.update_time


class UpdateVariantStoreResponse(TypedDict, closed=True):
    id: "capo_omics.types.resource_id.ResourceId"
    """<p>The store's ID.</p>"""
    reference: "capo_omics.types.reference_item.ReferenceItem"
    """<p>The store's genome reference.</p>"""
    status: "capo_omics.types.store_status.StoreStatus"
    """<p>The store's status.</p>"""
    name: "str"
    """<p>The store's name.</p>"""
    description: "capo_omics.types.description.Description"
    """<p>The store's description.</p>"""
    creation_time: "capo_omics.types.creation_time.CreationTime"
    """<p>When the store was created.</p>"""
    update_time: "capo_omics.types.update_time.UpdateTime"
    """<p>When the store was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateVariantStoreResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_omics.types.reference_item

    out["reference"] = capo_omics.types.reference_item.serialize_json(
        value["reference"]
    )
    out["status"] = value["status"]
    out["name"] = value["name"]
    out["description"] = value["description"]
    import capo_omics.types.creation_time

    out["creationTime"] = capo_omics.types.creation_time.serialize_json(
        value["creation_time"]
    )
    import capo_omics.types.update_time

    out["updateTime"] = capo_omics.types.update_time.serialize_json(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> UpdateVariantStoreResponse:
    out: UpdateVariantStoreResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UpdateVariantStoreResponse.id required")
    if "reference" in data:
        import capo_omics.types.reference_item

        out["reference"] = capo_omics.types.reference_item.deserialize_json(
            data["reference"]
        )
    else:
        raise DeserializationError("UpdateVariantStoreResponse.reference required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("UpdateVariantStoreResponse.status required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateVariantStoreResponse.name required")
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError("UpdateVariantStoreResponse.description required")
    if "creationTime" in data:
        import capo_omics.types.creation_time

        out["creation_time"] = capo_omics.types.creation_time.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("UpdateVariantStoreResponse.creation_time required")
    if "updateTime" in data:
        import capo_omics.types.update_time

        out["update_time"] = capo_omics.types.update_time.deserialize_json(
            data["updateTime"]
        )
    else:
        raise DeserializationError("UpdateVariantStoreResponse.update_time required")
    return out
