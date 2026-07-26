"""Generated from Smithy shape ``com.amazonaws.licensemanager#ResourceInventoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_license_manager.types.resource_inventory

ResourceInventoryList: TypeAlias = list[
    "capo_license_manager.types.resource_inventory.ResourceInventory"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceInventoryList) -> list:
    import capo_license_manager.types.resource_inventory

    out: list = []
    for item in value:
        out.append(
            capo_license_manager.types.resource_inventory.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceInventoryList:
    import capo_license_manager.types.resource_inventory

    out: ResourceInventoryList = []
    for item in data:
        out.append(
            capo_license_manager.types.resource_inventory.deserialize_aws_json_1_1(item)
        )
    return out
