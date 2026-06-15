"""Generated from Smithy shape ``com.amazonaws.batch#CreateConsumableResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.long
    import aws_sdk_batch.types.string
    import aws_sdk_batch.types.tagris_tags_map


class CreateConsumableResourceRequest(TypedDict):
    consumable_resource_name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name of the consumable resource. Must be unique.</p>"""
    total_quantity: NotRequired["aws_sdk_batch.types.long.Long"]
    """<p>The total amount of the consumable resource that is available. Must be non-negative.</p>"""
    resource_type: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>Indicates whether the resource is available to be re-used after a job completes. Can be one of: </p> <ul> <li> <p> <code>REPLENISHABLE</code> (default)</p> </li> <li> <p> <code>NON_REPLENISHABLE</code> </p> </li> </ul>"""
    tags: NotRequired["aws_sdk_batch.types.tagris_tags_map.TagrisTagsMap"]
    r"""<p>The tags that you apply to the consumable resource to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html\">Tagging your Batch resources</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConsumableResourceRequest) -> dict:
    out: dict = {}
    if "consumable_resource_name" in value:
        out["consumableResourceName"] = value["consumable_resource_name"]
    if "total_quantity" in value:
        out["totalQuantity"] = value["total_quantity"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "tags" in value:
        import aws_sdk_batch.types.tagris_tags_map

        out["tags"] = aws_sdk_batch.types.tagris_tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateConsumableResourceRequest:
    out: CreateConsumableResourceRequest = {}  # type: ignore[typeddict-item]
    if "consumableResourceName" in data:
        out["consumable_resource_name"] = data["consumableResourceName"]
    if "totalQuantity" in data:
        out["total_quantity"] = data["totalQuantity"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    if "tags" in data:
        import aws_sdk_batch.types.tagris_tags_map

        out["tags"] = aws_sdk_batch.types.tagris_tags_map.deserialize_json(data["tags"])
    return out
