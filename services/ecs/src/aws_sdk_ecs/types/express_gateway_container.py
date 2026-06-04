"""Generated from Smithy shape ``com.amazonaws.ecs#ExpressGatewayContainer``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ecs.errors import DeserializationError

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


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpressGatewayContainer) -> dict:
    out: dict = {}
    out["image"] = value["image"]
    if "container_port" in value:
        out["containerPort"] = value["container_port"]
    if "aws_logs_configuration" in value:
        import aws_sdk_ecs.types.express_gateway_service_aws_logs_configuration

        out["awsLogsConfiguration"] = (
            aws_sdk_ecs.types.express_gateway_service_aws_logs_configuration.serialize_aws_json_1_1(
                value["aws_logs_configuration"]
            )
        )
    if "repository_credentials" in value:
        import aws_sdk_ecs.types.express_gateway_repository_credentials

        out["repositoryCredentials"] = (
            aws_sdk_ecs.types.express_gateway_repository_credentials.serialize_aws_json_1_1(
                value["repository_credentials"]
            )
        )
    if "command" in value:
        import aws_sdk_ecs.types.string_list

        out["command"] = aws_sdk_ecs.types.string_list.serialize_aws_json_1_1(
            value["command"]
        )
    if "environment" in value:
        import aws_sdk_ecs.types.environment_variables

        out["environment"] = (
            aws_sdk_ecs.types.environment_variables.serialize_aws_json_1_1(
                value["environment"]
            )
        )
    if "secrets" in value:
        import aws_sdk_ecs.types.secret_list

        out["secrets"] = aws_sdk_ecs.types.secret_list.serialize_aws_json_1_1(
            value["secrets"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExpressGatewayContainer:
    out: ExpressGatewayContainer = {}  # type: ignore[typeddict-item]
    if "image" in data:
        out["image"] = data["image"]
    else:
        raise DeserializationError("ExpressGatewayContainer.image required")
    if "containerPort" in data:
        out["container_port"] = data["containerPort"]
    if "awsLogsConfiguration" in data:
        import aws_sdk_ecs.types.express_gateway_service_aws_logs_configuration

        out["aws_logs_configuration"] = (
            aws_sdk_ecs.types.express_gateway_service_aws_logs_configuration.deserialize_aws_json_1_1(
                data["awsLogsConfiguration"]
            )
        )
    if "repositoryCredentials" in data:
        import aws_sdk_ecs.types.express_gateway_repository_credentials

        out["repository_credentials"] = (
            aws_sdk_ecs.types.express_gateway_repository_credentials.deserialize_aws_json_1_1(
                data["repositoryCredentials"]
            )
        )
    if "command" in data:
        import aws_sdk_ecs.types.string_list

        out["command"] = aws_sdk_ecs.types.string_list.deserialize_aws_json_1_1(
            data["command"]
        )
    if "environment" in data:
        import aws_sdk_ecs.types.environment_variables

        out["environment"] = (
            aws_sdk_ecs.types.environment_variables.deserialize_aws_json_1_1(
                data["environment"]
            )
        )
    if "secrets" in data:
        import aws_sdk_ecs.types.secret_list

        out["secrets"] = aws_sdk_ecs.types.secret_list.deserialize_aws_json_1_1(
            data["secrets"]
        )
    return out
