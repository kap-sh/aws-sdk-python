"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceDeploymentStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service_deployment_status

ServiceDeploymentStatusList: TypeAlias = list[
    "aws_sdk_ecs.types.service_deployment_status.ServiceDeploymentStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceDeploymentStatusList) -> list:
    import aws_sdk_ecs.types.service_deployment_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ecs.types.service_deployment_status.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceDeploymentStatusList:
    import aws_sdk_ecs.types.service_deployment_status

    out: ServiceDeploymentStatusList = []
    for item in data:
        out.append(
            aws_sdk_ecs.types.service_deployment_status.deserialize_aws_json_1_1(item)
        )
    return out
