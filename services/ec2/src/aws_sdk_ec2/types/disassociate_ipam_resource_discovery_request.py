"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateIpamResourceDiscoveryRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_resource_discovery_association_id


class DisassociateIpamResourceDiscoveryRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_resource_discovery_association_id: NotRequired[
        "aws_sdk_ec2.types.ipam_resource_discovery_association_id.IpamResourceDiscoveryAssociationId"
    ]
    """<p>A resource discovery association ID.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisassociateIpamResourceDiscoveryRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_resource_discovery_association_id" in value:
        pairs.append(
            (
                f"{prefix}.IpamResourceDiscoveryAssociationId",
                str(value["ipam_resource_discovery_association_id"]),
            )
        )


def deserialize_ec2_query(el: Element) -> DisassociateIpamResourceDiscoveryRequest:
    out: DisassociateIpamResourceDiscoveryRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_resource_discovery_association_id = el.find(
        "IpamResourceDiscoveryAssociationId"
    )
    if child_ipam_resource_discovery_association_id is not None:
        out["ipam_resource_discovery_association_id"] = str(
            child_ipam_resource_discovery_association_id.text or ""
        )
    return out
