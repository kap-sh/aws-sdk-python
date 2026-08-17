"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceVolumeConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.service_volume_configuration

ServiceVolumeConfigurations: TypeAlias = list[
    "capo_ecs.types.service_volume_configuration.ServiceVolumeConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceVolumeConfigurations) -> list:
    import capo_ecs.types.service_volume_configuration

    out: list = []
    for item in value:
        out.append(
            capo_ecs.types.service_volume_configuration.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceVolumeConfigurations:
    import capo_ecs.types.service_volume_configuration

    out: ServiceVolumeConfigurations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ecs.types.service_volume_configuration.deserialize_aws_json_1_1(item)
        )
    return out
