"""Generated from Smithy shape ``com.amazonaws.directconnect#AllocatePrivateVirtualInterfaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.connection_id
    import aws_sdk_direct_connect.types.new_private_virtual_interface_allocation
    import aws_sdk_direct_connect.types.owner_account


class AllocatePrivateVirtualInterfaceRequest(TypedDict, closed=True):
    connection_id: "aws_sdk_direct_connect.types.connection_id.ConnectionId"
    """<p>The ID of the connection on which the private virtual interface is provisioned.</p>"""
    owner_account: "aws_sdk_direct_connect.types.owner_account.OwnerAccount"
    """<p>The ID of the Amazon Web Services account that owns the virtual private interface.</p>"""
    new_private_virtual_interface_allocation: "aws_sdk_direct_connect.types.new_private_virtual_interface_allocation.NewPrivateVirtualInterfaceAllocation"
    """<p>Information about the private virtual interface.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AllocatePrivateVirtualInterfaceRequest) -> dict:
    out: dict = {}
    out["connectionId"] = value["connection_id"]
    out["ownerAccount"] = value["owner_account"]
    import aws_sdk_direct_connect.types.new_private_virtual_interface_allocation

    out["newPrivateVirtualInterfaceAllocation"] = (
        aws_sdk_direct_connect.types.new_private_virtual_interface_allocation.serialize_aws_json_1_1(
            value["new_private_virtual_interface_allocation"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AllocatePrivateVirtualInterfaceRequest:
    out: AllocatePrivateVirtualInterfaceRequest = {}  # type: ignore[typeddict-item]
    if "connectionId" in data:
        out["connection_id"] = data["connectionId"]
    else:
        raise DeserializationError(
            "AllocatePrivateVirtualInterfaceRequest.connection_id required"
        )
    if "ownerAccount" in data:
        out["owner_account"] = data["ownerAccount"]
    else:
        raise DeserializationError(
            "AllocatePrivateVirtualInterfaceRequest.owner_account required"
        )
    if "newPrivateVirtualInterfaceAllocation" in data:
        import aws_sdk_direct_connect.types.new_private_virtual_interface_allocation

        out["new_private_virtual_interface_allocation"] = (
            aws_sdk_direct_connect.types.new_private_virtual_interface_allocation.deserialize_aws_json_1_1(
                data["newPrivateVirtualInterfaceAllocation"]
            )
        )
    else:
        raise DeserializationError(
            "AllocatePrivateVirtualInterfaceRequest.new_private_virtual_interface_allocation required"
        )
    return out
