"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTransitGatewayConnectPeersResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_connect_peer_list


class DescribeTransitGatewayConnectPeersResult(TypedDict):
    transit_gateway_connect_peers: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_connect_peer_list.TransitGatewayConnectPeerList"
    ]
    """<p>Information about the Connect peers.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeTransitGatewayConnectPeersResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_connect_peers" in value:
        import aws_sdk_ec2.types.transit_gateway_connect_peer_list

        aws_sdk_ec2.types.transit_gateway_connect_peer_list.serialize_ec2_query(
            value["transit_gateway_connect_peers"],
            pairs,
            f"{prefix}.TransitGatewayConnectPeerSet",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeTransitGatewayConnectPeersResult:
    out: DescribeTransitGatewayConnectPeersResult = {}  # type: ignore[typeddict-item]
    if el.find("TransitGatewayConnectPeerSet") is not None:
        import aws_sdk_ec2.types.transit_gateway_connect_peer_list

        out["transit_gateway_connect_peers"] = (
            aws_sdk_ec2.types.transit_gateway_connect_peer_list.deserialize_ec2_query(
                el, "TransitGatewayConnectPeerSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
