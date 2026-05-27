"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateExpressGatewayServiceRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.express_gateway_container
    import aws_sdk_ecs.types.express_gateway_scaling_target
    import aws_sdk_ecs.types.express_gateway_service_network_configuration
    import aws_sdk_ecs.types.string


class UpdateExpressGatewayServiceRequest(TypedDict):
    service_arn: "aws_sdk_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the Express service to update.</p>"""
    execution_role_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the task execution role for the Express service.</p>"""
    health_check_path: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The path on the container for Application Load Balancer health checks.</p>"""
    primary_container: NotRequired[
        "aws_sdk_ecs.types.express_gateway_container.ExpressGatewayContainer"
    ]
    """<p>The primary container configuration for the Express service.</p>"""
    task_role_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM role for containers in this task.</p>"""
    network_configuration: NotRequired[
        "aws_sdk_ecs.types.express_gateway_service_network_configuration.ExpressGatewayServiceNetworkConfiguration"
    ]
    """<p>The network configuration for the Express service tasks. By default, the network configuration for an Express service uses the default VPC.</p>"""
    cpu: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The number of CPU units used by the task.</p>"""
    memory: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The amount of memory (in MiB) used by the task.</p>"""
    scaling_target: NotRequired[
        "aws_sdk_ecs.types.express_gateway_scaling_target.ExpressGatewayScalingTarget"
    ]
    """<p>The auto-scaling configuration for the Express service.</p>"""
