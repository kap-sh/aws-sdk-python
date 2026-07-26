"""Generated from Smithy shape ``com.amazonaws.batch#NetworkInterface``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.string


class NetworkInterface(TypedDict, closed=True):
    attachment_id: NotRequired["capo_batch.types.string.String"]
    """<p>The attachment ID for the network interface.</p>"""
    ipv6_address: NotRequired["capo_batch.types.string.String"]
    """<p>The private IPv6 address for the network interface.</p>"""
    private_ipv4_address: NotRequired["capo_batch.types.string.String"]
    """<p>The private IPv4 address for the network interface.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkInterface) -> dict:
    out: dict = {}
    if "attachment_id" in value:
        out["attachmentId"] = value["attachment_id"]
    if "ipv6_address" in value:
        out["ipv6Address"] = value["ipv6_address"]
    if "private_ipv4_address" in value:
        out["privateIpv4Address"] = value["private_ipv4_address"]
    return out


def deserialize_json(data: dict) -> NetworkInterface:
    out: NetworkInterface = {}  # type: ignore[typeddict-item]
    if "attachmentId" in data:
        out["attachment_id"] = data["attachmentId"]
    if "ipv6Address" in data:
        out["ipv6_address"] = data["ipv6Address"]
    if "privateIpv4Address" in data:
        out["private_ipv4_address"] = data["privateIpv4Address"]
    return out
