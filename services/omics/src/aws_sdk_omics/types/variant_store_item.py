"""Generated from Smithy shape ``com.amazonaws.omics#VariantStoreItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.arn
    import aws_sdk_omics.types.creation_time
    import aws_sdk_omics.types.description
    import aws_sdk_omics.types.reference_item
    import aws_sdk_omics.types.resource_id
    import aws_sdk_omics.types.sse_config
    import aws_sdk_omics.types.status_message
    import aws_sdk_omics.types.store_status
    import aws_sdk_omics.types.update_time


class VariantStoreItem(TypedDict, closed=True):
    id: "aws_sdk_omics.types.resource_id.ResourceId"
    """<p>The store's ID.</p>"""
    reference: "aws_sdk_omics.types.reference_item.ReferenceItem"
    """<p>The store's genome reference.</p>"""
    status: "aws_sdk_omics.types.store_status.StoreStatus"
    """<p>The store's status.</p>"""
    store_arn: "aws_sdk_omics.types.arn.Arn"
    """<p>The store's ARN.</p>"""
    name: "str"
    """<p>The store's name.</p>"""
    description: "aws_sdk_omics.types.description.Description"
    """<p>The store's description.</p>"""
    sse_config: "aws_sdk_omics.types.sse_config.SseConfig"
    """<p>The store's server-side encryption (SSE) settings.</p>"""
    creation_time: "aws_sdk_omics.types.creation_time.CreationTime"
    """<p>When the store was created.</p>"""
    update_time: "aws_sdk_omics.types.update_time.UpdateTime"
    """<p>When the store was updated.</p>"""
    status_message: "aws_sdk_omics.types.status_message.StatusMessage"
    """<p>The store's status message.</p>"""
    store_size_bytes: "int"
    """<p>The store's size in bytes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VariantStoreItem) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import aws_sdk_omics.types.reference_item

    out["reference"] = aws_sdk_omics.types.reference_item.serialize_json(
        value["reference"]
    )
    out["status"] = value["status"]
    out["storeArn"] = value["store_arn"]
    out["name"] = value["name"]
    out["description"] = value["description"]
    import aws_sdk_omics.types.sse_config

    out["sseConfig"] = aws_sdk_omics.types.sse_config.serialize_json(
        value["sse_config"]
    )
    import aws_sdk_omics.types.creation_time

    out["creationTime"] = aws_sdk_omics.types.creation_time.serialize_json(
        value["creation_time"]
    )
    import aws_sdk_omics.types.update_time

    out["updateTime"] = aws_sdk_omics.types.update_time.serialize_json(
        value["update_time"]
    )
    out["statusMessage"] = value["status_message"]
    out["storeSizeBytes"] = value["store_size_bytes"]
    return out


def deserialize_json(data: dict) -> VariantStoreItem:
    out: VariantStoreItem = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("VariantStoreItem.id required")
    if "reference" in data:
        import aws_sdk_omics.types.reference_item

        out["reference"] = aws_sdk_omics.types.reference_item.deserialize_json(
            data["reference"]
        )
    else:
        raise DeserializationError("VariantStoreItem.reference required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("VariantStoreItem.status required")
    if "storeArn" in data:
        out["store_arn"] = data["storeArn"]
    else:
        raise DeserializationError("VariantStoreItem.store_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("VariantStoreItem.name required")
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError("VariantStoreItem.description required")
    if "sseConfig" in data:
        import aws_sdk_omics.types.sse_config

        out["sse_config"] = aws_sdk_omics.types.sse_config.deserialize_json(
            data["sseConfig"]
        )
    else:
        raise DeserializationError("VariantStoreItem.sse_config required")
    if "creationTime" in data:
        import aws_sdk_omics.types.creation_time

        out["creation_time"] = aws_sdk_omics.types.creation_time.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("VariantStoreItem.creation_time required")
    if "updateTime" in data:
        import aws_sdk_omics.types.update_time

        out["update_time"] = aws_sdk_omics.types.update_time.deserialize_json(
            data["updateTime"]
        )
    else:
        raise DeserializationError("VariantStoreItem.update_time required")
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    else:
        raise DeserializationError("VariantStoreItem.status_message required")
    if "storeSizeBytes" in data:
        out["store_size_bytes"] = data["storeSizeBytes"]
    else:
        raise DeserializationError("VariantStoreItem.store_size_bytes required")
    return out
