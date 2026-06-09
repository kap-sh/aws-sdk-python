"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstancesIpv6Address``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipv6_address


class ScheduledInstancesIpv6Address(TypedDict):
    ipv6_address: NotRequired["aws_sdk_ec2.types.ipv6_address.Ipv6Address"]
    """<p>The IPv6 address.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ScheduledInstancesIpv6Address, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ipv6_address" in value:
        pairs.append((f"{prefix}.Ipv6Address", str(value["ipv6_address"])))


def deserialize_ec2_query(el: Element) -> ScheduledInstancesIpv6Address:
    out: ScheduledInstancesIpv6Address = {}  # type: ignore[typeddict-item]
    child_ipv6_address = el.find("Ipv6Address")
    if child_ipv6_address is not None:
        out["ipv6_address"] = str(child_ipv6_address.text or "")
    return out
