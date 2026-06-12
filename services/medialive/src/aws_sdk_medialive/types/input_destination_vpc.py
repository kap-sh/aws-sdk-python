"""Generated from Smithy shape ``com.amazonaws.medialive#InputDestinationVpc``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class InputDestinationVpc(TypedDict):
    availability_zone: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The availability zone of the Input destination."""
    network_interface_id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The network interface ID of the Input destination in the VPC."""


# --- restJson1 ser/de ---
def serialize_json(value: InputDestinationVpc) -> dict:
    out: dict = {}
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "network_interface_id" in value:
        out["networkInterfaceId"] = value["network_interface_id"]
    return out


def deserialize_json(data: dict) -> InputDestinationVpc:
    out: InputDestinationVpc = {}  # type: ignore[typeddict-item]
    if "availabilityZone" in data:
        out["availability_zone"] = data["availabilityZone"]
    if "networkInterfaceId" in data:
        out["network_interface_id"] = data["networkInterfaceId"]
    return out
