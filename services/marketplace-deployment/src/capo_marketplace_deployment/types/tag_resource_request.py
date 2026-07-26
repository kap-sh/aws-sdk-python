"""Generated from Smithy shape ``com.amazonaws.marketplacedeployment#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_deployment.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) associated with the resource you want to tag.</p>"""
    tags: NotRequired["capo_marketplace_deployment.types.tags.Tags"]
    """<p>A map of key-value pairs, where each pair represents a tag present on the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_marketplace_deployment.types.tags

        out["tags"] = capo_marketplace_deployment.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_marketplace_deployment.types.tags

        out["tags"] = capo_marketplace_deployment.types.tags.deserialize_json(
            data["tags"]
        )
    return out
