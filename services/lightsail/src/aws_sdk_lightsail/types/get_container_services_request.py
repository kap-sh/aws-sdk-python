"""Generated from Smithy shape ``com.amazonaws.lightsail#GetContainerServicesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.container_service_name


class GetContainerServicesRequest(TypedDict):
    service_name: NotRequired[
        "aws_sdk_lightsail.types.container_service_name.ContainerServiceName"
    ]
    """<p>The name of the container service for which to return information.</p> <p>When omitted, the response includes all of your container services in the Amazon Web Services Region where the request is made.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContainerServicesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContainerServicesRequest:
    out: GetContainerServicesRequest = {}  # type: ignore[typeddict-item]
    return out
