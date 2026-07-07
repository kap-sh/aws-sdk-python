"""Generated from Smithy shape ``com.amazonaws.ecs#DeregisterContainerInstanceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.container_instance


class DeregisterContainerInstanceResponse(TypedDict, closed=True):
    container_instance: NotRequired[
        "aws_sdk_ecs.types.container_instance.ContainerInstance"
    ]
    """<p>The container instance that was deregistered.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterContainerInstanceResponse) -> dict:
    out: dict = {}
    if "container_instance" in value:
        import aws_sdk_ecs.types.container_instance

        out["containerInstance"] = (
            aws_sdk_ecs.types.container_instance.serialize_aws_json_1_1(
                value["container_instance"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterContainerInstanceResponse:
    out: DeregisterContainerInstanceResponse = {}  # type: ignore[typeddict-item]
    if "containerInstance" in data:
        import aws_sdk_ecs.types.container_instance

        out["container_instance"] = (
            aws_sdk_ecs.types.container_instance.deserialize_aws_json_1_1(
                data["containerInstance"]
            )
        )
    return out
