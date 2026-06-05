"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateIpamResourceDiscoveryResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_resource_discovery_association


class DisassociateIpamResourceDiscoveryResult(TypedDict):
    ipam_resource_discovery_association: NotRequired[
        "aws_sdk_ec2.types.ipam_resource_discovery_association.IpamResourceDiscoveryAssociation"
    ]
    """<p>A resource discovery association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisassociateIpamResourceDiscoveryResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "ipam_resource_discovery_association" in value:
        import aws_sdk_ec2.types.ipam_resource_discovery_association

        aws_sdk_ec2.types.ipam_resource_discovery_association.serialize_ec2_query(
            value["ipam_resource_discovery_association"],
            pairs,
            f"{prefix}.IpamResourceDiscoveryAssociation",
        )


def deserialize_ec2_query(el: Element) -> DisassociateIpamResourceDiscoveryResult:
    out: DisassociateIpamResourceDiscoveryResult = {}  # type: ignore[typeddict-item]
    child_ipam_resource_discovery_association = el.find(
        "IpamResourceDiscoveryAssociation"
    )
    if child_ipam_resource_discovery_association is not None:
        import aws_sdk_ec2.types.ipam_resource_discovery_association

        out["ipam_resource_discovery_association"] = (
            aws_sdk_ec2.types.ipam_resource_discovery_association.deserialize_ec2_query(
                child_ipam_resource_discovery_association
            )
        )
    return out
