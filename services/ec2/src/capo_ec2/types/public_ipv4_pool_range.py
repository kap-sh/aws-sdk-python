"""Generated from Smithy shape ``com.amazonaws.ec2#PublicIpv4PoolRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer
    import capo_ec2.types.string


class PublicIpv4PoolRange(TypedDict, closed=True):
    first_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The first IP address in the range.</p>"""
    last_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The last IP address in the range.</p>"""
    address_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of addresses in the range.</p>"""
    available_address_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of available addresses in the range.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PublicIpv4PoolRange, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "first_address" in value:
        pairs.append((f"{key_prefix}FirstAddress", str(value["first_address"])))
    if "last_address" in value:
        pairs.append((f"{key_prefix}LastAddress", str(value["last_address"])))
    if "address_count" in value:
        pairs.append((f"{key_prefix}AddressCount", str(value["address_count"])))
    if "available_address_count" in value:
        pairs.append(
            (
                f"{key_prefix}AvailableAddressCount",
                str(value["available_address_count"]),
            )
        )


def deserialize_ec2_query(el: Element) -> PublicIpv4PoolRange:
    out: PublicIpv4PoolRange = {}  # type: ignore[typeddict-item]
    child_first_address = el.find("firstAddress")
    if child_first_address is not None:
        out["first_address"] = str(child_first_address.text or "")
    child_last_address = el.find("lastAddress")
    if child_last_address is not None:
        out["last_address"] = str(child_last_address.text or "")
    child_address_count = el.find("addressCount")
    if child_address_count is not None:
        out["address_count"] = int(child_address_count.text or "")
    child_available_address_count = el.find("availableAddressCount")
    if child_available_address_count is not None:
        out["available_address_count"] = int(child_available_address_count.text or "")
    return out
