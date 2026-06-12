"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryResultEntity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.inventory_result_entity_id
    import aws_sdk_ssm.types.inventory_result_item_map


class InventoryResultEntity(TypedDict):
    id: NotRequired[
        "aws_sdk_ssm.types.inventory_result_entity_id.InventoryResultEntityId"
    ]
    """<p>ID of the inventory result entity. For example, for managed node inventory the result will be the managed node ID. For EC2 instance inventory, the result will be the instance ID. </p>"""
    data: NotRequired[
        "aws_sdk_ssm.types.inventory_result_item_map.InventoryResultItemMap"
    ]
    """<p>The data section in the inventory result entity JSON.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryResultEntity) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "data" in value:
        import aws_sdk_ssm.types.inventory_result_item_map

        out["Data"] = (
            aws_sdk_ssm.types.inventory_result_item_map.serialize_aws_json_1_1(
                value["data"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InventoryResultEntity:
    out: InventoryResultEntity = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Data" in data:
        import aws_sdk_ssm.types.inventory_result_item_map

        out["data"] = (
            aws_sdk_ssm.types.inventory_result_item_map.deserialize_aws_json_1_1(
                data["Data"]
            )
        )
    return out
