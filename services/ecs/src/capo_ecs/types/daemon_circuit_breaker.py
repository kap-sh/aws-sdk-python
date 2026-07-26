"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonCircuitBreaker``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.daemon_deployment_rollback_monitors_status
    import capo_ecs.types.integer


class DaemonCircuitBreaker(TypedDict, closed=True):
    failure_count: "capo_ecs.types.integer.Integer"
    """<p>The number of times the circuit breaker detected a daemon deployment failure.</p>"""
    status: NotRequired[
        "capo_ecs.types.daemon_deployment_rollback_monitors_status.DaemonDeploymentRollbackMonitorsStatus"
    ]
    """<p>The circuit breaker status. Amazon ECS is not using the circuit breaker for daemon deployment failures when the status is <code>DISABLED</code>.</p>"""
    threshold: "capo_ecs.types.integer.Integer"
    """<p>The threshold which determines that the daemon deployment failed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonCircuitBreaker) -> dict:
    out: dict = {}
    out["failureCount"] = value.get("failure_count", 0)
    if "status" in value:
        import capo_ecs.types.daemon_deployment_rollback_monitors_status

        out["status"] = (
            capo_ecs.types.daemon_deployment_rollback_monitors_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    out["threshold"] = value.get("threshold", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> DaemonCircuitBreaker:
    out: DaemonCircuitBreaker = {}  # type: ignore[typeddict-item]
    if "failureCount" in data:
        out["failure_count"] = data["failureCount"]
    else:
        out["failure_count"] = 0
    if "status" in data:
        import capo_ecs.types.daemon_deployment_rollback_monitors_status

        out["status"] = (
            capo_ecs.types.daemon_deployment_rollback_monitors_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "threshold" in data:
        out["threshold"] = data["threshold"]
    else:
        out["threshold"] = 0
    return out
