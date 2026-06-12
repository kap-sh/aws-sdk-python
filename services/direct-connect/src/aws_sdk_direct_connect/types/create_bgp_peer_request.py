"""Generated from Smithy shape ``com.amazonaws.directconnect#CreateBGPPeerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.new_bgp_peer
    import aws_sdk_direct_connect.types.virtual_interface_id


class CreateBGPPeerRequest(TypedDict):
    virtual_interface_id: NotRequired[
        "aws_sdk_direct_connect.types.virtual_interface_id.VirtualInterfaceId"
    ]
    """<p>The ID of the virtual interface.</p>"""
    new_bgp_peer: NotRequired["aws_sdk_direct_connect.types.new_bgp_peer.NewBGPPeer"]
    """<p>Information about the BGP peer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateBGPPeerRequest) -> dict:
    out: dict = {}
    if "virtual_interface_id" in value:
        out["virtualInterfaceId"] = value["virtual_interface_id"]
    if "new_bgp_peer" in value:
        import aws_sdk_direct_connect.types.new_bgp_peer

        out["newBGPPeer"] = (
            aws_sdk_direct_connect.types.new_bgp_peer.serialize_aws_json_1_1(
                value["new_bgp_peer"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateBGPPeerRequest:
    out: CreateBGPPeerRequest = {}  # type: ignore[typeddict-item]
    if "virtualInterfaceId" in data:
        out["virtual_interface_id"] = data["virtualInterfaceId"]
    if "newBGPPeer" in data:
        import aws_sdk_direct_connect.types.new_bgp_peer

        out["new_bgp_peer"] = (
            aws_sdk_direct_connect.types.new_bgp_peer.deserialize_aws_json_1_1(
                data["newBGPPeer"]
            )
        )
    return out
