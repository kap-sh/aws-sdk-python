"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceDeploymentCircuitBreaker``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.integer
    import aws_sdk_ecs.types.service_deployment_rollback_monitors_status


class ServiceDeploymentCircuitBreaker(TypedDict):
    status: NotRequired[
        "aws_sdk_ecs.types.service_deployment_rollback_monitors_status.ServiceDeploymentRollbackMonitorsStatus"
    ]
    """<p>The circuit breaker status. Amazon ECS is not using the circuit breaker for service deployment failures when the status is <code>DISABLED</code>.</p>"""
    failure_count: "aws_sdk_ecs.types.integer.Integer"
    """<p>The number of times the circuit breaker detected a service deploymeny failure.</p>"""
    threshold: "aws_sdk_ecs.types.integer.Integer"
    """<p>The threshhold which determines that the service deployment failed.</p> <p>The deployment circuit breaker calculates the threshold value, and then uses the value to determine when to move the deployment to a FAILED state. The deployment circuit breaker has a minimum threshold of 3 and a maximum threshold of 200. and uses the values in the following formula to determine the deployment failure.</p> <p> <code>0.5 * desired task count</code> </p>"""
