"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateContainerServiceDeploymentResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.container_service


class CreateContainerServiceDeploymentResult(TypedDict, closed=True):
    container_service: NotRequired[
        "capo_lightsail.types.container_service.ContainerService"
    ]
    """<p>An object that describes a container service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateContainerServiceDeploymentResult) -> dict:
    out: dict = {}
    if "container_service" in value:
        import capo_lightsail.types.container_service

        out["containerService"] = (
            capo_lightsail.types.container_service.serialize_aws_json_1_1(
                value["container_service"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateContainerServiceDeploymentResult:
    out: CreateContainerServiceDeploymentResult = {}  # type: ignore[typeddict-item]
    if "containerService" in data:
        import capo_lightsail.types.container_service

        out["container_service"] = (
            capo_lightsail.types.container_service.deserialize_aws_json_1_1(
                data["containerService"]
            )
        )
    return out
