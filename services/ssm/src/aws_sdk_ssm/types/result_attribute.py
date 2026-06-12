"""Generated from Smithy shape ``com.amazonaws.ssm#ResultAttribute``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.inventory_item_type_name


class ResultAttribute(TypedDict):
    type_name: "aws_sdk_ssm.types.inventory_item_type_name.InventoryItemTypeName"
    """<p>Name of the inventory item type. Valid value: <code>AWS:InstanceInformation</code>. Default Value: <code>AWS:InstanceInformation</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResultAttribute) -> dict:
    out: dict = {}
    out["TypeName"] = value["type_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResultAttribute:
    out: ResultAttribute = {}  # type: ignore[typeddict-item]
    if "TypeName" in data:
        out["type_name"] = data["TypeName"]
    else:
        raise DeserializationError("ResultAttribute.type_name required")
    return out
