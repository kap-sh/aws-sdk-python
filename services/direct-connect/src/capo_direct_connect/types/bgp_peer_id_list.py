"""Generated from Smithy shape ``com.amazonaws.directconnect#BGPPeerIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_direct_connect.types.bgp_peer_id

BGPPeerIdList: TypeAlias = list["capo_direct_connect.types.bgp_peer_id.BGPPeerId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BGPPeerIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> BGPPeerIdList:
    return list(data)
