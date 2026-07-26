"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServicePowerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.container_service_power

ContainerServicePowerList: TypeAlias = list[
    "capo_lightsail.types.container_service_power.ContainerServicePower"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerServicePowerList) -> list:
    import capo_lightsail.types.container_service_power

    out: list = []
    for item in value:
        out.append(
            capo_lightsail.types.container_service_power.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerServicePowerList:
    import capo_lightsail.types.container_service_power

    out: ContainerServicePowerList = []
    for item in data:
        out.append(
            capo_lightsail.types.container_service_power.deserialize_aws_json_1_1(item)
        )
    return out
