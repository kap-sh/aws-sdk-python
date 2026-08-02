"""Generated from Smithy shape ``com.amazonaws.ec2#CreateIpamResourceDiscoveryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_resource_discovery


class CreateIpamResourceDiscoveryResult(TypedDict, closed=True):
    ipam_resource_discovery: NotRequired[
        "capo_ec2.types.ipam_resource_discovery.IpamResourceDiscovery"
    ]
    """<p>An IPAM resource discovery.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateIpamResourceDiscoveryResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipam_resource_discovery" in value:
        import capo_ec2.types.ipam_resource_discovery

        capo_ec2.types.ipam_resource_discovery.serialize_ec2_query(
            value["ipam_resource_discovery"],
            pairs,
            f"{key_prefix}IpamResourceDiscovery",
        )


def deserialize_ec2_query(el: Element) -> CreateIpamResourceDiscoveryResult:
    out: CreateIpamResourceDiscoveryResult = {}  # type: ignore[typeddict-item]
    child_ipam_resource_discovery = el.find("IpamResourceDiscovery")
    if child_ipam_resource_discovery is not None:
        import capo_ec2.types.ipam_resource_discovery

        out["ipam_resource_discovery"] = (
            capo_ec2.types.ipam_resource_discovery.deserialize_ec2_query(
                child_ipam_resource_discovery
            )
        )
    return out
