"""Generated from Smithy shape ``com.amazonaws.directconnect#BGPPeerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.bgp_peer

BGPPeerList: TypeAlias = list["aws_sdk_direct_connect.types.bgp_peer.BGPPeer"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BGPPeerList) -> list:
    import aws_sdk_direct_connect.types.bgp_peer

    out: list = []
    for item in value:
        out.append(aws_sdk_direct_connect.types.bgp_peer.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> BGPPeerList:
    import aws_sdk_direct_connect.types.bgp_peer

    out: BGPPeerList = []
    for item in data:
        out.append(aws_sdk_direct_connect.types.bgp_peer.deserialize_aws_json_1_1(item))
    return out
