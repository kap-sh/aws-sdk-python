"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentCircuitBreaker``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boolean


class DeploymentCircuitBreaker(TypedDict, closed=True):
    enable: "aws_sdk_ecs.types.boolean.Boolean"
    """<p>Determines whether to use the deployment circuit breaker logic for the service.</p>"""
    rollback: "aws_sdk_ecs.types.boolean.Boolean"
    """<p>Determines whether to configure Amazon ECS to roll back the service if a service deployment fails. If rollback is on, when a service deployment fails, the service is rolled back to the last deployment that completed successfully.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentCircuitBreaker) -> dict:
    out: dict = {}
    out["enable"] = value.get("enable", False)
    out["rollback"] = value.get("rollback", False)
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
    return out
