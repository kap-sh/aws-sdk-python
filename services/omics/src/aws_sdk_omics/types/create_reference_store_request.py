"""Generated from Smithy shape ``com.amazonaws.omics#CreateReferenceStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.client_token
    import aws_sdk_omics.types.reference_store_description
    import aws_sdk_omics.types.reference_store_name
    import aws_sdk_omics.types.sse_config
    import aws_sdk_omics.types.tag_map


class CreateReferenceStoreRequest(TypedDict, closed=True):
    name: "aws_sdk_omics.types.reference_store_name.ReferenceStoreName"
    """<p>A name for the store.</p>"""
    description: NotRequired[
        "aws_sdk_omics.types.reference_store_description.ReferenceStoreDescription"
    ]
    """<p>A description for the store.</p>"""
    sse_config: NotRequired["aws_sdk_omics.types.sse_config.SseConfig"]
    """<p>Server-side encryption (SSE) settings for the store.</p>"""
    tags: NotRequired["aws_sdk_omics.types.tag_map.TagMap"]
    """<p>Tags for the store.</p>"""
    client_token: NotRequired["aws_sdk_omics.types.client_token.ClientToken"]
    """<p>To ensure that requests don't run multiple times, specify a unique token for each request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateReferenceStoreRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "sse_config" in value:
        import aws_sdk_omics.types.sse_config

        out["sseConfig"] = aws_sdk_omics.types.sse_config.serialize_json(
            value["sse_config"]
        )
    if "tags" in value:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.serialize_json(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateReferenceStoreRequest:
    out: CreateReferenceStoreRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateReferenceStoreRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "sseConfig" in data:
        import aws_sdk_omics.types.sse_config

        out["sse_config"] = aws_sdk_omics.types.sse_config.deserialize_json(
            data["sseConfig"]
        )
    if "tags" in data:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.deserialize_json(data["tags"])
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
