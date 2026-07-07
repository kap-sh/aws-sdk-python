"""Generated from Smithy shape ``com.amazonaws.omics#CreateVariantStoreResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.creation_time
    import aws_sdk_omics.types.reference_item
    import aws_sdk_omics.types.resource_id
    import aws_sdk_omics.types.store_status


class CreateVariantStoreResponse(TypedDict, closed=True):
    id: "aws_sdk_omics.types.resource_id.ResourceId"
    """<p>The store's ID.</p>"""
    reference: NotRequired["aws_sdk_omics.types.reference_item.ReferenceItem"]
    """<p>The store's genome reference.</p>"""
    status: "aws_sdk_omics.types.store_status.StoreStatus"
    """<p>The store's status.</p>"""
    name: "str"
    """<p>The store's name.</p>"""
    creation_time: "aws_sdk_omics.types.creation_time.CreationTime"
    """<p>When the store was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVariantStoreResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "reference" in value:
        import aws_sdk_omics.types.reference_item

        out["reference"] = aws_sdk_omics.types.reference_item.serialize_json(
            value["reference"]
        )
    out["status"] = value["status"]
    out["name"] = value["name"]
    import aws_sdk_omics.types.creation_time

    out["creationTime"] = aws_sdk_omics.types.creation_time.serialize_json(
        value["creation_time"]
    )
    return out


def deserialize_json(data: dict) -> CreateVariantStoreResponse:
    out: CreateVariantStoreResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateVariantStoreResponse.id required")
    if "reference" in data:
        import aws_sdk_omics.types.reference_item

        out["reference"] = aws_sdk_omics.types.reference_item.deserialize_json(
            data["reference"]
        )
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("CreateVariantStoreResponse.status required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateVariantStoreResponse.name required")
    if "creationTime" in data:
        import aws_sdk_omics.types.creation_time

        out["creation_time"] = aws_sdk_omics.types.creation_time.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("CreateVariantStoreResponse.creation_time required")
    return out
