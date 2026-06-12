"""Generated from Smithy shape ``com.amazonaws.lightsail#DeleteContainerImageRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.container_service_name
    import aws_sdk_lightsail.types.string


class DeleteContainerImageRequest(TypedDict):
    service_name: "aws_sdk_lightsail.types.container_service_name.ContainerServiceName"
    """<p>The name of the container service for which to delete a registered container image.</p>"""
    image: "aws_sdk_lightsail.types.string.string"
    """<p>The name of the container image to delete from the container service.</p> <p>Use the <code>GetContainerImages</code> action to get the name of the container images that are registered to a container service.</p> <note> <p>Container images sourced from your Lightsail container service, that are registered and stored on your service, start with a colon (<code>:</code>). For example, <code>:container-service-1.mystaticwebsite.1</code>. Container images sourced from a public registry like Docker Hub don't start with a colon. For example, <code>nginx:latest</code> or <code>nginx</code>.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteContainerImageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteContainerImageRequest:
    out: DeleteContainerImageRequest = {}  # type: ignore[typeddict-item]
    return out
