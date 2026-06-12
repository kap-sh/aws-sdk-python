"""Generated from Smithy shape ``com.amazonaws.batch#DescribeConsumableResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.long
    import aws_sdk_batch.types.string
    import aws_sdk_batch.types.tagris_tags_map


class DescribeConsumableResourceResponse(TypedDict):
    consumable_resource_name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name of the consumable resource.</p>"""
    consumable_resource_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the consumable resource.</p>"""
    total_quantity: NotRequired["aws_sdk_batch.types.long.Long"]
    """<p>The total amount of the consumable resource that is available.</p>"""
    in_use_quantity: NotRequired["aws_sdk_batch.types.long.Long"]
    """<p>The amount of the consumable resource that is currently in use.</p>"""
    available_quantity: NotRequired["aws_sdk_batch.types.long.Long"]
    """<p>The amount of the consumable resource that is currently available to use.</p>"""
    resource_type: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>Indicates whether the resource is available to be re-used after a job completes. Can be one of: </p> <ul> <li> <p> <code>REPLENISHABLE</code> </p> </li> <li> <p> <code>NON_REPLENISHABLE</code> </p> </li> </ul>"""
    created_at: NotRequired["aws_sdk_batch.types.long.Long"]
    """<p>The Unix timestamp (in milliseconds) for when the consumable resource was created.</p>"""
    tags: NotRequired["aws_sdk_batch.types.tagris_tags_map.TagrisTagsMap"]
    """<p>The tags that you apply to the consumable resource to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html\">Tagging your Batch resources</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeConsumableResourceResponse) -> dict:
    out: dict = {}
    if "consumable_resource_name" in value:
        out["consumableResourceName"] = value["consumable_resource_name"]
    if "consumable_resource_arn" in value:
        out["consumableResourceArn"] = value["consumable_resource_arn"]
    if "total_quantity" in value:
        out["totalQuantity"] = value["total_quantity"]
    if "in_use_quantity" in value:
        out["inUseQuantity"] = value["in_use_quantity"]
    if "available_quantity" in value:
        out["availableQuantity"] = value["available_quantity"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "created_at" in value:
        out["createdAt"] = value["created_at"]
    if "tags" in value:
        import aws_sdk_batch.types.tagris_tags_map

        out["tags"] = aws_sdk_batch.types.tagris_tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> DescribeConsumableResourceResponse:
    out: DescribeConsumableResourceResponse = {}  # type: ignore[typeddict-item]
    if "consumableResourceName" in data:
        out["consumable_resource_name"] = data["consumableResourceName"]
    if "consumableResourceArn" in data:
        out["consumable_resource_arn"] = data["consumableResourceArn"]
    if "totalQuantity" in data:
        out["total_quantity"] = data["totalQuantity"]
    if "inUseQuantity" in data:
        out["in_use_quantity"] = data["inUseQuantity"]
    if "availableQuantity" in data:
        out["available_quantity"] = data["availableQuantity"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    if "createdAt" in data:
        out["created_at"] = data["createdAt"]
    if "tags" in data:
        import aws_sdk_batch.types.tagris_tags_map

        out["tags"] = aws_sdk_batch.types.tagris_tags_map.deserialize_json(data["tags"])
    return out
