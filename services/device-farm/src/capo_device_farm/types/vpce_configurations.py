"""Generated from Smithy shape ``com.amazonaws.devicefarm#VPCEConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_device_farm.types.vpce_configuration

VPCEConfigurations: TypeAlias = list[
    "capo_device_farm.types.vpce_configuration.VPCEConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VPCEConfigurations) -> list:
    import capo_device_farm.types.vpce_configuration

    out: list = []
    for item in value:
        out.append(
            capo_device_farm.types.vpce_configuration.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> VPCEConfigurations:
    import capo_device_farm.types.vpce_configuration

    out: VPCEConfigurations = []
    for item in data:
        out.append(
            capo_device_farm.types.vpce_configuration.deserialize_aws_json_1_1(item)
        )
    return out
