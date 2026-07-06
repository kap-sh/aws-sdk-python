"""Generated from Smithy shape ``com.amazonaws.directconnect#AllocatePublicVirtualInterfaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.connection_id
    import aws_sdk_direct_connect.types.new_public_virtual_interface_allocation
    import aws_sdk_direct_connect.types.owner_account


class AllocatePublicVirtualInterfaceRequest(TypedDict, closed=True):
    connection_id: "aws_sdk_direct_connect.types.connection_id.ConnectionId"
    """<p>The ID of the connection on which the public virtual interface is provisioned.</p>"""
    owner_account: "aws_sdk_direct_connect.types.owner_account.OwnerAccount"
    """<p>The ID of the Amazon Web Services account that owns the public virtual interface.</p>"""
    new_public_virtual_interface_allocation: "aws_sdk_direct_connect.types.new_public_virtual_interface_allocation.NewPublicVirtualInterfaceAllocation"
    """<p>Information about the public virtual interface.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AllocatePublicVirtualInterfaceRequest) -> dict:
    out: dict = {}
    out["connectionId"] = value["connection_id"]
    out["ownerAccount"] = value["owner_account"]
    import aws_sdk_direct_connect.types.new_public_virtual_interface_allocation

    out["newPublicVirtualInterfaceAllocation"] = (
        aws_sdk_direct_connect.types.new_public_virtual_interface_allocation.serialize_aws_json_1_1(
            value["new_public_virtual_interface_allocation"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AllocatePublicVirtualInterfaceRequest:
    out: AllocatePublicVirtualInterfaceRequest = {}  # type: ignore[typeddict-item]
    if "connectionId" in data:
        out["connection_id"] = data["connectionId"]
    else:
        raise DeserializationError(
            "AllocatePublicVirtualInterfaceRequest.connection_id required"
        )
    if "ownerAccount" in data:
        out["owner_account"] = data["ownerAccount"]
    else:
        raise DeserializationError(
            "AllocatePublicVirtualInterfaceRequest.owner_account required"
        )
    if "newPublicVirtualInterfaceAllocation" in data:
        import aws_sdk_direct_connect.types.new_public_virtual_interface_allocation

        out["new_public_virtual_interface_allocation"] = (
            aws_sdk_direct_connect.types.new_public_virtual_interface_allocation.deserialize_aws_json_1_1(
                data["newPublicVirtualInterfaceAllocation"]
            )
        )
    else:
        raise DeserializationError(
            "AllocatePublicVirtualInterfaceRequest.new_public_virtual_interface_allocation required"
        )
    return out
