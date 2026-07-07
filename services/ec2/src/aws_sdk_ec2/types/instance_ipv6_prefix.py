"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceIpv6Prefix``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class InstanceIpv6Prefix(TypedDict, closed=True):
    ipv6_prefix: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>One or more IPv6 prefixes assigned to the network interface.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceIpv6Prefix, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ipv6_prefix" in value:
        pairs.append((f"{prefix}.Ipv6Prefix", str(value["ipv6_prefix"])))


def deserialize_ec2_query(el: Element) -> InstanceIpv6Prefix:
    out: InstanceIpv6Prefix = {}  # type: ignore[typeddict-item]
    child_ipv6_prefix = el.find("Ipv6Prefix")
    if child_ipv6_prefix is not None:
        out["ipv6_prefix"] = str(child_ipv6_prefix.text or "")
    return out
