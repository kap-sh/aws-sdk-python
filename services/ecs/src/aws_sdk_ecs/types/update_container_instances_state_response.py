"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateContainerInstancesStateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.container_instances
    import aws_sdk_ecs.types.failures


class UpdateContainerInstancesStateResponse(TypedDict):
    container_instances: NotRequired[
        "aws_sdk_ecs.types.container_instances.ContainerInstances"
    ]
    """<p>The list of container instances.</p>"""
    failures: NotRequired["aws_sdk_ecs.types.failures.Failures"]
    """<p>Any failures associated with the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateContainerInstancesStateResponse) -> dict:
    out: dict = {}
    if "container_instances" in value:
        import aws_sdk_ecs.types.container_instances

        out["containerInstances"] = (
            aws_sdk_ecs.types.container_instances.serialize_aws_json_1_1(
                value["container_instances"]
            )
        )
    if "failures" in value:
        import aws_sdk_ecs.types.failures

        out["failures"] = aws_sdk_ecs.types.failures.serialize_aws_json_1_1(
            value["failures"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateContainerInstancesStateResponse:
    out: UpdateContainerInstancesStateResponse = {}  # type: ignore[typeddict-item]
    if "containerInstances" in data:
        import aws_sdk_ecs.types.container_instances

        out["container_instances"] = (
            aws_sdk_ecs.types.container_instances.deserialize_aws_json_1_1(
                data["containerInstances"]
            )
        )
    if "failures" in data:
        import aws_sdk_ecs.types.failures

        out["failures"] = aws_sdk_ecs.types.failures.deserialize_aws_json_1_1(
            data["failures"]
        )
    return out
