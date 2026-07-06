"""Generated from Smithy shape ``com.amazonaws.omics#CreateAnnotationStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.description
    import aws_sdk_omics.types.reference_item
    import aws_sdk_omics.types.sse_config
    import aws_sdk_omics.types.store_format
    import aws_sdk_omics.types.store_name
    import aws_sdk_omics.types.store_options
    import aws_sdk_omics.types.tag_map
    import aws_sdk_omics.types.version_name


class CreateAnnotationStoreRequest(TypedDict, closed=True):
    reference: NotRequired["aws_sdk_omics.types.reference_item.ReferenceItem"]
    """<p>The genome reference for the store's annotations.</p>"""
    name: NotRequired["aws_sdk_omics.types.store_name.StoreName"]
    """<p>A name for the store.</p>"""
    description: NotRequired["aws_sdk_omics.types.description.Description"]
    """<p>A description for the store.</p>"""
    tags: NotRequired["aws_sdk_omics.types.tag_map.TagMap"]
    """<p>Tags for the store.</p>"""
    version_name: NotRequired["aws_sdk_omics.types.version_name.VersionName"]
    """<p> The name given to an annotation store version to distinguish it from other versions. </p>"""
    sse_config: NotRequired["aws_sdk_omics.types.sse_config.SseConfig"]
    """<p>Server-side encryption (SSE) settings for the store.</p>"""
    store_format: "aws_sdk_omics.types.store_format.StoreFormat"
    """<p>The annotation file format of the store.</p>"""
    store_options: NotRequired["aws_sdk_omics.types.store_options.StoreOptions"]
    """<p>File parsing options for the annotation store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAnnotationStoreRequest) -> dict:
    out: dict = {}
    if "reference" in value:
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
    if "version_name" in value:
        out["versionName"] = value["version_name"]
    if "sse_config" in value:
        import aws_sdk_omics.types.sse_config

        out["sseConfig"] = aws_sdk_omics.types.sse_config.serialize_json(
            value["sse_config"]
        )
    out["storeFormat"] = value["store_format"]
    if "store_options" in value:
        import aws_sdk_omics.types.store_options

        out["storeOptions"] = aws_sdk_omics.types.store_options.serialize_json(
            value["store_options"]
        )
    return out


def deserialize_json(data: dict) -> CreateAnnotationStoreRequest:
    out: CreateAnnotationStoreRequest = {}  # type: ignore[typeddict-item]
    if "reference" in data:
        import aws_sdk_omics.types.reference_item

        out["reference"] = aws_sdk_omics.types.reference_item.deserialize_json(
            data["reference"]
        )
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.deserialize_json(data["tags"])
    if "versionName" in data:
        out["version_name"] = data["versionName"]
    if "sseConfig" in data:
        import aws_sdk_omics.types.sse_config

        out["sse_config"] = aws_sdk_omics.types.sse_config.deserialize_json(
            data["sseConfig"]
        )
    if "storeFormat" in data:
        out["store_format"] = data["storeFormat"]
    else:
        raise DeserializationError("CreateAnnotationStoreRequest.store_format required")
    if "storeOptions" in data:
        import aws_sdk_omics.types.store_options

        out["store_options"] = aws_sdk_omics.types.store_options.deserialize_json(
            data["storeOptions"]
        )
    return out
