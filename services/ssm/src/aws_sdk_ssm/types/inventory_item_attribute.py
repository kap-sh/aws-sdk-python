"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryItemAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.inventory_attribute_data_type
    import aws_sdk_ssm.types.inventory_item_attribute_name


class InventoryItemAttribute(TypedDict, closed=True):
    name: "aws_sdk_ssm.types.inventory_item_attribute_name.InventoryItemAttributeName"
    """<p>Name of the inventory item attribute.</p>"""
    data_type: (
        "aws_sdk_ssm.types.inventory_attribute_data_type.InventoryAttributeDataType"
    )
    """<p>The data type of the inventory item attribute. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryItemAttribute) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_ssm.types.inventory_attribute_data_type

    out["DataType"] = (
        aws_sdk_ssm.types.inventory_attribute_data_type.serialize_aws_json_1_1(
            value["data_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> InventoryItemAttribute:
    out: InventoryItemAttribute = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("InventoryItemAttribute.name required")
    if "DataType" in data:
        import aws_sdk_ssm.types.inventory_attribute_data_type

        out["data_type"] = (
            aws_sdk_ssm.types.inventory_attribute_data_type.deserialize_aws_json_1_1(
                data["DataType"]
            )
        )
    else:
        raise DeserializationError("InventoryItemAttribute.data_type required")
    return out
