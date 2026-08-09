"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIpv6PoolsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipv6_pool_set
    import capo_ec2.types.next_token


class DescribeIpv6PoolsResult(TypedDict, closed=True):
    ipv6_pools: NotRequired["capo_ec2.types.ipv6_pool_set.Ipv6PoolSet"]
    """<p>Information about the IPv6 address pools.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeIpv6PoolsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipv6_pools" in value:
        import capo_ec2.types.ipv6_pool_set

        capo_ec2.types.ipv6_pool_set.serialize_ec2_query(
            value["ipv6_pools"], pairs, f"{key_prefix}Ipv6PoolSet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeIpv6PoolsResult:
    out: DescribeIpv6PoolsResult = {}  # type: ignore[typeddict-item]
    child_ipv6_pools = el.find("ipv6PoolSet")
    if child_ipv6_pools is not None:
        import capo_ec2.types.ipv6_pool_set

        out["ipv6_pools"] = capo_ec2.types.ipv6_pool_set.deserialize_ec2_query(
            child_ipv6_pools
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
