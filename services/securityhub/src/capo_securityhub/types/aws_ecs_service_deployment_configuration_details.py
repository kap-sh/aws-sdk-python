"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsServiceDeploymentConfigurationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ecs_service_deployment_configuration_deployment_circuit_breaker_details
    import capo_securityhub.types.integer


class AwsEcsServiceDeploymentConfigurationDetails(TypedDict, closed=True):
    deployment_circuit_breaker: NotRequired[
        "capo_securityhub.types.aws_ecs_service_deployment_configuration_deployment_circuit_breaker_details.AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetails"
    ]
    """<p>Determines whether a service deployment fails if a service cannot reach a steady state.</p>"""
    maximum_percent: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>For a service that uses the rolling update (<code>ECS</code>) deployment type, the maximum number of tasks in a service that are allowed in the <code>RUNNING</code> or <code>PENDING</code> state during a deployment, and for tasks that use the EC2 launch type, when any container instances are in the <code>DRAINING</code> state. Provided as a percentage of the desired number of tasks. The default value is 200%.</p> <p>For a service that uses the blue/green (<code>CODE_DEPLOY</code>) or <code>EXTERNAL</code> deployment types, and tasks that use the EC2 launch type, the maximum number of tasks in the service that remain in the <code>RUNNING</code> state while the container instances are in the <code>DRAINING</code> state.</p> <p>For the Fargate launch type, the maximum percent value is not used.</p>"""
    minimum_healthy_percent: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>For a service that uses the rolling update (<code>ECS</code>) deployment type, the minimum number of tasks in a service that must remain in the <code>RUNNING</code> state during a deployment, and while any container instances are in the <code>DRAINING</code> state if the service contains tasks using the EC2 launch type. Expressed as a percentage of the desired number of tasks. The default value is 100%.</p> <p>For a service that uses the blue/green (<code>CODE_DEPLOY</code>) or <code>EXTERNAL</code> deployment types and tasks that use the EC2 launch type, the minimum number of the tasks in the service that remain in the <code>RUNNING</code> state while the container instances are in the <code>DRAINING</code> state.</p> <p>For the Fargate launch type, the minimum healthy percent value is not used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsServiceDeploymentConfigurationDetails) -> dict:
    out: dict = {}
    if "deployment_circuit_breaker" in value:
        import capo_securityhub.types.aws_ecs_service_deployment_configuration_deployment_circuit_breaker_details

        out["DeploymentCircuitBreaker"] = (
            capo_securityhub.types.aws_ecs_service_deployment_configuration_deployment_circuit_breaker_details.serialize_json(
                value["deployment_circuit_breaker"]
            )
        )
    if "maximum_percent" in value:
        out["MaximumPercent"] = value["maximum_percent"]
    if "minimum_healthy_percent" in value:
        out["MinimumHealthyPercent"] = value["minimum_healthy_percent"]
    return out


def deserialize_json(data: dict) -> AwsEcsServiceDeploymentConfigurationDetails:
    out: AwsEcsServiceDeploymentConfigurationDetails = {}  # type: ignore[typeddict-item]
    if "DeploymentCircuitBreaker" in data:
        import capo_securityhub.types.aws_ecs_service_deployment_configuration_deployment_circuit_breaker_details

        out["deployment_circuit_breaker"] = (
            capo_securityhub.types.aws_ecs_service_deployment_configuration_deployment_circuit_breaker_details.deserialize_json(
                data["DeploymentCircuitBreaker"]
            )
        )
    if "MaximumPercent" in data:
        out["maximum_percent"] = data["MaximumPercent"]
    if "MinimumHealthyPercent" in data:
        out["minimum_healthy_percent"] = data["MinimumHealthyPercent"]
    return out
