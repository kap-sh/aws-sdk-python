"""Generated from Smithy shape ``com.amazonaws.lightsail#RegisterContainerImageResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.container_image


class RegisterContainerImageResult(TypedDict, closed=True):
    container_image: NotRequired[
        "aws_sdk_lightsail.types.container_image.ContainerImage"
    ]
    """<p>An object that describes a container image that is registered to a Lightsail container service</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterContainerImageResult) -> dict:
    out: dict = {}
    if "container_image" in value:
        import aws_sdk_lightsail.types.container_image

        out["containerImage"] = (
            aws_sdk_lightsail.types.container_image.serialize_aws_json_1_1(
                value["container_image"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterContainerImageResult:
    out: RegisterContainerImageResult = {}  # type: ignore[typeddict-item]
    if "containerImage" in data:
        import aws_sdk_lightsail.types.container_image

        out["container_image"] = (
            aws_sdk_lightsail.types.container_image.deserialize_aws_json_1_1(
                data["containerImage"]
            )
        )
    return out
