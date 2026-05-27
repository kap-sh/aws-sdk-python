"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceDeployments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service_deployment

ServiceDeployments: TypeAlias = list[
    "aws_sdk_ecs.types.service_deployment.ServiceDeployment"
]
