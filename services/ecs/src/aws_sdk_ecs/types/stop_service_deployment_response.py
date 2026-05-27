"""Generated from Smithy shape ``com.amazonaws.ecs#StopServiceDeploymentResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class StopServiceDeploymentResponse(TypedDict):
    service_deployment_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the stopped service deployment.</p>"""
