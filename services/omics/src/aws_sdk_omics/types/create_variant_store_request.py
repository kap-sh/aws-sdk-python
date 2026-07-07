"""Generated from Smithy shape ``com.amazonaws.omics#CreateVariantStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.description
    import aws_sdk_omics.types.reference_item
    import aws_sdk_omics.types.sse_config
    import aws_sdk_omics.types.store_name
    import aws_sdk_omics.types.tag_map


class CreateVariantStoreRequest(TypedDict, closed=True):
    reference: "aws_sdk_omics.types.reference_item.ReferenceItem"
    """<p>The genome reference for the store's variants.</p>"""
    name: NotRequired["aws_sdk_omics.types.store_name.StoreName"]
    """<p>A name for the store.</p>"""
    description: NotRequired["aws_sdk_omics.types.description.Description"]
    """<p>A description for the store.</p>"""
    tags: NotRequired["aws_sdk_omics.types.tag_map.TagMap"]
    """<p>Tags for the store.</p>"""
    sse_config: NotRequired["aws_sdk_omics.types.sse_config.SseConfig"]
    """<p>Server-side encryption (SSE) settings for the store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVariantStoreRequest) -> dict:
    out: dict = {}
    import aws_sdk_omics.types.reference_item

    out["reference"] = aws_sdk_omics.types.reference_item.serialize_json(
        value["reference"]
    )
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.serialize_json(value["tags"])
    if "sse_config" in value:
        import aws_sdk_omics.types.sse_config

        out["sseConfig"] = aws_sdk_omics.types.sse_config.serialize_json(
            value["sse_config"]
        )
    return out


def deserialize_json(data: dict) -> CreateVariantStoreRequest:
    out: CreateVariantStoreRequest = {}  # type: ignore[typeddict-item]
    if "reference" in data:
        import aws_sdk_omics.types.reference_item

        out["reference"] = aws_sdk_omics.types.reference_item.deserialize_json(
            data["reference"]
        )
    else:
        raise DeserializationError("CreateVariantStoreRequest.reference required")
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.deserialize_json(data["tags"])
    if "sseConfig" in data:
        import aws_sdk_omics.types.sse_config

        out["sse_config"] = aws_sdk_omics.types.sse_config.deserialize_json(
            data["sseConfig"]
        )
    return out
