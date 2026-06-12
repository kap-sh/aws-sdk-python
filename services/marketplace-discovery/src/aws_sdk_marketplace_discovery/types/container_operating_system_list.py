"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ContainerOperatingSystemList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.container_operating_system

ContainerOperatingSystemList: TypeAlias = list["aws_sdk_marketplace_discovery.types.container_operating_system.ContainerOperatingSystem"]


# --- restJson1 ser/de ---
def serialize_json(value: ContainerOperatingSystemList) -> list:
    import aws_sdk_marketplace_discovery.types.container_operating_system
    out: list = []
    for item in value:
        out.append(aws_sdk_marketplace_discovery.types.container_operating_system.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContainerOperatingSystemList:
    import aws_sdk_marketplace_discovery.types.container_operating_system
    out: ContainerOperatingSystemList = []
    for item in data:
        out.append(aws_sdk_marketplace_discovery.types.container_operating_system.deserialize_json(item))
    return out