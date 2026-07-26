"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServiceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.container_service

ContainerServiceList: TypeAlias = list[
    "capo_lightsail.types.container_service.ContainerService"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerServiceList) -> list:
    import capo_lightsail.types.container_service

    out: list = []
    for item in value:
        out.append(capo_lightsail.types.container_service.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerServiceList:
    import capo_lightsail.types.container_service

    out: ContainerServiceList = []
    for item in data:
        out.append(
            capo_lightsail.types.container_service.deserialize_aws_json_1_1(item)
        )
    return out
