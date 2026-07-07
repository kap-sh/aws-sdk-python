"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_service_catalog_appregistry.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.arn
    import aws_sdk_service_catalog_appregistry.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_service_catalog_appregistry.types.arn.Arn"
    """<p>The Amazon resource name (ARN) that specifies the resource.</p>"""
    tags: "aws_sdk_service_catalog_appregistry.types.tags.Tags"
    """<p>The new or modified tags for the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_service_catalog_appregistry.types.tags

    out["tags"] = aws_sdk_service_catalog_appregistry.types.tags.serialize_json(
        value["tags"]
    )
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_service_catalog_appregistry.types.tags

        out["tags"] = aws_sdk_service_catalog_appregistry.types.tags.deserialize_json(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
