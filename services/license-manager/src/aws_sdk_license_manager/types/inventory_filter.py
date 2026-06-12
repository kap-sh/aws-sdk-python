"""Generated from Smithy shape ``com.amazonaws.licensemanager#InventoryFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.inventory_filter_condition
    import aws_sdk_license_manager.types.string


class InventoryFilter(TypedDict):
    name: "aws_sdk_license_manager.types.string.String"
    """<p>Name of the filter.</p>"""
    condition: "aws_sdk_license_manager.types.inventory_filter_condition.InventoryFilterCondition"
    """<p>Condition of the filter.</p>"""
    value: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Value of the filter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryFilter) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_license_manager.types.inventory_filter_condition

    out["Condition"] = (
        aws_sdk_license_manager.types.inventory_filter_condition.serialize_aws_json_1_1(
            value["condition"]
        )
    )
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InventoryFilter:
    out: InventoryFilter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("InventoryFilter.name required")
    if "Condition" in data:
        import aws_sdk_license_manager.types.inventory_filter_condition

        out["condition"] = (
            aws_sdk_license_manager.types.inventory_filter_condition.deserialize_aws_json_1_1(
                data["Condition"]
            )
        )
    else:
        raise DeserializationError("InventoryFilter.condition required")
    if "Value" in data:
        out["value"] = data["Value"]
    return out
