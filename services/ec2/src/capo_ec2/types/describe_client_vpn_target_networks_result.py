"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeClientVpnTargetNetworksResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.next_token
    import capo_ec2.types.target_network_set


class DescribeClientVpnTargetNetworksResult(TypedDict, closed=True):
    client_vpn_target_networks: NotRequired[
        "capo_ec2.types.target_network_set.TargetNetworkSet"
    ]
    """<p>Information about the associated target networks.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeClientVpnTargetNetworksResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "client_vpn_target_networks" in value:
        import capo_ec2.types.target_network_set

        capo_ec2.types.target_network_set.serialize_ec2_query(
            value["client_vpn_target_networks"],
            pairs,
            f"{key_prefix}ClientVpnTargetNetworks",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeClientVpnTargetNetworksResult:
    out: DescribeClientVpnTargetNetworksResult = {}  # type: ignore[typeddict-item]
    if el.find("ClientVpnTargetNetworks") is not None:
        import capo_ec2.types.target_network_set

        out["client_vpn_target_networks"] = (
            capo_ec2.types.target_network_set.deserialize_ec2_query(
                el, "ClientVpnTargetNetworks"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
