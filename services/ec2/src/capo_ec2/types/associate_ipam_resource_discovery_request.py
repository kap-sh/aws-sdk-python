"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateIpamResourceDiscoveryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.ipam_id
    import capo_ec2.types.ipam_resource_discovery_id
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class AssociateIpamResourceDiscoveryRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_id: NotRequired["capo_ec2.types.ipam_id.IpamId"]
    """<p>An IPAM ID.</p>"""
    ipam_resource_discovery_id: NotRequired[
        "capo_ec2.types.ipam_resource_discovery_id.IpamResourceDiscoveryId"
    ]
    """<p>A resource discovery ID.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>Tag specifications.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>A client token.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociateIpamResourceDiscoveryRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_id" in value:
        pairs.append((f"{key_prefix}IpamId", str(value["ipam_id"])))
    if "ipam_resource_discovery_id" in value:
        pairs.append(
            (
                f"{key_prefix}IpamResourceDiscoveryId",
                str(value["ipam_resource_discovery_id"]),
            )
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecifications"
        )
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))


def deserialize_ec2_query(el: Element) -> AssociateIpamResourceDiscoveryRequest:
    out: AssociateIpamResourceDiscoveryRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_id = el.find("IpamId")
    if child_ipam_id is not None:
        out["ipam_id"] = str(child_ipam_id.text or "")
    child_ipam_resource_discovery_id = el.find("IpamResourceDiscoveryId")
    if child_ipam_resource_discovery_id is not None:
        out["ipam_resource_discovery_id"] = str(
            child_ipam_resource_discovery_id.text or ""
        )
    if el.find("TagSpecifications") is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecifications"
            )
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out
