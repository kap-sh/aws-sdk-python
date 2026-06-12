"""Generated from Smithy shape ``com.amazonaws.lightsail#GetContainerImagesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.container_image_list


class GetContainerImagesResult(TypedDict):
    container_images: NotRequired[
        "aws_sdk_lightsail.types.container_image_list.ContainerImageList"
    ]
    """<p>An array of objects that describe container images that are registered to the container service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContainerImagesResult) -> dict:
    out: dict = {}
    if "container_images" in value:
        import aws_sdk_lightsail.types.container_image_list

        out["containerImages"] = (
            aws_sdk_lightsail.types.container_image_list.serialize_aws_json_1_1(
                value["container_images"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContainerImagesResult:
    out: GetContainerImagesResult = {}  # type: ignore[typeddict-item]
    if "containerImages" in data:
        import aws_sdk_lightsail.types.container_image_list

        out["container_images"] = (
            aws_sdk_lightsail.types.container_image_list.deserialize_aws_json_1_1(
                data["containerImages"]
            )
        )
    return out
