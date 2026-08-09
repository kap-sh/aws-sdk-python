"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCoipPoolsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.coip_pool_set
    import capo_ec2.types.string


class DescribeCoipPoolsResult(TypedDict, closed=True):
    coip_pools: NotRequired["capo_ec2.types.coip_pool_set.CoipPoolSet"]
    """<p>Information about the address pools.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeCoipPoolsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "coip_pools" in value:
        import capo_ec2.types.coip_pool_set

        capo_ec2.types.coip_pool_set.serialize_ec2_query(
            value["coip_pools"], pairs, f"{key_prefix}CoipPoolSet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeCoipPoolsResult:
    out: DescribeCoipPoolsResult = {}  # type: ignore[typeddict-item]
    child_coip_pools = el.find("coipPoolSet")
    if child_coip_pools is not None:
        import capo_ec2.types.coip_pool_set

        out["coip_pools"] = capo_ec2.types.coip_pool_set.deserialize_ec2_query(
            child_coip_pools
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
