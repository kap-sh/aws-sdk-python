"""Generated from Smithy shape ``com.amazonaws.lightsail#GetContainerImagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.container_service_name


class GetContainerImagesRequest(TypedDict, closed=True):
    service_name: "aws_sdk_lightsail.types.container_service_name.ContainerServiceName"
    """<p>The name of the container service for which to return registered container images.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContainerImagesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContainerImagesRequest:
    out: GetContainerImagesRequest = {}  # type: ignore[typeddict-item]
    return out
