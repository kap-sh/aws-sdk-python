"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeClientVpnRoutesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_route_set
    import aws_sdk_ec2.types.next_token


class DescribeClientVpnRoutesResult(TypedDict, closed=True):
    routes: NotRequired["aws_sdk_ec2.types.client_vpn_route_set.ClientVpnRouteSet"]
    """<p>Information about the Client VPN endpoint routes.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeClientVpnRoutesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "routes" in value:
        import aws_sdk_ec2.types.client_vpn_route_set

        aws_sdk_ec2.types.client_vpn_route_set.serialize_ec2_query(
            value["routes"], pairs, f"{prefix}.Routes"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeClientVpnRoutesResult:
    out: DescribeClientVpnRoutesResult = {}  # type: ignore[typeddict-item]
    if el.find("Routes") is not None:
        import aws_sdk_ec2.types.client_vpn_route_set

        out["routes"] = aws_sdk_ec2.types.client_vpn_route_set.deserialize_ec2_query(
            el, "Routes"
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
