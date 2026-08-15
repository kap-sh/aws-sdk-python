"""Generated from Smithy shape ``com.amazonaws.ecs#ExpressGatewayServiceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.express_gateway_container
    import capo_ecs.types.express_gateway_scaling_target
    import capo_ecs.types.express_gateway_service_network_configuration
    import capo_ecs.types.ingress_path_summaries
    import capo_ecs.types.string
    import capo_ecs.types.timestamp


class ExpressGatewayServiceConfiguration(TypedDict, closed=True):
    service_revision_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The ARN of the service revision.</p>"""
    execution_role_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The ARN of the task execution role for the service revision.</p>"""
    task_role_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The ARN of the task role for the service revision.</p>"""
    task_definition_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The ARN of the task definition used by this service revision. This is present for all Express services and reflects the task definition in use, whether managed by Amazon ECS or provided by the customer.</p>"""
    cpu: NotRequired["capo_ecs.types.string.String"]
    """<p>The CPU allocation for tasks in this service revision.</p>"""
    memory: NotRequired["capo_ecs.types.string.String"]
    """<p>The memory allocation for tasks in this service revision.</p>"""
    network_configuration: NotRequired[
        "capo_ecs.types.express_gateway_service_network_configuration.ExpressGatewayServiceNetworkConfiguration"
    ]
    """<p>The network configuration for tasks in this service revision.</p>"""
    health_check_path: NotRequired["capo_ecs.types.string.String"]
    """<p>The health check path for this service revision.</p>"""
    primary_container: NotRequired[
        "capo_ecs.types.express_gateway_container.ExpressGatewayContainer"
    ]
    """<p>The primary container configuration for this service revision.</p>"""
    scaling_target: NotRequired[
        "capo_ecs.types.express_gateway_scaling_target.ExpressGatewayScalingTarget"
    ]
    """<p>The auto-scaling configuration for this service revision.</p>"""
    ingress_paths: NotRequired[
        "capo_ecs.types.ingress_path_summaries.IngressPathSummaries"
    ]
    """<p>The entry point into this service revision.</p>"""
    created_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for when this service revision was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpressGatewayServiceConfiguration) -> dict:
    out: dict = {}
    if "service_revision_arn" in value:
        out["serviceRevisionArn"] = value["service_revision_arn"]
    if "execution_role_arn" in value:
        out["executionRoleArn"] = value["execution_role_arn"]
    if "task_role_arn" in value:
        out["taskRoleArn"] = value["task_role_arn"]
    if "task_definition_arn" in value:
        out["taskDefinitionArn"] = value["task_definition_arn"]
    if "cpu" in value:
        out["cpu"] = value["cpu"]
    if "memory" in value:
        out["memory"] = value["memory"]
    if "network_configuration" in value:
        import capo_ecs.types.express_gateway_service_network_configuration

        out["networkConfiguration"] = (
            capo_ecs.types.express_gateway_service_network_configuration.serialize_aws_json_1_1(
                value["network_configuration"]
            )
        )
    if "health_check_path" in value:
        out["healthCheckPath"] = value["health_check_path"]
    if "primary_container" in value:
        import capo_ecs.types.express_gateway_container

        out["primaryContainer"] = (
            capo_ecs.types.express_gateway_container.serialize_aws_json_1_1(
                value["primary_container"]
            )
        )
    if "scaling_target" in value:
        import capo_ecs.types.express_gateway_scaling_target

        out["scalingTarget"] = (
            capo_ecs.types.express_gateway_scaling_target.serialize_aws_json_1_1(
                value["scaling_target"]
            )
        )
    if "ingress_paths" in value:
        import capo_ecs.types.ingress_path_summaries

        out["ingressPaths"] = (
            capo_ecs.types.ingress_path_summaries.serialize_aws_json_1_1(
                value["ingress_paths"]
            )
        )
    if "created_at" in value:
        import capo_ecs.types.timestamp

        out["createdAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExpressGatewayServiceConfiguration:
    out: ExpressGatewayServiceConfiguration = {}  # type: ignore[typeddict-item]
    if "serviceRevisionArn" in data:
        out["service_revision_arn"] = data["serviceRevisionArn"]
    if "executionRoleArn" in data:
        out["execution_role_arn"] = data["executionRoleArn"]
    if "taskRoleArn" in data:
        out["task_role_arn"] = data["taskRoleArn"]
    if "taskDefinitionArn" in data:
        out["task_definition_arn"] = data["taskDefinitionArn"]
    if "cpu" in data:
        out["cpu"] = data["cpu"]
    if "memory" in data:
        out["memory"] = data["memory"]
    if "networkConfiguration" in data:
        import capo_ecs.types.express_gateway_service_network_configuration

        out["network_configuration"] = (
            capo_ecs.types.express_gateway_service_network_configuration.deserialize_aws_json_1_1(
                data["networkConfiguration"]
            )
        )
    if "healthCheckPath" in data:
        out["health_check_path"] = data["healthCheckPath"]
    if "primaryContainer" in data:
        import capo_ecs.types.express_gateway_container

        out["primary_container"] = (
            capo_ecs.types.express_gateway_container.deserialize_aws_json_1_1(
                data["primaryContainer"]
            )
        )
    if "scalingTarget" in data:
        import capo_ecs.types.express_gateway_scaling_target

        out["scaling_target"] = (
            capo_ecs.types.express_gateway_scaling_target.deserialize_aws_json_1_1(
                data["scalingTarget"]
            )
        )
    if "ingressPaths" in data:
        import capo_ecs.types.ingress_path_summaries

        out["ingress_paths"] = (
            capo_ecs.types.ingress_path_summaries.deserialize_aws_json_1_1(
                data["ingressPaths"]
            )
        )
    if "createdAt" in data:
        import capo_ecs.types.timestamp

        out["created_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    return out
