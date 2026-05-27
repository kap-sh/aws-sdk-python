"""Generated from Smithy shape ``com.amazonaws.ecs#StopServiceDeploymentRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.stop_service_deployment_stop_type
    import aws_sdk_ecs.types.string


class StopServiceDeploymentRequest(TypedDict):
    service_deployment_arn: "aws_sdk_ecs.types.string.String"
    """<p>The ARN of the service deployment that you want to stop.</p>"""
    stop_type: NotRequired[
        "aws_sdk_ecs.types.stop_service_deployment_stop_type.StopServiceDeploymentStopType"
    ]
    """<p>How you want Amazon ECS to stop the service. </p> <p>The valid values are <code>ROLLBACK</code>.</p>"""
