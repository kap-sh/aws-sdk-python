"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonCircuitBreaker``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_deployment_rollback_monitors_status
    import aws_sdk_ecs.types.integer


class DaemonCircuitBreaker(TypedDict):
    failure_count: "aws_sdk_ecs.types.integer.Integer"
    """<p>The number of times the circuit breaker detected a daemon deployment failure.</p>"""
    status: NotRequired[
        "aws_sdk_ecs.types.daemon_deployment_rollback_monitors_status.DaemonDeploymentRollbackMonitorsStatus"
    ]
    """<p>The circuit breaker status. Amazon ECS is not using the circuit breaker for daemon deployment failures when the status is <code>DISABLED</code>.</p>"""
    threshold: "aws_sdk_ecs.types.integer.Integer"
    """<p>The threshold which determines that the daemon deployment failed.</p>"""
