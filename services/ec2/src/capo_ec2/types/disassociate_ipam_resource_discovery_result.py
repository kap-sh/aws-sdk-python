"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateIpamResourceDiscoveryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_resource_discovery_association


class DisassociateIpamResourceDiscoveryResult(TypedDict, closed=True):
    ipam_resource_discovery_association: NotRequired[
        "capo_ec2.types.ipam_resource_discovery_association.IpamResourceDiscoveryAssociation"
    ]
    """<p>A resource discovery association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisassociateIpamResourceDiscoveryResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipam_resource_discovery_association" in value:
        import capo_ec2.types.ipam_resource_discovery_association

        capo_ec2.types.ipam_resource_discovery_association.serialize_ec2_query(
            value["ipam_resource_discovery_association"],
            pairs,
            f"{key_prefix}IpamResourceDiscoveryAssociation",
        )


def deserialize_ec2_query(el: Element) -> DisassociateIpamResourceDiscoveryResult:
    out: DisassociateIpamResourceDiscoveryResult = {}  # type: ignore[typeddict-item]
    child_ipam_resource_discovery_association = el.find(
        "ipamResourceDiscoveryAssociation"
    )
    if child_ipam_resource_discovery_association is not None:
        import capo_ec2.types.ipam_resource_discovery_association

        out["ipam_resource_discovery_association"] = (
            capo_ec2.types.ipam_resource_discovery_association.deserialize_ec2_query(
                child_ipam_resource_discovery_association
            )
        )
    return out
