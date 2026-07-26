"""Generated from Smithy shape ``com.amazonaws.omics#AnnotationStoreItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_omics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_omics.types.arn
    import capo_omics.types.creation_time
    import capo_omics.types.description
    import capo_omics.types.reference_item
    import capo_omics.types.resource_id
    import capo_omics.types.sse_config
    import capo_omics.types.status_message
    import capo_omics.types.store_format
    import capo_omics.types.store_status
    import capo_omics.types.update_time


class AnnotationStoreItem(TypedDict, closed=True):
    id: "capo_omics.types.resource_id.ResourceId"
    """<p>The store's ID.</p>"""
    reference: "capo_omics.types.reference_item.ReferenceItem"
    """<p>The store's genome reference.</p>"""
    status: "capo_omics.types.store_status.StoreStatus"
    """<p>The store's status.</p>"""
    store_arn: "capo_omics.types.arn.Arn"
    """<p>The store's ARN.</p>"""
    name: "str"
    """<p>The store's name.</p>"""
    store_format: "capo_omics.types.store_format.StoreFormat"
    """<p>The store's file format.</p>"""
    description: "capo_omics.types.description.Description"
    """<p>The store's description.</p>"""
    sse_config: "capo_omics.types.sse_config.SseConfig"
    """<p>The store's server-side encryption (SSE) settings.</p>"""
    creation_time: "capo_omics.types.creation_time.CreationTime"
    """<p>The store's creation time.</p>"""
    update_time: "capo_omics.types.update_time.UpdateTime"
    """<p>When the store was updated.</p>"""
    status_message: "capo_omics.types.status_message.StatusMessage"
    """<p>The store's status message.</p>"""
    store_size_bytes: "int"
    """<p>The store's size in bytes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnnotationStoreItem) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_omics.types.reference_item

    out["reference"] = capo_omics.types.reference_item.serialize_json(
        value["reference"]
    )
    out["status"] = value["status"]
    out["storeArn"] = value["store_arn"]
    out["name"] = value["name"]
    out["storeFormat"] = value["store_format"]
    out["description"] = value["description"]
    import capo_omics.types.sse_config

    out["sseConfig"] = capo_omics.types.sse_config.serialize_json(value["sse_config"])
    import capo_omics.types.creation_time

    out["creationTime"] = capo_omics.types.creation_time.serialize_json(
        value["creation_time"]
    )
    import capo_omics.types.update_time

    out["updateTime"] = capo_omics.types.update_time.serialize_json(
        value["update_time"]
    )
    out["statusMessage"] = value["status_message"]
    out["storeSizeBytes"] = value["store_size_bytes"]
    return out


def deserialize_json(data: dict) -> AnnotationStoreItem:
    out: AnnotationStoreItem = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("AnnotationStoreItem.id required")
    if "reference" in data:
        import capo_omics.types.reference_item

        out["reference"] = capo_omics.types.reference_item.deserialize_json(
            data["reference"]
        )
    else:
        raise DeserializationError("AnnotationStoreItem.reference required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("AnnotationStoreItem.status required")
    if "storeArn" in data:
        out["store_arn"] = data["storeArn"]
    else:
        raise DeserializationError("AnnotationStoreItem.store_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AnnotationStoreItem.name required")
    if "storeFormat" in data:
        out["store_format"] = data["storeFormat"]
    else:
        raise DeserializationError("AnnotationStoreItem.store_format required")
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError("AnnotationStoreItem.description required")
    if "sseConfig" in data:
        import capo_omics.types.sse_config

        out["sse_config"] = capo_omics.types.sse_config.deserialize_json(
            data["sseConfig"]
        )
    else:
        raise DeserializationError("AnnotationStoreItem.sse_config required")
    if "creationTime" in data:
        import capo_omics.types.creation_time

        out["creation_time"] = capo_omics.types.creation_time.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("AnnotationStoreItem.creation_time required")
    if "updateTime" in data:
        import capo_omics.types.update_time

        out["update_time"] = capo_omics.types.update_time.deserialize_json(
            data["updateTime"]
        )
    else:
        raise DeserializationError("AnnotationStoreItem.update_time required")
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    else:
        raise DeserializationError("AnnotationStoreItem.status_message required")
    if "storeSizeBytes" in data:
        out["store_size_bytes"] = data["storeSizeBytes"]
    else:
        raise DeserializationError("AnnotationStoreItem.store_size_bytes required")
    return out
