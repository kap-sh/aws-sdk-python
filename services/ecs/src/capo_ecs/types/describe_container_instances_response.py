"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeContainerInstancesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.container_instances
    import capo_ecs.types.failures


class DescribeContainerInstancesResponse(TypedDict, closed=True):
    container_instances: NotRequired[
        "capo_ecs.types.container_instances.ContainerInstances"
    ]
    """<p>The list of container instances.</p>"""
    failures: NotRequired["capo_ecs.types.failures.Failures"]
    """<p>Any failures associated with the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeContainerInstancesResponse) -> dict:
    out: dict = {}
    if "container_instances" in value:
        import capo_ecs.types.container_instances

        out["containerInstances"] = (
            capo_ecs.types.container_instances.serialize_aws_json_1_1(
                value["container_instances"]
            )
        )
    if "failures" in value:
        import capo_ecs.types.failures

        out["failures"] = capo_ecs.types.failures.serialize_aws_json_1_1(
            value["failures"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeContainerInstancesResponse:
    out: DescribeContainerInstancesResponse = {}  # type: ignore[typeddict-item]
    if "containerInstances" in data:
        import capo_ecs.types.container_instances

        out["container_instances"] = (
            capo_ecs.types.container_instances.deserialize_aws_json_1_1(
                data["containerInstances"]
            )
        )
    if "failures" in data:
        import capo_ecs.types.failures

        out["failures"] = capo_ecs.types.failures.deserialize_aws_json_1_1(
            data["failures"]
        )
    return out
