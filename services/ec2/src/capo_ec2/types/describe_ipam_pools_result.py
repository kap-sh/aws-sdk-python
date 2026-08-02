"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIpamPoolsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_pool_set
    import capo_ec2.types.next_token


class DescribeIpamPoolsResult(TypedDict, closed=True):
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    ipam_pools: NotRequired["capo_ec2.types.ipam_pool_set.IpamPoolSet"]
    """<p>Information about the IPAM pools.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeIpamPoolsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "ipam_pools" in value:
        import capo_ec2.types.ipam_pool_set

        capo_ec2.types.ipam_pool_set.serialize_ec2_query(
            value["ipam_pools"], pairs, f"{key_prefix}IpamPoolSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeIpamPoolsResult:
    out: DescribeIpamPoolsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("IpamPoolSet") is not None:
        import capo_ec2.types.ipam_pool_set

        out["ipam_pools"] = capo_ec2.types.ipam_pool_set.deserialize_ec2_query(
            el, "IpamPoolSet"
        )
    return out
