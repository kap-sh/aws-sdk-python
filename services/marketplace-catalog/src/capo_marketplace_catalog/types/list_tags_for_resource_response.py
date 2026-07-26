"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.resource_arn
    import capo_marketplace_catalog.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    resource_arn: NotRequired["capo_marketplace_catalog.types.resource_arn.ResourceARN"]
    """<p>Required. The ARN associated with the resource you want to list tags on.</p>"""
    tags: NotRequired["capo_marketplace_catalog.types.tag_list.TagList"]
    """<p>Required. A list of objects specifying each key name and value. Number of objects allowed: 1-50.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "tags" in value:
        import capo_marketplace_catalog.types.tag_list

        out["Tags"] = capo_marketplace_catalog.types.tag_list.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "Tags" in data:
        import capo_marketplace_catalog.types.tag_list

        out["tags"] = capo_marketplace_catalog.types.tag_list.deserialize_json(
            data["Tags"]
        )
    return out
