"""Generated from Smithy shape ``com.amazonaws.ec2#IpamDiscoveredRoute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_byoip_advertisement_type
    import capo_ec2.types.ipam_byoip_cidr_state
    import capo_ec2.types.ipam_resource_discovery_id
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string


class IpamDiscoveredRoute(TypedDict, closed=True):
    ipam_resource_discovery_id: NotRequired[
        "capo_ec2.types.ipam_resource_discovery_id.IpamResourceDiscoveryId"
    ]
    """<p>The ID of the IPAM resource discovery that discovered the route.</p>"""
    resource_region: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Web Services Region where the route was discovered.</p>"""
    resource_owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the resource owner.</p>"""
    cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The IP address prefix of the discovered route in CIDR notation.</p>"""
    asn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Autonomous System Number (ASN) that originates the route.</p>"""
    state: NotRequired["capo_ec2.types.ipam_byoip_cidr_state.IpamByoipCidrState"]
    """<p>The state of the BYOIP CIDR. Possible values:</p> <ul> <li> <p> <code>advertised</code> - The CIDR is being advertised.</p> </li> <li> <p> <code>deprovisioned</code> - The CIDR has been deprovisioned.</p> </li> <li> <p> <code>failed-deprovision</code> - Deprovisioning failed.</p> </li> <li> <p> <code>failed-provision</code> - Provisioning failed.</p> </li> <li> <p> <code>pending-deprovision</code> - Deprovisioning is in progress.</p> </li> <li> <p> <code>pending-provision</code> - Provisioning is in progress.</p> </li> <li> <p> <code>provisioned</code> - The CIDR is provisioned.</p> </li> <li> <p> <code>provisioned-not-publicly-advertisable</code> - The CIDR is provisioned but not publicly advertisable.</p> </li> </ul>"""
    advertisement_type: NotRequired[
        "capo_ec2.types.ipam_byoip_advertisement_type.IpamByoipAdvertisementType"
    ]
    """<p>The advertisement type of the route. Possible values:</p> <ul> <li> <p> <code>regional</code> - The IP address is advertised from a single location (regional services such as Amazon EC2).</p> </li> <li> <p> <code>global</code> - The IP address is advertised from multiple global locations simultaneously (global services such as Amazon CloudFront).</p> </li> </ul>"""
    network_border_group: NotRequired["capo_ec2.types.string.String"]
    """<p>The network border group for the route.</p>"""
    pool_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the BYOIP pool associated with the route.</p>"""
    ipam_pool_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the IPAM pool associated with the route.</p>"""
    sample_time: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The time when the route was last sampled.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamDiscoveredRoute, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipam_resource_discovery_id" in value:
        pairs.append(
            (
                f"{key_prefix}IpamResourceDiscoveryId",
                str(value["ipam_resource_discovery_id"]),
            )
        )
    if "resource_region" in value:
        pairs.append((f"{key_prefix}ResourceRegion", str(value["resource_region"])))
    if "resource_owner_id" in value:
        pairs.append((f"{key_prefix}ResourceOwnerId", str(value["resource_owner_id"])))
    if "cidr" in value:
        pairs.append((f"{key_prefix}Cidr", str(value["cidr"])))
    if "asn" in value:
        pairs.append((f"{key_prefix}Asn", str(value["asn"])))
    if "state" in value:
        import capo_ec2.types.ipam_byoip_cidr_state

        capo_ec2.types.ipam_byoip_cidr_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "advertisement_type" in value:
        import capo_ec2.types.ipam_byoip_advertisement_type

        capo_ec2.types.ipam_byoip_advertisement_type.serialize_ec2_query(
            value["advertisement_type"], pairs, f"{key_prefix}AdvertisementType"
        )
    if "network_border_group" in value:
        pairs.append(
            (f"{key_prefix}NetworkBorderGroup", str(value["network_border_group"]))
        )
    if "pool_id" in value:
        pairs.append((f"{key_prefix}PoolId", str(value["pool_id"])))
    if "ipam_pool_id" in value:
        pairs.append((f"{key_prefix}IpamPoolId", str(value["ipam_pool_id"])))
    if "sample_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["sample_time"], pairs, f"{key_prefix}SampleTime"
        )


def deserialize_ec2_query(el: Element) -> IpamDiscoveredRoute:
    out: IpamDiscoveredRoute = {}  # type: ignore[typeddict-item]
    child_ipam_resource_discovery_id = el.find("ipamResourceDiscoveryId")
    if child_ipam_resource_discovery_id is not None:
        out["ipam_resource_discovery_id"] = str(
            child_ipam_resource_discovery_id.text or ""
        )
    child_resource_region = el.find("resourceRegion")
    if child_resource_region is not None:
        out["resource_region"] = str(child_resource_region.text or "")
    child_resource_owner_id = el.find("resourceOwnerId")
    if child_resource_owner_id is not None:
        out["resource_owner_id"] = str(child_resource_owner_id.text or "")
    child_cidr = el.find("cidr")
    if child_cidr is not None:
        out["cidr"] = str(child_cidr.text or "")
    child_asn = el.find("asn")
    if child_asn is not None:
        out["asn"] = str(child_asn.text or "")
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.ipam_byoip_cidr_state

        out["state"] = capo_ec2.types.ipam_byoip_cidr_state.deserialize_ec2_query(
            child_state
        )
    child_advertisement_type = el.find("advertisementType")
    if child_advertisement_type is not None:
        import capo_ec2.types.ipam_byoip_advertisement_type

        out["advertisement_type"] = (
            capo_ec2.types.ipam_byoip_advertisement_type.deserialize_ec2_query(
                child_advertisement_type
            )
        )
    child_network_border_group = el.find("networkBorderGroup")
    if child_network_border_group is not None:
        out["network_border_group"] = str(child_network_border_group.text or "")
    child_pool_id = el.find("poolId")
    if child_pool_id is not None:
        out["pool_id"] = str(child_pool_id.text or "")
    child_ipam_pool_id = el.find("ipamPoolId")
    if child_ipam_pool_id is not None:
        out["ipam_pool_id"] = str(child_ipam_pool_id.text or "")
    child_sample_time = el.find("sampleTime")
    if child_sample_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["sample_time"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_sample_time
        )
    return out
