"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceDeploymentStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service_deployment_status

ServiceDeploymentStatusList: TypeAlias = list[
    "aws_sdk_ecs.types.service_deployment_status.ServiceDeploymentStatus"
]
