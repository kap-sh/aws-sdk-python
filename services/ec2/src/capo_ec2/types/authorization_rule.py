"""Generated from Smithy shape ``com.amazonaws.ec2#AuthorizationRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.client_vpn_authorization_rule_status
    import capo_ec2.types.string


class AuthorizationRule(TypedDict, closed=True):
    client_vpn_endpoint_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Client VPN endpoint with which the authorization rule is associated.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A brief description of the authorization rule.</p>"""
    group_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Active Directory group to which the authorization rule grants access.</p>"""
    access_all: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the authorization rule grants access to all clients.</p>"""
    destination_cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv4 address range, in CIDR notation, of the network to which the authorization rule applies.</p>"""
    status: NotRequired[
        "capo_ec2.types.client_vpn_authorization_rule_status.ClientVpnAuthorizationRuleStatus"
    ]
    """<p>The current state of the authorization rule.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AuthorizationRule, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "client_vpn_endpoint_id" in value:
        pairs.append(
            (f"{key_prefix}ClientVpnEndpointId", str(value["client_vpn_endpoint_id"]))
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "group_id" in value:
        pairs.append((f"{key_prefix}GroupId", str(value["group_id"])))
    if "access_all" in value:
        pairs.append(
            (f"{key_prefix}AccessAll", "true" if value["access_all"] else "false")
        )
    if "destination_cidr" in value:
        pairs.append((f"{key_prefix}DestinationCidr", str(value["destination_cidr"])))
    if "status" in value:
        import capo_ec2.types.client_vpn_authorization_rule_status

        capo_ec2.types.client_vpn_authorization_rule_status.serialize_ec2_query(
            value["status"], pairs, f"{key_prefix}Status"
        )


def deserialize_ec2_query(el: Element) -> AuthorizationRule:
    out: AuthorizationRule = {}  # type: ignore[typeddict-item]
    child_client_vpn_endpoint_id = el.find("ClientVpnEndpointId")
    if child_client_vpn_endpoint_id is not None:
        out["client_vpn_endpoint_id"] = str(child_client_vpn_endpoint_id.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_group_id = el.find("GroupId")
    if child_group_id is not None:
        out["group_id"] = str(child_group_id.text or "")
    child_access_all = el.find("AccessAll")
    if child_access_all is not None:
        out["access_all"] = (child_access_all.text or "").lower() == "true"
    child_destination_cidr = el.find("DestinationCidr")
    if child_destination_cidr is not None:
        out["destination_cidr"] = str(child_destination_cidr.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_ec2.types.client_vpn_authorization_rule_status

        out["status"] = (
            capo_ec2.types.client_vpn_authorization_rule_status.deserialize_ec2_query(
                child_status
            )
        )
    return out
