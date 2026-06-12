"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryResultItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.inventory_item_capture_time
    import aws_sdk_ssm.types.inventory_item_content_hash
    import aws_sdk_ssm.types.inventory_item_entry_list
    import aws_sdk_ssm.types.inventory_item_schema_version
    import aws_sdk_ssm.types.inventory_item_type_name


class InventoryResultItem(TypedDict):
    type_name: "aws_sdk_ssm.types.inventory_item_type_name.InventoryItemTypeName"
    """<p>The name of the inventory result item type.</p>"""
    schema_version: (
        "aws_sdk_ssm.types.inventory_item_schema_version.InventoryItemSchemaVersion"
    )
    """<p>The schema version for the inventory result item/</p>"""
    capture_time: NotRequired[
        "aws_sdk_ssm.types.inventory_item_capture_time.InventoryItemCaptureTime"
    ]
    """<p>The time inventory item data was captured.</p>"""
    content_hash: NotRequired[
        "aws_sdk_ssm.types.inventory_item_content_hash.InventoryItemContentHash"
    ]
    """<p>MD5 hash of the inventory item type contents. The content hash is used to determine whether to update inventory information. The PutInventory API doesn't update the inventory item type contents if the MD5 hash hasn't changed since last update. </p>"""
    content: "aws_sdk_ssm.types.inventory_item_entry_list.InventoryItemEntryList"
    """<p>Contains all the inventory data of the item type. Results include attribute names and values. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryResultItem) -> dict:
    out: dict = {}
    out["TypeName"] = value["type_name"]
    out["SchemaVersion"] = value["schema_version"]
    if "capture_time" in value:
        out["CaptureTime"] = value["capture_time"]
    if "content_hash" in value:
        out["ContentHash"] = value["content_hash"]
    import aws_sdk_ssm.types.inventory_item_entry_list

    out["Content"] = aws_sdk_ssm.types.inventory_item_entry_list.serialize_aws_json_1_1(
        value["content"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> InventoryResultItem:
    out: InventoryResultItem = {}  # type: ignore[typeddict-item]
    if "TypeName" in data:
        out["type_name"] = data["TypeName"]
    else:
        raise DeserializationError("InventoryResultItem.type_name required")
    if "SchemaVersion" in data:
        out["schema_version"] = data["SchemaVersion"]
    else:
        raise DeserializationError("InventoryResultItem.schema_version required")
    if "CaptureTime" in data:
        out["capture_time"] = data["CaptureTime"]
    if "ContentHash" in data:
        out["content_hash"] = data["ContentHash"]
    if "Content" in data:
        import aws_sdk_ssm.types.inventory_item_entry_list

        out["content"] = (
            aws_sdk_ssm.types.inventory_item_entry_list.deserialize_aws_json_1_1(
                data["Content"]
            )
        )
    else:
        raise DeserializationError("InventoryResultItem.content required")
    return out
