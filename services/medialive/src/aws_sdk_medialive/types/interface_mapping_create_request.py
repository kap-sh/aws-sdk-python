"""Generated from Smithy shape ``com.amazonaws.medialive#InterfaceMappingCreateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class InterfaceMappingCreateRequest(TypedDict):
    logical_interface_name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The logical name for one interface (on every Node) that handles a specific type of traffic. We recommend that the name hints at the physical interface it applies to. For example, it could refer to the traffic that the physical interface handles. For example, my-Inputs-Interface."""
    network_id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The ID of the network that you want to connect to the specified logicalInterfaceName."""


# --- restJson1 ser/de ---
def serialize_json(value: InterfaceMappingCreateRequest) -> dict:
    out: dict = {}
    if "logical_interface_name" in value:
        out["logicalInterfaceName"] = value["logical_interface_name"]
    if "network_id" in value:
        out["networkId"] = value["network_id"]
    return out


def deserialize_json(data: dict) -> InterfaceMappingCreateRequest:
    out: InterfaceMappingCreateRequest = {}  # type: ignore[typeddict-item]
    if "logicalInterfaceName" in data:
        out["logical_interface_name"] = data["logicalInterfaceName"]
    if "networkId" in data:
        out["network_id"] = data["networkId"]
    return out
