"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateExpressGatewayServiceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.express_gateway_container
    import capo_ecs.types.express_gateway_scaling_target
    import capo_ecs.types.express_gateway_service_network_configuration
    import capo_ecs.types.string


class UpdateExpressGatewayServiceRequest(TypedDict, closed=True):
    service_arn: "capo_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the Express service to update.</p>"""
    execution_role_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the task execution role for the Express service.</p>"""
    health_check_path: NotRequired["capo_ecs.types.string.String"]
    """<p>The path on the container for Application Load Balancer health checks.</p>"""
    primary_container: NotRequired[
        "capo_ecs.types.express_gateway_container.ExpressGatewayContainer"
    ]
    """<p>The primary container configuration for the Express service.</p>"""
    task_role_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM role for containers in this task.</p>"""
    network_configuration: NotRequired[
        "capo_ecs.types.express_gateway_service_network_configuration.ExpressGatewayServiceNetworkConfiguration"
    ]
    """<p>The network configuration for the Express service tasks. By default, the network configuration for an Express service uses the default VPC.</p>"""
    cpu: NotRequired["capo_ecs.types.string.String"]
    """<p>The number of CPU units used by the task.</p>"""
    memory: NotRequired["capo_ecs.types.string.String"]
    """<p>The amount of memory (in MiB) used by the task.</p>"""
    scaling_target: NotRequired[
        "capo_ecs.types.express_gateway_scaling_target.ExpressGatewayScalingTarget"
    ]
    """<p>The auto-scaling configuration for the Express service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateExpressGatewayServiceRequest) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    if "execution_role_arn" in value:
        out["executionRoleArn"] = value["execution_role_arn"]
    if "health_check_path" in value:
        out["healthCheckPath"] = value["health_check_path"]
    if "primary_container" in value:
        import capo_ecs.types.express_gateway_container

        out["primaryContainer"] = (
            capo_ecs.types.express_gateway_container.serialize_aws_json_1_1(
                value["primary_container"]
            )
        )
    if "task_role_arn" in value:
        out["taskRoleArn"] = value["task_role_arn"]
    if "network_configuration" in value:
        import capo_ecs.types.express_gateway_service_network_configuration

        out["networkConfiguration"] = (
            capo_ecs.types.express_gateway_service_network_configuration.serialize_aws_json_1_1(
                value["network_configuration"]
            )
        )
    if "cpu" in value:
        out["cpu"] = value["cpu"]
    if "memory" in value:
        out["memory"] = value["memory"]
    if "scaling_target" in value:
        import capo_ecs.types.express_gateway_scaling_target

        out["scalingTarget"] = (
            capo_ecs.types.express_gateway_scaling_target.serialize_aws_json_1_1(
                value["scaling_target"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateExpressGatewayServiceRequest:
    out: UpdateExpressGatewayServiceRequest = {}  # type: ignore[typeddict-item]
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    else:
        raise DeserializationError(
            "UpdateExpressGatewayServiceRequest.service_arn required"
        )
    if "executionRoleArn" in data:
        out["execution_role_arn"] = data["executionRoleArn"]
    if "healthCheckPath" in data:
        out["health_check_path"] = data["healthCheckPath"]
    if "primaryContainer" in data:
        import capo_ecs.types.express_gateway_container

        out["primary_container"] = (
            capo_ecs.types.express_gateway_container.deserialize_aws_json_1_1(
                data["primaryContainer"]
            )
        )
    if "taskRoleArn" in data:
        out["task_role_arn"] = data["taskRoleArn"]
    if "networkConfiguration" in data:
        import capo_ecs.types.express_gateway_service_network_configuration

        out["network_configuration"] = (
            capo_ecs.types.express_gateway_service_network_configuration.deserialize_aws_json_1_1(
                data["networkConfiguration"]
            )
        )
    if "cpu" in data:
        out["cpu"] = data["cpu"]
    if "memory" in data:
        out["memory"] = data["memory"]
    if "scalingTarget" in data:
        import capo_ecs.types.express_gateway_scaling_target

        out["scaling_target"] = (
            capo_ecs.types.express_gateway_scaling_target.deserialize_aws_json_1_1(
                data["scalingTarget"]
            )
        )
    return out
