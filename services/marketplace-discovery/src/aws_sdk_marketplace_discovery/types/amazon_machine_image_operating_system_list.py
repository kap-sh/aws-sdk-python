"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#AmazonMachineImageOperatingSystemList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.amazon_machine_image_operating_system

AmazonMachineImageOperatingSystemList: TypeAlias = list["aws_sdk_marketplace_discovery.types.amazon_machine_image_operating_system.AmazonMachineImageOperatingSystem"]


# --- restJson1 ser/de ---
def serialize_json(value: AmazonMachineImageOperatingSystemList) -> list:
    import aws_sdk_marketplace_discovery.types.amazon_machine_image_operating_system
    out: list = []
    for item in value:
        out.append(aws_sdk_marketplace_discovery.types.amazon_machine_image_operating_system.serialize_json(item))
    return out


def deserialize_json(data: list) -> AmazonMachineImageOperatingSystemList:
    import aws_sdk_marketplace_discovery.types.amazon_machine_image_operating_system
    out: AmazonMachineImageOperatingSystemList = []
    for item in data:
        out.append(aws_sdk_marketplace_discovery.types.amazon_machine_image_operating_system.deserialize_json(item))
    return out