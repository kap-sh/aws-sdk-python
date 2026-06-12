"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryItemSchema``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.inventory_item_attribute_list
    import aws_sdk_ssm.types.inventory_item_schema_version
    import aws_sdk_ssm.types.inventory_item_type_name
    import aws_sdk_ssm.types.inventory_type_display_name


class InventoryItemSchema(TypedDict):
    type_name: "aws_sdk_ssm.types.inventory_item_type_name.InventoryItemTypeName"
    """<p>The name of the inventory type. Default inventory item type names start with Amazon Web Services. Custom inventory type names will start with Custom. Default inventory item types include the following: <code>AWS:AWSComponent</code>, <code>AWS:Application</code>, <code>AWS:InstanceInformation</code>, <code>AWS:Network</code>, and <code>AWS:WindowsUpdate</code>.</p>"""
    version: NotRequired[
        "aws_sdk_ssm.types.inventory_item_schema_version.InventoryItemSchemaVersion"
    ]
    """<p>The schema version for the inventory item.</p>"""
    attributes: (
        "aws_sdk_ssm.types.inventory_item_attribute_list.InventoryItemAttributeList"
    )
    """<p>The schema attributes for inventory. This contains data type and attribute name.</p>"""
    display_name: NotRequired[
        "aws_sdk_ssm.types.inventory_type_display_name.InventoryTypeDisplayName"
    ]
    """<p>The alias name of the inventory type. The alias name is used for display purposes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryItemSchema) -> dict:
    out: dict = {}
    out["TypeName"] = value["type_name"]
    if "version" in value:
        out["Version"] = value["version"]
    import aws_sdk_ssm.types.inventory_item_attribute_list

    out["Attributes"] = (
        aws_sdk_ssm.types.inventory_item_attribute_list.serialize_aws_json_1_1(
            value["attributes"]
        )
    )
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InventoryItemSchema:
    out: InventoryItemSchema = {}  # type: ignore[typeddict-item]
    if "TypeName" in data:
        out["type_name"] = data["TypeName"]
    else:
        raise DeserializationError("InventoryItemSchema.type_name required")
    if "Version" in data:
        out["version"] = data["Version"]
    if "Attributes" in data:
        import aws_sdk_ssm.types.inventory_item_attribute_list

        out["attributes"] = (
            aws_sdk_ssm.types.inventory_item_attribute_list.deserialize_aws_json_1_1(
                data["Attributes"]
            )
        )
    else:
        raise DeserializationError("InventoryItemSchema.attributes required")
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    return out
