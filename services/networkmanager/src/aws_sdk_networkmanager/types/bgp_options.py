"""Generated from Smithy shape ``com.amazonaws.networkmanager#BgpOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.long


class BgpOptions(TypedDict):
    peer_asn: NotRequired["aws_sdk_networkmanager.types.long.Long"]
    """<p>The Peer ASN of the BGP.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BgpOptions) -> dict:
    out: dict = {}
    if "peer_asn" in value:
        out["PeerAsn"] = value["peer_asn"]
    return out


def deserialize_json(data: dict) -> BgpOptions:
    out: BgpOptions = {}  # type: ignore[typeddict-item]
    if "PeerAsn" in data:
        out["peer_asn"] = data["PeerAsn"]
    return out
