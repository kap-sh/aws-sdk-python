"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIpamPoolAllocationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_pool_allocation_set
    import capo_ec2.types.next_token


class DescribeIpamPoolAllocationsResult(TypedDict, closed=True):
    ipam_pool_allocations: NotRequired[
        "capo_ec2.types.ipam_pool_allocation_set.IpamPoolAllocationSet"
    ]
    """<p>Information about the IPAM pool allocations.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeIpamPoolAllocationsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipam_pool_allocations" in value:
        import capo_ec2.types.ipam_pool_allocation_set

        capo_ec2.types.ipam_pool_allocation_set.serialize_ec2_query(
            value["ipam_pool_allocations"], pairs, f"{key_prefix}IpamPoolAllocationSet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeIpamPoolAllocationsResult:
    out: DescribeIpamPoolAllocationsResult = {}  # type: ignore[typeddict-item]
    child_ipam_pool_allocations = el.find("ipamPoolAllocationSet")
    if child_ipam_pool_allocations is not None:
        import capo_ec2.types.ipam_pool_allocation_set

        out["ipam_pool_allocations"] = (
            capo_ec2.types.ipam_pool_allocation_set.deserialize_ec2_query(
                child_ipam_pool_allocations
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
