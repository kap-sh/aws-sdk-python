"""Generated from Smithy shape ``com.amazonaws.licensemanager#ResourceInventoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.resource_inventory

ResourceInventoryList: TypeAlias = list[
    "aws_sdk_license_manager.types.resource_inventory.ResourceInventory"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceInventoryList) -> list:
    import aws_sdk_license_manager.types.resource_inventory

    out: list = []
    for item in value:
        out.append(
            aws_sdk_license_manager.types.resource_inventory.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceInventoryList:
    import aws_sdk_license_manager.types.resource_inventory

    out: ResourceInventoryList = []
    for item in data:
        out.append(
            aws_sdk_license_manager.types.resource_inventory.deserialize_aws_json_1_1(
                item
            )
        )
    return out
