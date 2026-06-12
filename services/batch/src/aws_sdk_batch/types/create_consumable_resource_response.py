"""Generated from Smithy shape ``com.amazonaws.batch#CreateConsumableResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.string


class CreateConsumableResourceResponse(TypedDict):
    consumable_resource_name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name of the consumable resource.</p>"""
    consumable_resource_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the consumable resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConsumableResourceResponse) -> dict:
    out: dict = {}
    if "consumable_resource_name" in value:
        out["consumableResourceName"] = value["consumable_resource_name"]
    if "consumable_resource_arn" in value:
        out["consumableResourceArn"] = value["consumable_resource_arn"]
    return out


def deserialize_json(data: dict) -> CreateConsumableResourceResponse:
    out: CreateConsumableResourceResponse = {}  # type: ignore[typeddict-item]
    if "consumableResourceName" in data:
        out["consumable_resource_name"] = data["consumableResourceName"]
    if "consumableResourceArn" in data:
        out["consumable_resource_arn"] = data["consumableResourceArn"]
    return out
