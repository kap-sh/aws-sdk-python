"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeClientVpnEndpointsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.endpoint_set
    import aws_sdk_ec2.types.next_token


class DescribeClientVpnEndpointsResult(TypedDict):
    client_vpn_endpoints: NotRequired["aws_sdk_ec2.types.endpoint_set.EndpointSet"]
    """<p>Information about the Client VPN endpoints.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeClientVpnEndpointsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "client_vpn_endpoints" in value:
        import aws_sdk_ec2.types.endpoint_set

        aws_sdk_ec2.types.endpoint_set.serialize_ec2_query(
            value["client_vpn_endpoints"], pairs, f"{prefix}.ClientVpnEndpoint"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeClientVpnEndpointsResult:
    out: DescribeClientVpnEndpointsResult = {}  # type: ignore[typeddict-item]
    if el.find("ClientVpnEndpoint") is not None:
        import aws_sdk_ec2.types.endpoint_set

        out["client_vpn_endpoints"] = (
            aws_sdk_ec2.types.endpoint_set.deserialize_ec2_query(
                el, "ClientVpnEndpoint"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
