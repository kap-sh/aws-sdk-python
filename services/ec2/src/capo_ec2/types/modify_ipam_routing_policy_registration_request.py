"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamRoutingPolicyRegistrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.asn_list
    import capo_ec2.types.boolean
    import capo_ec2.types.boxed_boolean
    import capo_ec2.types.ipam_internet_registry_association_id
    import capo_ec2.types.ipam_routing_policy_registration_max_length
    import capo_ec2.types.string


class ModifyIpamRoutingPolicyRegistrationRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_internet_registry_association_id: NotRequired[
        "capo_ec2.types.ipam_internet_registry_association_id.IpamInternetRegistryAssociationId"
    ]
    """<p>The ID of the IPAM internet registry association.</p>"""
    cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The IP address prefix in CIDR notation identifying the routing policy registration to modify.</p>"""
    asns: NotRequired["capo_ec2.types.asn_list.AsnList"]
    """<p>The updated list of Autonomous System Numbers (ASNs) authorized to originate the prefix.</p>"""
    permit_more_specific_announcements: NotRequired[
        "capo_ec2.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>Specifies whether to permit more specific route announcements than the CIDR prefix. Default: <code>false</code>.</p>"""
    max_length: NotRequired[
        "capo_ec2.types.ipam_routing_policy_registration_max_length.IpamRoutingPolicyRegistrationMaxLength"
    ]
    """<p>The new maximum prefix length that the ASNs are authorized to announce. Must be greater than or equal to the prefix length of the CIDR.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A new description for the routing policy registration.</p>"""
    force: NotRequired["capo_ec2.types.boxed_boolean.BoxedBoolean"]
    """<p>Forces the modification even if it conflicts with an announced route. Default: <code>false</code>.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the operation ignores the request, but does not return an error.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyIpamRoutingPolicyRegistrationRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_internet_registry_association_id" in value:
        pairs.append(
            (
                f"{key_prefix}IpamInternetRegistryAssociationId",
                str(value["ipam_internet_registry_association_id"]),
            )
        )
    if "cidr" in value:
        pairs.append((f"{key_prefix}Cidr", str(value["cidr"])))
    if "asns" in value:
        import capo_ec2.types.asn_list

        capo_ec2.types.asn_list.serialize_ec2_query(
            value["asns"], pairs, f"{key_prefix}Asn"
        )
    if "permit_more_specific_announcements" in value:
        pairs.append(
            (
                f"{key_prefix}PermitMoreSpecificAnnouncements",
                "true" if value["permit_more_specific_announcements"] else "false",
            )
        )
    if "max_length" in value:
        pairs.append((f"{key_prefix}MaxLength", str(value["max_length"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "force" in value:
        pairs.append((f"{key_prefix}Force", "true" if value["force"] else "false"))
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))


def deserialize_ec2_query(el: Element) -> ModifyIpamRoutingPolicyRegistrationRequest:
    out: ModifyIpamRoutingPolicyRegistrationRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_internet_registry_association_id = el.find(
        "IpamInternetRegistryAssociationId"
    )
    if child_ipam_internet_registry_association_id is not None:
        out["ipam_internet_registry_association_id"] = str(
            child_ipam_internet_registry_association_id.text or ""
        )
    child_cidr = el.find("Cidr")
    if child_cidr is not None:
        out["cidr"] = str(child_cidr.text or "")
    child_asns = el.find("Asn")
    if child_asns is not None:
        import capo_ec2.types.asn_list

        out["asns"] = capo_ec2.types.asn_list.deserialize_ec2_query(child_asns)
    child_permit_more_specific_announcements = el.find(
        "PermitMoreSpecificAnnouncements"
    )
    if child_permit_more_specific_announcements is not None:
        out["permit_more_specific_announcements"] = (
            child_permit_more_specific_announcements.text or ""
        ).lower() == "true"
    child_max_length = el.find("MaxLength")
    if child_max_length is not None:
        out["max_length"] = int(child_max_length.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_force = el.find("Force")
    if child_force is not None:
        out["force"] = (child_force.text or "").lower() == "true"
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out
