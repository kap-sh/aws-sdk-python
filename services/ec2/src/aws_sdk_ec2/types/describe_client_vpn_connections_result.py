"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeClientVpnConnectionsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_connection_set
    import aws_sdk_ec2.types.next_token


class DescribeClientVpnConnectionsResult(TypedDict):
    connections: NotRequired[
        "aws_sdk_ec2.types.client_vpn_connection_set.ClientVpnConnectionSet"
    ]
    """<p>Information about the active and terminated client connections.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeClientVpnConnectionsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "connections" in value:
        import aws_sdk_ec2.types.client_vpn_connection_set

        aws_sdk_ec2.types.client_vpn_connection_set.serialize_ec2_query(
            value["connections"], pairs, f"{prefix}.Connections"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeClientVpnConnectionsResult:
    out: DescribeClientVpnConnectionsResult = {}  # type: ignore[typeddict-item]
    if el.find("Connections") is not None:
        import aws_sdk_ec2.types.client_vpn_connection_set

        out["connections"] = (
            aws_sdk_ec2.types.client_vpn_connection_set.deserialize_ec2_query(
                el, "Connections"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
