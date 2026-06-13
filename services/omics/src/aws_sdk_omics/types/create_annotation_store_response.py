"""Generated from Smithy shape ``com.amazonaws.omics#CreateAnnotationStoreResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.creation_time
    import aws_sdk_omics.types.reference_item
    import aws_sdk_omics.types.resource_id
    import aws_sdk_omics.types.store_format
    import aws_sdk_omics.types.store_options
    import aws_sdk_omics.types.store_status
    import aws_sdk_omics.types.version_name


class CreateAnnotationStoreResponse(TypedDict):
    id: "aws_sdk_omics.types.resource_id.ResourceId"
    """<p>The store's ID.</p>"""
    reference: NotRequired["aws_sdk_omics.types.reference_item.ReferenceItem"]
    """<p>The store's genome reference. Required for all stores except TSV format with generic annotations.</p>"""
    store_format: NotRequired["aws_sdk_omics.types.store_format.StoreFormat"]
    """<p>The annotation file format of the store.</p>"""
    store_options: NotRequired["aws_sdk_omics.types.store_options.StoreOptions"]
    """<p>The store's file parsing options.</p>"""
    status: "aws_sdk_omics.types.store_status.StoreStatus"
    """<p>The store's status.</p>"""
    name: "str"
    """<p>The store's name.</p>"""
    version_name: "aws_sdk_omics.types.version_name.VersionName"
    """<p> The name given to an annotation store version to distinguish it from other versions. </p>"""
    creation_time: "aws_sdk_omics.types.creation_time.CreationTime"
    """<p>When the store was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAnnotationStoreResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "reference" in value:
        import aws_sdk_omics.types.reference_item

        out["reference"] = aws_sdk_omics.types.reference_item.serialize_json(
            value["reference"]
        )
    if "store_format" in value:
        out["storeFormat"] = value["store_format"]
    if "store_options" in value:
        import aws_sdk_omics.types.store_options

        out["storeOptions"] = aws_sdk_omics.types.store_options.serialize_json(
            value["store_options"]
        )
    out["status"] = value["status"]
    out["name"] = value["name"]
    out["versionName"] = value["version_name"]
    import aws_sdk_omics.types.creation_time

    out["creationTime"] = aws_sdk_omics.types.creation_time.serialize_json(
        value["creation_time"]
    )
    return out


def deserialize_json(data: dict) -> CreateAnnotationStoreResponse:
    out: CreateAnnotationStoreResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateAnnotationStoreResponse.id required")
    if "reference" in data:
        import aws_sdk_omics.types.reference_item

        out["reference"] = aws_sdk_omics.types.reference_item.deserialize_json(
            data["reference"]
        )
    if "storeFormat" in data:
        out["store_format"] = data["storeFormat"]
    if "storeOptions" in data:
        import aws_sdk_omics.types.store_options

        out["store_options"] = aws_sdk_omics.types.store_options.deserialize_json(
            data["storeOptions"]
        )
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("CreateAnnotationStoreResponse.status required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAnnotationStoreResponse.name required")
    if "versionName" in data:
        out["version_name"] = data["versionName"]
    else:
        raise DeserializationError(
            "CreateAnnotationStoreResponse.version_name required"
        )
    if "creationTime" in data:
        import aws_sdk_omics.types.creation_time

        out["creation_time"] = aws_sdk_omics.types.creation_time.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError(
            "CreateAnnotationStoreResponse.creation_time required"
        )
    return out
