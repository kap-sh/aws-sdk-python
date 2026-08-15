"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentCircuitBreaker``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boolean
    import capo_ecs.types.boxed_boolean
    import capo_ecs.types.threshold_configuration


class DeploymentCircuitBreaker(TypedDict, closed=True):
    enable: "capo_ecs.types.boolean.Boolean"
    """<p>Determines whether to use the deployment circuit breaker logic for the service.</p>"""
    rollback: "capo_ecs.types.boolean.Boolean"
    """<p>Determines whether to configure Amazon ECS to roll back the service if a service deployment fails. If rollback is on, when a service deployment fails, the service is rolled back to the last deployment that completed successfully.</p>"""
    reset_on_healthy_task: NotRequired["capo_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>Specifies whether the deployment circuit breaker resets its failure count when a task reaches a healthy state. When set to <code>true</code>, a task that reaches a healthy state resets the failure count to <code>0</code>. When set to <code>false</code>, Amazon ECS does not reset the failure count. The default is <code>true</code>.</p>"""
    threshold_configuration: NotRequired[
        "capo_ecs.types.threshold_configuration.ThresholdConfiguration"
    ]
    """<p>The threshold configuration that controls when the deployment circuit breaker triggers. The <code>type</code> and <code>value</code> together determine how many task failures are tolerated before the circuit breaker activates.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentCircuitBreaker) -> dict:
    out: dict = {}
    out["enable"] = value.get("enable", False)
    out["rollback"] = value.get("rollback", False)
    if "reset_on_healthy_task" in value:
        out["resetOnHealthyTask"] = value["reset_on_healthy_task"]
    if "threshold_configuration" in value:
        import capo_ecs.types.threshold_configuration

        out["thresholdConfiguration"] = (
            capo_ecs.types.threshold_configuration.serialize_aws_json_1_1(
                value["threshold_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeploymentCircuitBreaker:
    out: DeploymentCircuitBreaker = {}  # type: ignore[typeddict-item]
    if "enable" in data:
        out["enable"] = data["enable"]
    else:
        out["enable"] = False
    if "rollback" in data:
        out["rollback"] = data["rollback"]
    else:
        out["rollback"] = False
    if "resetOnHealthyTask" in data:
        out["reset_on_healthy_task"] = data["resetOnHealthyTask"]
    if "thresholdConfiguration" in data:
        import capo_ecs.types.threshold_configuration

        out["threshold_configuration"] = (
            capo_ecs.types.threshold_configuration.deserialize_aws_json_1_1(
                data["thresholdConfiguration"]
            )
        )
    return out
