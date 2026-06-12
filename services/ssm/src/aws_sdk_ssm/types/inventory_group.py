"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryGroup``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.inventory_filter_list
    import aws_sdk_ssm.types.inventory_group_name


class InventoryGroup(TypedDict):
    name: "aws_sdk_ssm.types.inventory_group_name.InventoryGroupName"
    """<p>The name of the group.</p>"""
    filters: "aws_sdk_ssm.types.inventory_filter_list.InventoryFilterList"
    """<p>Filters define the criteria for the group. The <code>matchingCount</code> field displays the number of resources that match the criteria. The <code>notMatchingCount</code> field displays the number of resources that don't match the criteria. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryGroup) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_ssm.types.inventory_filter_list

    out["Filters"] = aws_sdk_ssm.types.inventory_filter_list.serialize_aws_json_1_1(
        value["filters"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> InventoryGroup:
    out: InventoryGroup = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("InventoryGroup.name required")
    if "Filters" in data:
        import aws_sdk_ssm.types.inventory_filter_list

        out["filters"] = (
            aws_sdk_ssm.types.inventory_filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    else:
        raise DeserializationError("InventoryGroup.filters required")
    return out
