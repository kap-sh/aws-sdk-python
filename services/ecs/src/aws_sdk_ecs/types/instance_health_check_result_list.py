"""Generated from Smithy shape ``com.amazonaws.ecs#InstanceHealthCheckResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.instance_health_check_result

InstanceHealthCheckResultList: TypeAlias = list[
    "aws_sdk_ecs.types.instance_health_check_result.InstanceHealthCheckResult"
]
