"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpnConcentratorsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.next_token
    import capo_ec2.types.vpn_concentrator_list


class DescribeVpnConcentratorsResult(TypedDict, closed=True):
    vpn_concentrators: NotRequired[
        "capo_ec2.types.vpn_concentrator_list.VpnConcentratorList"
    ]
    """<p>Information about the VPN concentrators.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpnConcentratorsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "vpn_concentrators" in value:
        import capo_ec2.types.vpn_concentrator_list

        capo_ec2.types.vpn_concentrator_list.serialize_ec2_query(
            value["vpn_concentrators"], pairs, f"{prefix}.VpnConcentratorSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeVpnConcentratorsResult:
    out: DescribeVpnConcentratorsResult = {}  # type: ignore[typeddict-item]
    if el.find("VpnConcentratorSet") is not None:
        import capo_ec2.types.vpn_concentrator_list

        out["vpn_concentrators"] = (
            capo_ec2.types.vpn_concentrator_list.deserialize_ec2_query(
                el, "VpnConcentratorSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
