"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcPeeringConnectionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.vpc_peering_connection_list


class DescribeVpcPeeringConnectionsResult(TypedDict, closed=True):
    vpc_peering_connections: NotRequired[
        "capo_ec2.types.vpc_peering_connection_list.VpcPeeringConnectionList"
    ]
    """<p>Information about the VPC peering connections.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpcPeeringConnectionsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "vpc_peering_connections" in value:
        import capo_ec2.types.vpc_peering_connection_list

        capo_ec2.types.vpc_peering_connection_list.serialize_ec2_query(
            value["vpc_peering_connections"],
            pairs,
            f"{key_prefix}VpcPeeringConnectionSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeVpcPeeringConnectionsResult:
    out: DescribeVpcPeeringConnectionsResult = {}  # type: ignore[typeddict-item]
    if el.find("vpcPeeringConnectionSet") is not None:
        import capo_ec2.types.vpc_peering_connection_list

        out["vpc_peering_connections"] = (
            capo_ec2.types.vpc_peering_connection_list.deserialize_ec2_query(
                el, "vpcPeeringConnectionSet"
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
