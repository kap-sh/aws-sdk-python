"""Generated from Smithy shape ``com.amazonaws.ec2#ApplySecurityGroupsToClientVpnTargetNetworkRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.client_vpn_endpoint_id
    import aws_sdk_ec2.types.client_vpn_security_group_id_set
    import aws_sdk_ec2.types.vpc_id


class ApplySecurityGroupsToClientVpnTargetNetworkRequest(TypedDict):
    client_vpn_endpoint_id: NotRequired[
        "aws_sdk_ec2.types.client_vpn_endpoint_id.ClientVpnEndpointId"
    ]
    """<p>The ID of the Client VPN endpoint.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC in which the associated target network is located.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_ec2.types.client_vpn_security_group_id_set.ClientVpnSecurityGroupIdSet"
    ]
    """<p>The IDs of the security groups to apply to the associated target network. Up to 5 security groups can be applied to an associated target network.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ApplySecurityGroupsToClientVpnTargetNetworkRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "client_vpn_endpoint_id" in value:
        pairs.append(
            (f"{prefix}.ClientVpnEndpointId", str(value["client_vpn_endpoint_id"]))
        )
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))
    if "security_group_ids" in value:
        import aws_sdk_ec2.types.client_vpn_security_group_id_set

        aws_sdk_ec2.types.client_vpn_security_group_id_set.serialize_ec2_query(
            value["security_group_ids"], pairs, f"{prefix}.SecurityGroupIds"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> ApplySecurityGroupsToClientVpnTargetNetworkRequest:
    out: ApplySecurityGroupsToClientVpnTargetNetworkRequest = {}  # type: ignore[typeddict-item]
    child_client_vpn_endpoint_id = el.find("ClientVpnEndpointId")
    if child_client_vpn_endpoint_id is not None:
        out["client_vpn_endpoint_id"] = str(child_client_vpn_endpoint_id.text or "")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    if el.find("SecurityGroupIds") is not None:
        import aws_sdk_ec2.types.client_vpn_security_group_id_set

        out["security_group_ids"] = (
            aws_sdk_ec2.types.client_vpn_security_group_id_set.deserialize_ec2_query(
                el, "SecurityGroupIds"
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
