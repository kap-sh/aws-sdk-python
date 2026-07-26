"""Generated from Smithy shape ``com.amazonaws.lightsail#DeleteContainerServiceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.container_service_name


class DeleteContainerServiceRequest(TypedDict, closed=True):
    service_name: "capo_lightsail.types.container_service_name.ContainerServiceName"
    """<p>The name of the container service to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteContainerServiceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteContainerServiceRequest:
    out: DeleteContainerServiceRequest = {}  # type: ignore[typeddict-item]
    return out
