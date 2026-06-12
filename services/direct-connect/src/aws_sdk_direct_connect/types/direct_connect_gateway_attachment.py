"""Generated from Smithy shape ``com.amazonaws.directconnect#DirectConnectGatewayAttachment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.direct_connect_gateway_attachment_state
    import aws_sdk_direct_connect.types.direct_connect_gateway_attachment_type
    import aws_sdk_direct_connect.types.direct_connect_gateway_id
    import aws_sdk_direct_connect.types.owner_account
    import aws_sdk_direct_connect.types.state_change_error
    import aws_sdk_direct_connect.types.virtual_interface_id
    import aws_sdk_direct_connect.types.virtual_interface_region


class DirectConnectGatewayAttachment(TypedDict):
    direct_connect_gateway_id: NotRequired[
        "aws_sdk_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId"
    ]
    """<p>The ID of the Direct Connect gateway.</p>"""
    virtual_interface_id: NotRequired[
        "aws_sdk_direct_connect.types.virtual_interface_id.VirtualInterfaceId"
    ]
    """<p>The ID of the virtual interface.</p>"""
    virtual_interface_region: NotRequired[
        "aws_sdk_direct_connect.types.virtual_interface_region.VirtualInterfaceRegion"
    ]
    """<p>The Amazon Web Services Region where the virtual interface is located.</p>"""
    virtual_interface_owner_account: NotRequired[
        "aws_sdk_direct_connect.types.owner_account.OwnerAccount"
    ]
    """<p>The ID of the Amazon Web Services account that owns the virtual interface.</p>"""
    attachment_state: NotRequired[
        "aws_sdk_direct_connect.types.direct_connect_gateway_attachment_state.DirectConnectGatewayAttachmentState"
    ]
    """<p>The state of the attachment. The following are the possible values:</p> <ul> <li> <p> <code>attaching</code>: The initial state after a virtual interface is created using the Direct Connect gateway.</p> </li> <li> <p> <code>attached</code>: The Direct Connect gateway and virtual interface are attached and ready to pass traffic.</p> </li> <li> <p> <code>detaching</code>: The initial state after calling <a>DeleteVirtualInterface</a>.</p> </li> <li> <p> <code>detached</code>: The virtual interface is detached from the Direct Connect gateway. Traffic flow between the Direct Connect gateway and virtual interface is stopped.</p> </li> </ul>"""
    attachment_type: NotRequired[
        "aws_sdk_direct_connect.types.direct_connect_gateway_attachment_type.DirectConnectGatewayAttachmentType"
    ]
    """<p>The type of attachment.</p>"""
    state_change_error: NotRequired[
        "aws_sdk_direct_connect.types.state_change_error.StateChangeError"
    ]
    """<p>The error message if the state of an object failed to advance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectConnectGatewayAttachment) -> dict:
    out: dict = {}
    if "direct_connect_gateway_id" in value:
        out["directConnectGatewayId"] = value["direct_connect_gateway_id"]
    if "virtual_interface_id" in value:
        out["virtualInterfaceId"] = value["virtual_interface_id"]
    if "virtual_interface_region" in value:
        out["virtualInterfaceRegion"] = value["virtual_interface_region"]
    if "virtual_interface_owner_account" in value:
        out["virtualInterfaceOwnerAccount"] = value["virtual_interface_owner_account"]
    if "attachment_state" in value:
        import aws_sdk_direct_connect.types.direct_connect_gateway_attachment_state

        out["attachmentState"] = (
            aws_sdk_direct_connect.types.direct_connect_gateway_attachment_state.serialize_aws_json_1_1(
                value["attachment_state"]
            )
        )
    if "attachment_type" in value:
        import aws_sdk_direct_connect.types.direct_connect_gateway_attachment_type

        out["attachmentType"] = (
            aws_sdk_direct_connect.types.direct_connect_gateway_attachment_type.serialize_aws_json_1_1(
                value["attachment_type"]
            )
        )
    if "state_change_error" in value:
        out["stateChangeError"] = value["state_change_error"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DirectConnectGatewayAttachment:
    out: DirectConnectGatewayAttachment = {}  # type: ignore[typeddict-item]
    if "directConnectGatewayId" in data:
        out["direct_connect_gateway_id"] = data["directConnectGatewayId"]
    if "virtualInterfaceId" in data:
        out["virtual_interface_id"] = data["virtualInterfaceId"]
    if "virtualInterfaceRegion" in data:
        out["virtual_interface_region"] = data["virtualInterfaceRegion"]
    if "virtualInterfaceOwnerAccount" in data:
        out["virtual_interface_owner_account"] = data["virtualInterfaceOwnerAccount"]
    if "attachmentState" in data:
        import aws_sdk_direct_connect.types.direct_connect_gateway_attachment_state

        out["attachment_state"] = (
            aws_sdk_direct_connect.types.direct_connect_gateway_attachment_state.deserialize_aws_json_1_1(
                data["attachmentState"]
            )
        )
    if "attachmentType" in data:
        import aws_sdk_direct_connect.types.direct_connect_gateway_attachment_type

        out["attachment_type"] = (
            aws_sdk_direct_connect.types.direct_connect_gateway_attachment_type.deserialize_aws_json_1_1(
                data["attachmentType"]
            )
        )
    if "stateChangeError" in data:
        out["state_change_error"] = data["stateChangeError"]
    return out
