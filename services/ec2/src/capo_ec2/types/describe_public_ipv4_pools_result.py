"""Generated from Smithy shape ``com.amazonaws.ec2#DescribePublicIpv4PoolsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.public_ipv4_pool_set
    import capo_ec2.types.string


class DescribePublicIpv4PoolsResult(TypedDict, closed=True):
    public_ipv4_pools: NotRequired[
        "capo_ec2.types.public_ipv4_pool_set.PublicIpv4PoolSet"
    ]
    """<p>Information about the address pools.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribePublicIpv4PoolsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "public_ipv4_pools" in value:
        import capo_ec2.types.public_ipv4_pool_set

        capo_ec2.types.public_ipv4_pool_set.serialize_ec2_query(
            value["public_ipv4_pools"], pairs, f"{key_prefix}PublicIpv4PoolSet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribePublicIpv4PoolsResult:
    out: DescribePublicIpv4PoolsResult = {}  # type: ignore[typeddict-item]
    child_public_ipv4_pools = el.find("publicIpv4PoolSet")
    if child_public_ipv4_pools is not None:
        import capo_ec2.types.public_ipv4_pool_set

        out["public_ipv4_pools"] = (
            capo_ec2.types.public_ipv4_pool_set.deserialize_ec2_query(
                child_public_ipv4_pools
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
