"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServiceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.container_service

ContainerServiceList: TypeAlias = list[
    "aws_sdk_lightsail.types.container_service.ContainerService"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerServiceList) -> list:
    import aws_sdk_lightsail.types.container_service

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lightsail.types.container_service.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerServiceList:
    import aws_sdk_lightsail.types.container_service

    out: ContainerServiceList = []
    for item in data:
        out.append(
            aws_sdk_lightsail.types.container_service.deserialize_aws_json_1_1(item)
        )
    return out
