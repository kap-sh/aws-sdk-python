"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerInstanceHealthStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.instance_health_check_result_list
    import aws_sdk_ecs.types.instance_health_check_state


class ContainerInstanceHealthStatus(TypedDict):
    overall_status: NotRequired[
        "aws_sdk_ecs.types.instance_health_check_state.InstanceHealthCheckState"
    ]
    """<p>The overall health status of the container instance. This is an aggregate status of all container instance health checks.</p>"""
    details: NotRequired[
        "aws_sdk_ecs.types.instance_health_check_result_list.InstanceHealthCheckResultList"
    ]
    """<p>An array of objects representing the details of the container instance health status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerInstanceHealthStatus) -> dict:
    out: dict = {}
    if "overall_status" in value:
        import aws_sdk_ecs.types.instance_health_check_state

        out["overallStatus"] = (
            aws_sdk_ecs.types.instance_health_check_state.serialize_aws_json_1_1(
                value["overall_status"]
            )
        )
    if "details" in value:
        import aws_sdk_ecs.types.instance_health_check_result_list

        out["details"] = (
            aws_sdk_ecs.types.instance_health_check_result_list.serialize_aws_json_1_1(
                value["details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerInstanceHealthStatus:
    out: ContainerInstanceHealthStatus = {}  # type: ignore[typeddict-item]
    if "overallStatus" in data:
        import aws_sdk_ecs.types.instance_health_check_state

        out["overall_status"] = (
            aws_sdk_ecs.types.instance_health_check_state.deserialize_aws_json_1_1(
                data["overallStatus"]
            )
        )
    if "details" in data:
        import aws_sdk_ecs.types.instance_health_check_result_list

        out["details"] = (
            aws_sdk_ecs.types.instance_health_check_result_list.deserialize_aws_json_1_1(
                data["details"]
            )
        )
    return out
