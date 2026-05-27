"""Generated from Smithy shape ``com.amazonaws.ecs#Deployments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.deployment

Deployments: TypeAlias = list["aws_sdk_ecs.types.deployment.Deployment"]
