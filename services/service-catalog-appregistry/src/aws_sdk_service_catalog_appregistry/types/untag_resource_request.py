"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.arn
    import aws_sdk_service_catalog_appregistry.types.tag_keys


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_service_catalog_appregistry.types.arn.Arn"
    """<p>The Amazon resource name (ARN) that specifies the resource.</p>"""
    tag_keys: "aws_sdk_service_catalog_appregistry.types.tag_keys.TagKeys"
    """<p>A list of the tag keys to remove from the specified resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
