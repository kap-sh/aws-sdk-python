"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServicePowerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.container_service_power

ContainerServicePowerList: TypeAlias = list[
    "aws_sdk_lightsail.types.container_service_power.ContainerServicePower"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerServicePowerList) -> list:
    import aws_sdk_lightsail.types.container_service_power

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lightsail.types.container_service_power.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerServicePowerList:
    import aws_sdk_lightsail.types.container_service_power

    out: ContainerServicePowerList = []
    for item in data:
        out.append(
            aws_sdk_lightsail.types.container_service_power.deserialize_aws_json_1_1(
                item
            )
        )
    return out
