"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#HelmOperatingSystemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.helm_operating_system

HelmOperatingSystemList: TypeAlias = list[
    "aws_sdk_marketplace_discovery.types.helm_operating_system.HelmOperatingSystem"
]


# --- restJson1 ser/de ---
def serialize_json(value: HelmOperatingSystemList) -> list:
    import aws_sdk_marketplace_discovery.types.helm_operating_system

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_discovery.types.helm_operating_system.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> HelmOperatingSystemList:
    import aws_sdk_marketplace_discovery.types.helm_operating_system

    out: HelmOperatingSystemList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_discovery.types.helm_operating_system.deserialize_json(
                item
            )
        )
    return out
