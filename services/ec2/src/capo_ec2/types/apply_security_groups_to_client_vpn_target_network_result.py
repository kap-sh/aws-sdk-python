"""Generated from Smithy shape ``com.amazonaws.ec2#ApplySecurityGroupsToClientVpnTargetNetworkResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.client_vpn_security_group_id_set


class ApplySecurityGroupsToClientVpnTargetNetworkResult(TypedDict, closed=True):
    security_group_ids: NotRequired[
        "capo_ec2.types.client_vpn_security_group_id_set.ClientVpnSecurityGroupIdSet"
    ]
    """<p>The IDs of the applied security groups.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ApplySecurityGroupsToClientVpnTargetNetworkResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "security_group_ids" in value:
        import capo_ec2.types.client_vpn_security_group_id_set

        capo_ec2.types.client_vpn_security_group_id_set.serialize_ec2_query(
            value["security_group_ids"], pairs, f"{prefix}.SecurityGroupIds"
        )


def deserialize_ec2_query(
    el: Element,
) -> ApplySecurityGroupsToClientVpnTargetNetworkResult:
    out: ApplySecurityGroupsToClientVpnTargetNetworkResult = {}  # type: ignore[typeddict-item]
    if el.find("SecurityGroupIds") is not None:
        import capo_ec2.types.client_vpn_security_group_id_set

        out["security_group_ids"] = (
            capo_ec2.types.client_vpn_security_group_id_set.deserialize_ec2_query(
                el, "SecurityGroupIds"
            )
        )
    return out
