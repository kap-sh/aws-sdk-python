"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceDeploymentBrief``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service_deployment_status
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class ServiceDeploymentBrief(TypedDict):
    service_deployment_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the service deployment.</p>"""
    service_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the service for this service deployment.</p>"""
    cluster_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the cluster that hosts the service.</p>"""
    started_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The time that the service deployment statred. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p>"""
    created_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The time that the service deployment was created. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p>"""
    finished_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The time that the service deployment completed. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p>"""
    target_service_revision_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the service revision being deplyed.</p>"""
    status: NotRequired[
        "aws_sdk_ecs.types.service_deployment_status.ServiceDeploymentStatus"
    ]
    """<p>The status of the service deployment</p>"""
    status_reason: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>Information about why the service deployment is in the current status. For example, the circuit breaker detected a deployment failure.</p>"""
