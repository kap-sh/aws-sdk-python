"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcEndpointConnectionsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_endpoint_connection_set


class DescribeVpcEndpointConnectionsResult(TypedDict):
    vpc_endpoint_connections: NotRequired[
        "aws_sdk_ec2.types.vpc_endpoint_connection_set.VpcEndpointConnectionSet"
    ]
    """<p>Information about the VPC endpoint connections.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpcEndpointConnectionsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "vpc_endpoint_connections" in value:
        import aws_sdk_ec2.types.vpc_endpoint_connection_set

        aws_sdk_ec2.types.vpc_endpoint_connection_set.serialize_ec2_query(
            value["vpc_endpoint_connections"],
            pairs,
            f"{prefix}.VpcEndpointConnectionSet",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeVpcEndpointConnectionsResult:
    out: DescribeVpcEndpointConnectionsResult = {}  # type: ignore[typeddict-item]
    if el.find("VpcEndpointConnectionSet") is not None:
        import aws_sdk_ec2.types.vpc_endpoint_connection_set

        out["vpc_endpoint_connections"] = (
            aws_sdk_ec2.types.vpc_endpoint_connection_set.deserialize_ec2_query(
                el, "VpcEndpointConnectionSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
