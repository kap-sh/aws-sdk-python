"""Generated from Smithy shape ``com.amazonaws.ecs#CreateExpressGatewayServiceRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.express_gateway_container
    import aws_sdk_ecs.types.express_gateway_scaling_target
    import aws_sdk_ecs.types.express_gateway_service_network_configuration
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.tags


class CreateExpressGatewayServiceRequest(TypedDict):
    execution_role_arn: "aws_sdk_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the task execution role that grants the Amazon ECS container agent permission to make Amazon Web Services API calls on your behalf. This role is required for Amazon ECS to pull container images from Amazon ECR, send container logs to Amazon CloudWatch Logs, and retrieve sensitive data from Amazon Web Services Systems Manager Parameter Store or Amazon Web Services Secrets Manager.</p> <p>The execution role must include the <code>AmazonECSTaskExecutionRolePolicy</code> managed policy or equivalent permissions. For Express services, this role is used during task startup and runtime for container management operations.</p>"""
    infrastructure_role_arn: "aws_sdk_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the infrastructure role that grants Amazon ECS permission to create and manage Amazon Web Services resources on your behalf for the Express service. This role is used to provision and manage Application Load Balancers, target groups, security groups, auto-scaling policies, and other Amazon Web Services infrastructure components.</p> <p>The infrastructure role must include permissions for Elastic Load Balancing, Application Auto Scaling, Amazon EC2 (for security groups), and other services required for managed infrastructure. This role is only used during Express service creation, updates, and deletion operations.</p>"""
    service_name: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of the Express service. This name must be unique within the specified cluster and can contain up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens. The name is used to identify the service in the Amazon ECS console and API operations.</p> <p>If you don't specify a service name, Amazon ECS generates a unique name for the service. The service name becomes part of the service ARN and cannot be changed after the service is created.</p>"""
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster on which to create the Express service. If you do not specify a cluster, the <code>default</code> cluster is assumed.</p>"""
    health_check_path: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The path on the container that the Application Load Balancer uses for health checks. This should be a valid HTTP endpoint that returns a successful response (HTTP 200) when the application is healthy.</p> <p>If not specified, the default health check path is <code>/ping</code>. The health check path must start with a forward slash and can include query parameters. Examples: <code>/health</code>, <code>/api/status</code>, <code>/ping?format=json</code>.</p>"""
    primary_container: (
        "aws_sdk_ecs.types.express_gateway_container.ExpressGatewayContainer"
    )
    """<p>The primary container configuration for the Express service. This defines the main application container that will receive traffic from the Application Load Balancer.</p> <p>The primary container must specify at minimum a container image. You can also configure the container port (defaults to 80), logging configuration, environment variables, secrets, and startup commands. The container image can be from Amazon ECR, Docker Hub, or any other container registry accessible to your execution role.</p>"""
    task_role_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. This role allows your application code to access other Amazon Web Services services securely.</p> <p>The task role is different from the execution role. While the execution role is used by the Amazon ECS agent to set up the task, the task role is used by your application code running inside the container to make Amazon Web Services API calls. If your application doesn't need to access Amazon Web Services services, you can omit this parameter.</p>"""
    network_configuration: NotRequired[
        "aws_sdk_ecs.types.express_gateway_service_network_configuration.ExpressGatewayServiceNetworkConfiguration"
    ]
    """<p>The network configuration for the Express service tasks. This specifies the VPC subnets and security groups for the tasks.</p> <p>For Express services, you can specify custom security groups and subnets. If not provided, Amazon ECS will use the default VPC configuration and create appropriate security groups automatically. The network configuration determines how your service integrates with your VPC and what network access it has.</p>"""
    cpu: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The number of CPU units used by the task. This parameter determines the CPU allocation for each task in the Express service. The default value for an Express service is 256 (.25 vCPU).</p>"""
    memory: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The amount of memory (in MiB) used by the task. This parameter determines the memory allocation for each task in the Express service. The default value for an express service is 512 MiB.</p>"""
    scaling_target: NotRequired[
        "aws_sdk_ecs.types.express_gateway_scaling_target.ExpressGatewayScalingTarget"
    ]
    """<p>The auto-scaling configuration for the Express service. This defines how the service automatically adjusts the number of running tasks based on demand.</p> <p>You can specify the minimum and maximum number of tasks, the scaling metric (CPU utilization, memory utilization, or request count per target), and the target value for the metric. If not specified, the default target value for an Express service is 60.</p>"""
    tags: NotRequired["aws_sdk_ecs.types.tags.Tags"]
    """<p>The metadata that you apply to the Express service to help categorize and organize it. Each tag consists of a key and an optional value. You can apply up to 50 tags to a service.</p>"""
