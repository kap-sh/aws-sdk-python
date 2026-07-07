"""Generated from Smithy shape ``com.amazonaws.ssm#ListInventoryEntriesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.instance_id
    import aws_sdk_ssm.types.inventory_item_capture_time
    import aws_sdk_ssm.types.inventory_item_entry_list
    import aws_sdk_ssm.types.inventory_item_schema_version
    import aws_sdk_ssm.types.inventory_item_type_name
    import aws_sdk_ssm.types.next_token


class ListInventoryEntriesResult(TypedDict, closed=True):
    type_name: NotRequired[
        "aws_sdk_ssm.types.inventory_item_type_name.InventoryItemTypeName"
    ]
    """<p>The type of inventory item returned by the request.</p>"""
    instance_id: NotRequired["aws_sdk_ssm.types.instance_id.InstanceId"]
    """<p>The managed node ID targeted by the request to query inventory information.</p>"""
    schema_version: NotRequired[
        "aws_sdk_ssm.types.inventory_item_schema_version.InventoryItemSchemaVersion"
    ]
    """<p>The inventory schema version used by the managed nodes.</p>"""
    capture_time: NotRequired[
        "aws_sdk_ssm.types.inventory_item_capture_time.InventoryItemCaptureTime"
    ]
    """<p>The time that inventory information was collected for the managed nodes.</p>"""
    entries: NotRequired[
        "aws_sdk_ssm.types.inventory_item_entry_list.InventoryItemEntryList"
    ]
    """<p>A list of inventory items on the managed nodes.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListInventoryEntriesResult) -> dict:
    out: dict = {}
    if "type_name" in value:
        out["TypeName"] = value["type_name"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "schema_version" in value:
        out["SchemaVersion"] = value["schema_version"]
    if "capture_time" in value:
        out["CaptureTime"] = value["capture_time"]
    if "entries" in value:
        import aws_sdk_ssm.types.inventory_item_entry_list

        out["Entries"] = (
            aws_sdk_ssm.types.inventory_item_entry_list.serialize_aws_json_1_1(
                value["entries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListInventoryEntriesResult:
    out: ListInventoryEntriesResult = {}  # type: ignore[typeddict-item]
    if "TypeName" in data:
        out["type_name"] = data["TypeName"]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    if "SchemaVersion" in data:
        out["schema_version"] = data["SchemaVersion"]
    if "CaptureTime" in data:
        out["capture_time"] = data["CaptureTime"]
    if "Entries" in data:
        import aws_sdk_ssm.types.inventory_item_entry_list

        out["entries"] = (
            aws_sdk_ssm.types.inventory_item_entry_list.deserialize_aws_json_1_1(
                data["Entries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
