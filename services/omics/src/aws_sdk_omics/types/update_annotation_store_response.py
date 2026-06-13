"""Generated from Smithy shape ``com.amazonaws.omics#UpdateAnnotationStoreResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.creation_time
    import aws_sdk_omics.types.description
    import aws_sdk_omics.types.reference_item
    import aws_sdk_omics.types.resource_id
    import aws_sdk_omics.types.store_format
    import aws_sdk_omics.types.store_options
    import aws_sdk_omics.types.store_status
    import aws_sdk_omics.types.update_time


class UpdateAnnotationStoreResponse(TypedDict):
    id: "aws_sdk_omics.types.resource_id.ResourceId"
    """<p>The store's ID.</p>"""
    reference: "aws_sdk_omics.types.reference_item.ReferenceItem"
    """<p>The store's genome reference.</p>"""
    status: "aws_sdk_omics.types.store_status.StoreStatus"
    """<p>The store's status.</p>"""
    name: "str"
    """<p>The store's name.</p>"""
    description: "aws_sdk_omics.types.description.Description"
    """<p>The store's description.</p>"""
    creation_time: "aws_sdk_omics.types.creation_time.CreationTime"
    """<p>When the store was created.</p>"""
    update_time: "aws_sdk_omics.types.update_time.UpdateTime"
    """<p>When the store was updated.</p>"""
    store_options: NotRequired["aws_sdk_omics.types.store_options.StoreOptions"]
    """<p>Parsing options for the store.</p>"""
    store_format: NotRequired["aws_sdk_omics.types.store_format.StoreFormat"]
    """<p>The annotation file format of the store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAnnotationStoreResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import aws_sdk_omics.types.reference_item

    out["reference"] = aws_sdk_omics.types.reference_item.serialize_json(
        value["reference"]
    )
    out["status"] = value["status"]
    out["name"] = value["name"]
    out["description"] = value["description"]
    import aws_sdk_omics.types.creation_time

    out["creationTime"] = aws_sdk_omics.types.creation_time.serialize_json(
        value["creation_time"]
    )
    import aws_sdk_omics.types.update_time

    out["updateTime"] = aws_sdk_omics.types.update_time.serialize_json(
        value["update_time"]
    )
    if "store_options" in value:
        import aws_sdk_omics.types.store_options

        out["storeOptions"] = aws_sdk_omics.types.store_options.serialize_json(
            value["store_options"]
        )
    if "store_format" in value:
        out["storeFormat"] = value["store_format"]
    return out


def deserialize_json(data: dict) -> UpdateAnnotationStoreResponse:
    out: UpdateAnnotationStoreResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UpdateAnnotationStoreResponse.id required")
    if "reference" in data:
        import aws_sdk_omics.types.reference_item

        out["reference"] = aws_sdk_omics.types.reference_item.deserialize_json(
            data["reference"]
        )
    else:
        raise DeserializationError("UpdateAnnotationStoreResponse.reference required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("UpdateAnnotationStoreResponse.status required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateAnnotationStoreResponse.name required")
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError("UpdateAnnotationStoreResponse.description required")
    if "creationTime" in data:
        import aws_sdk_omics.types.creation_time

        out["creation_time"] = aws_sdk_omics.types.creation_time.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError(
            "UpdateAnnotationStoreResponse.creation_time required"
        )
    if "updateTime" in data:
        import aws_sdk_omics.types.update_time

        out["update_time"] = aws_sdk_omics.types.update_time.deserialize_json(
            data["updateTime"]
        )
    else:
        raise DeserializationError("UpdateAnnotationStoreResponse.update_time required")
    if "storeOptions" in data:
        import aws_sdk_omics.types.store_options

        out["store_options"] = aws_sdk_omics.types.store_options.deserialize_json(
            data["storeOptions"]
        )
    if "storeFormat" in data:
        out["store_format"] = data["storeFormat"]
    return out
