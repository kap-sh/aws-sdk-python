"""Generated from Smithy shape ``com.amazonaws.directconnect#AssociateVirtualInterfaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.connection_id
    import aws_sdk_direct_connect.types.virtual_interface_id


class AssociateVirtualInterfaceRequest(TypedDict, closed=True):
    virtual_interface_id: (
        "aws_sdk_direct_connect.types.virtual_interface_id.VirtualInterfaceId"
    )
    """<p>The ID of the virtual interface.</p>"""
    connection_id: "aws_sdk_direct_connect.types.connection_id.ConnectionId"
    """<p>The ID of the LAG or connection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateVirtualInterfaceRequest) -> dict:
    out: dict = {}
    out["virtualInterfaceId"] = value["virtual_interface_id"]
    out["connectionId"] = value["connection_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateVirtualInterfaceRequest:
    out: AssociateVirtualInterfaceRequest = {}  # type: ignore[typeddict-item]
    if "virtualInterfaceId" in data:
        out["virtual_interface_id"] = data["virtualInterfaceId"]
    else:
        raise DeserializationError(
            "AssociateVirtualInterfaceRequest.virtual_interface_id required"
        )
    if "connectionId" in data:
        out["connection_id"] = data["connectionId"]
    else:
        raise DeserializationError(
            "AssociateVirtualInterfaceRequest.connection_id required"
        )
    return out
