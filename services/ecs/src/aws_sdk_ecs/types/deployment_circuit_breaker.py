"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentCircuitBreaker``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boolean


class DeploymentCircuitBreaker(TypedDict):
    enable: "aws_sdk_ecs.types.boolean.Boolean"
    """<p>Determines whether to use the deployment circuit breaker logic for the service.</p>"""
    rollback: "aws_sdk_ecs.types.boolean.Boolean"
    """<p>Determines whether to configure Amazon ECS to roll back the service if a service deployment fails. If rollback is on, when a service deployment fails, the service is rolled back to the last deployment that completed successfully.</p>"""
