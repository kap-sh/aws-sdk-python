"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_service_catalog_appregistry.types.arn
    import capo_service_catalog_appregistry.types.tag_keys


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_service_catalog_appregistry.types.arn.Arn"
    """<p>The Amazon resource name (ARN) that specifies the resource.</p>"""
    tag_keys: "capo_service_catalog_appregistry.types.tag_keys.TagKeys"
    """<p>A list of the tag keys to remove from the specified resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
