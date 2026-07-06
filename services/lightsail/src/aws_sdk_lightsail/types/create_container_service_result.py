"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateContainerServiceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.container_service


class CreateContainerServiceResult(TypedDict, closed=True):
    container_service: NotRequired[
        "aws_sdk_lightsail.types.container_service.ContainerService"
    ]
    """<p>An object that describes a container service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateContainerServiceResult) -> dict:
    out: dict = {}
    if "container_service" in value:
        import aws_sdk_lightsail.types.container_service

        out["containerService"] = (
            aws_sdk_lightsail.types.container_service.serialize_aws_json_1_1(
                value["container_service"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateContainerServiceResult:
    out: CreateContainerServiceResult = {}  # type: ignore[typeddict-item]
    if "containerService" in data:
        import aws_sdk_lightsail.types.container_service

        out["container_service"] = (
            aws_sdk_lightsail.types.container_service.deserialize_aws_json_1_1(
                data["containerService"]
            )
        )
    return out
