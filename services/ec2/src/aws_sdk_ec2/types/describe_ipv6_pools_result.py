"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIpv6PoolsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipv6_pool_set
    import aws_sdk_ec2.types.next_token


class DescribeIpv6PoolsResult(TypedDict):
    ipv6_pools: NotRequired["aws_sdk_ec2.types.ipv6_pool_set.Ipv6PoolSet"]
    """<p>Information about the IPv6 address pools.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeIpv6PoolsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ipv6_pools" in value:
        import aws_sdk_ec2.types.ipv6_pool_set

        aws_sdk_ec2.types.ipv6_pool_set.serialize_ec2_query(
            value["ipv6_pools"], pairs, f"{prefix}.Ipv6PoolSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeIpv6PoolsResult:
    out: DescribeIpv6PoolsResult = {}  # type: ignore[typeddict-item]
    if el.find("Ipv6PoolSet") is not None:
        import aws_sdk_ec2.types.ipv6_pool_set

        out["ipv6_pools"] = aws_sdk_ec2.types.ipv6_pool_set.deserialize_ec2_query(
            el, "Ipv6PoolSet"
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
