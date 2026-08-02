"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcEndpointConnectionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.vpc_endpoint_connection_set


class DescribeVpcEndpointConnectionsResult(TypedDict, closed=True):
    vpc_endpoint_connections: NotRequired[
        "capo_ec2.types.vpc_endpoint_connection_set.VpcEndpointConnectionSet"
    ]
    """<p>Information about the VPC endpoint connections.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpcEndpointConnectionsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "vpc_endpoint_connections" in value:
        import capo_ec2.types.vpc_endpoint_connection_set

        capo_ec2.types.vpc_endpoint_connection_set.serialize_ec2_query(
            value["vpc_endpoint_connections"],
            pairs,
            f"{key_prefix}VpcEndpointConnectionSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeVpcEndpointConnectionsResult:
    out: DescribeVpcEndpointConnectionsResult = {}  # type: ignore[typeddict-item]
    if el.find("VpcEndpointConnectionSet") is not None:
        import capo_ec2.types.vpc_endpoint_connection_set

        out["vpc_endpoint_connections"] = (
            capo_ec2.types.vpc_endpoint_connection_set.deserialize_ec2_query(
                el, "VpcEndpointConnectionSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
