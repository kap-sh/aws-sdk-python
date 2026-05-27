"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceDeploymentsBrief``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service_deployment_brief

ServiceDeploymentsBrief: TypeAlias = list[
    "aws_sdk_ecs.types.service_deployment_brief.ServiceDeploymentBrief"
]
