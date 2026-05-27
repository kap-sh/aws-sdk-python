"""Generated from Smithy shape ``com.amazonaws.ecs#ExpressGatewayContainer``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer
    import aws_sdk_ecs.types.environment_variables
    import aws_sdk_ecs.types.express_gateway_repository_credentials
    import aws_sdk_ecs.types.express_gateway_service_aws_logs_configuration
    import aws_sdk_ecs.types.secret_list
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list


class ExpressGatewayContainer(TypedDict):
    image: "aws_sdk_ecs.types.string.String"
    """<p>The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with either <code>repository-url/image:tag</code> or <code>repository-url/image@digest</code>.</p> <p>For Express services, the image typically contains a web application that listens on the specified container port. The image can be stored in Amazon ECR, Docker Hub, or any other container registry accessible to your execution role.</p>"""
    container_port: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The port number on the container that receives traffic from the load balancer. Default is 80.</p>"""
    aws_logs_configuration: NotRequired[
        "aws_sdk_ecs.types.express_gateway_service_aws_logs_configuration.ExpressGatewayServiceAwsLogsConfiguration"
    ]
    """<p>The log configuration for the container.</p>"""
    repository_credentials: NotRequired[
        "aws_sdk_ecs.types.express_gateway_repository_credentials.ExpressGatewayRepositoryCredentials"
    ]
    """<p>The configuration for repository credentials for private registry authentication.</p>"""
    command: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>The command that is passed to the container.</p>"""
    environment: NotRequired[
        "aws_sdk_ecs.types.environment_variables.EnvironmentVariables"
    ]
    """<p>The environment variables to pass to the container.</p>"""
    secrets: NotRequired["aws_sdk_ecs.types.secret_list.SecretList"]
    """<p>The secrets to pass to the container.</p>"""
