"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServiceDeploymentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.container_service_deployment

ContainerServiceDeploymentList: TypeAlias = list[
    "aws_sdk_lightsail.types.container_service_deployment.ContainerServiceDeployment"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerServiceDeploymentList) -> list:
    import aws_sdk_lightsail.types.container_service_deployment

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lightsail.types.container_service_deployment.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerServiceDeploymentList:
    import aws_sdk_lightsail.types.container_service_deployment

    out: ContainerServiceDeploymentList = []
    for item in data:
        out.append(
            aws_sdk_lightsail.types.container_service_deployment.deserialize_aws_json_1_1(
                item
            )
        )
    return out
