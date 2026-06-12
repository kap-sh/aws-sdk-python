"""Generated from Smithy shape ``com.amazonaws.ssm#PutInventoryRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.instance_id
    import aws_sdk_ssm.types.inventory_item_list


class PutInventoryRequest(TypedDict):
    instance_id: "aws_sdk_ssm.types.instance_id.InstanceId"
    """<p>An managed node ID where you want to add or update inventory items.</p>"""
    items: "aws_sdk_ssm.types.inventory_item_list.InventoryItemList"
    """<p>The inventory items that you want to add or update on managed nodes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutInventoryRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    import aws_sdk_ssm.types.inventory_item_list

    out["Items"] = aws_sdk_ssm.types.inventory_item_list.serialize_aws_json_1_1(
        value["items"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutInventoryRequest:
    out: PutInventoryRequest = {}  # type: ignore[typeddict-item]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("PutInventoryRequest.instance_id required")
    if "Items" in data:
        import aws_sdk_ssm.types.inventory_item_list

        out["items"] = aws_sdk_ssm.types.inventory_item_list.deserialize_aws_json_1_1(
            data["Items"]
        )
    else:
        raise DeserializationError("PutInventoryRequest.items required")
    return out
