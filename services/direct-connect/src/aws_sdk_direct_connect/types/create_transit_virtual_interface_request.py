"""Generated from Smithy shape ``com.amazonaws.directconnect#CreateTransitVirtualInterfaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.connection_id
    import aws_sdk_direct_connect.types.new_transit_virtual_interface


class CreateTransitVirtualInterfaceRequest(TypedDict, closed=True):
    connection_id: "aws_sdk_direct_connect.types.connection_id.ConnectionId"
    """<p>The ID of the connection.</p>"""
    new_transit_virtual_interface: "aws_sdk_direct_connect.types.new_transit_virtual_interface.NewTransitVirtualInterface"
    """<p>Information about the transit virtual interface.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTransitVirtualInterfaceRequest) -> dict:
    out: dict = {}
    out["connectionId"] = value["connection_id"]
    import aws_sdk_direct_connect.types.new_transit_virtual_interface

    out["newTransitVirtualInterface"] = (
        aws_sdk_direct_connect.types.new_transit_virtual_interface.serialize_aws_json_1_1(
            value["new_transit_virtual_interface"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTransitVirtualInterfaceRequest:
    out: CreateTransitVirtualInterfaceRequest = {}  # type: ignore[typeddict-item]
    if "connectionId" in data:
        out["connection_id"] = data["connectionId"]
    else:
        raise DeserializationError(
            "CreateTransitVirtualInterfaceRequest.connection_id required"
        )
    if "newTransitVirtualInterface" in data:
        import aws_sdk_direct_connect.types.new_transit_virtual_interface

        out["new_transit_virtual_interface"] = (
            aws_sdk_direct_connect.types.new_transit_virtual_interface.deserialize_aws_json_1_1(
                data["newTransitVirtualInterface"]
            )
        )
    else:
        raise DeserializationError(
            "CreateTransitVirtualInterfaceRequest.new_transit_virtual_interface required"
        )
    return out
