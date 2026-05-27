"""Generated from Smithy shape ``com.amazonaws.ecs#ExpressGatewayServiceConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.express_gateway_container
    import aws_sdk_ecs.types.express_gateway_scaling_target
    import aws_sdk_ecs.types.express_gateway_service_network_configuration
    import aws_sdk_ecs.types.ingress_path_summaries
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class ExpressGatewayServiceConfiguration(TypedDict):
    service_revision_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the service revision.</p>"""
    execution_role_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the task execution role for the service revision.</p>"""
    task_role_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the task role for the service revision.</p>"""
    cpu: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The CPU allocation for tasks in this service revision.</p>"""
    memory: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The memory allocation for tasks in this service revision.</p>"""
    network_configuration: NotRequired[
        "aws_sdk_ecs.types.express_gateway_service_network_configuration.ExpressGatewayServiceNetworkConfiguration"
    ]
    """<p>The network configuration for tasks in this service revision.</p>"""
    health_check_path: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The health check path for this service revision.</p>"""
    primary_container: NotRequired[
        "aws_sdk_ecs.types.express_gateway_container.ExpressGatewayContainer"
    ]
    """<p>The primary container configuration for this service revision.</p>"""
    scaling_target: NotRequired[
        "aws_sdk_ecs.types.express_gateway_scaling_target.ExpressGatewayScalingTarget"
    ]
    """<p>The auto-scaling configuration for this service revision.</p>"""
    ingress_paths: NotRequired[
        "aws_sdk_ecs.types.ingress_path_summaries.IngressPathSummaries"
    ]
    """<p>The entry point into this service revision.</p>"""
    created_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for when this service revision was created.</p>"""
