"""Generated from Smithy shape ``com.amazonaws.batch#ConsumableResourceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.long
    import aws_sdk_batch.types.string


class ConsumableResourceSummary(TypedDict, closed=True):
    consumable_resource_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the consumable resource.</p>"""
    consumable_resource_name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name of the consumable resource.</p>"""
    total_quantity: NotRequired["aws_sdk_batch.types.long.Long"]
    """<p>The total amount of the consumable resource that is available.</p>"""
    in_use_quantity: NotRequired["aws_sdk_batch.types.long.Long"]
    """<p>The amount of the consumable resource that is currently in use.</p>"""
    resource_type: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>Indicates whether the resource is available to be re-used after a job completes. Can be one of: </p> <ul> <li> <p> <code>REPLENISHABLE</code> </p> </li> <li> <p> <code>NON_REPLENISHABLE</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConsumableResourceSummary) -> dict:
    out: dict = {}
    if "consumable_resource_arn" in value:
        out["consumableResourceArn"] = value["consumable_resource_arn"]
    if "consumable_resource_name" in value:
        out["consumableResourceName"] = value["consumable_resource_name"]
    if "total_quantity" in value:
        out["totalQuantity"] = value["total_quantity"]
    if "in_use_quantity" in value:
        out["inUseQuantity"] = value["in_use_quantity"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ConsumableResourceSummary:
    out: ConsumableResourceSummary = {}  # type: ignore[typeddict-item]
    if "consumableResourceArn" in data:
        out["consumable_resource_arn"] = data["consumableResourceArn"]
    if "consumableResourceName" in data:
        out["consumable_resource_name"] = data["consumableResourceName"]
    if "totalQuantity" in data:
        out["total_quantity"] = data["totalQuantity"]
    if "inUseQuantity" in data:
        out["in_use_quantity"] = data["inUseQuantity"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    return out
