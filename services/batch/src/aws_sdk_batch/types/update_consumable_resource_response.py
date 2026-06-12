"""Generated from Smithy shape ``com.amazonaws.batch#UpdateConsumableResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.long
    import aws_sdk_batch.types.string


class UpdateConsumableResourceResponse(TypedDict):
    consumable_resource_name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name of the consumable resource to be updated.</p>"""
    consumable_resource_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the consumable resource.</p>"""
    total_quantity: NotRequired["aws_sdk_batch.types.long.Long"]
    """<p>The total amount of the consumable resource that is available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConsumableResourceResponse) -> dict:
    out: dict = {}
    if "consumable_resource_name" in value:
        out["consumableResourceName"] = value["consumable_resource_name"]
    if "consumable_resource_arn" in value:
        out["consumableResourceArn"] = value["consumable_resource_arn"]
    if "total_quantity" in value:
        out["totalQuantity"] = value["total_quantity"]
    return out


def deserialize_json(data: dict) -> UpdateConsumableResourceResponse:
    out: UpdateConsumableResourceResponse = {}  # type: ignore[typeddict-item]
    if "consumableResourceName" in data:
        out["consumable_resource_name"] = data["consumableResourceName"]
    if "consumableResourceArn" in data:
        out["consumable_resource_arn"] = data["consumableResourceArn"]
    if "totalQuantity" in data:
        out["total_quantity"] = data["totalQuantity"]
    return out
