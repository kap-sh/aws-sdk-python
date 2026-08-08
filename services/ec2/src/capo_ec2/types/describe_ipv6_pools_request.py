"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIpv6PoolsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.filter_list
    import capo_ec2.types.ipv6_pool_id_list
    import capo_ec2.types.ipv6_pool_max_results
    import capo_ec2.types.next_token


class DescribeIpv6PoolsRequest(TypedDict, closed=True):
    pool_ids: NotRequired["capo_ec2.types.ipv6_pool_id_list.Ipv6PoolIdList"]
    """<p>The IDs of the IPv6 address pools.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
    max_results: NotRequired["capo_ec2.types.ipv6_pool_max_results.Ipv6PoolMaxResults"]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>tag</code>:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeIpv6PoolsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "pool_ids" in value:
        import capo_ec2.types.ipv6_pool_id_list

        capo_ec2.types.ipv6_pool_id_list.serialize_ec2_query(
            value["pool_ids"], pairs, f"{key_prefix}PoolId"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )


def deserialize_ec2_query(el: Element) -> DescribeIpv6PoolsRequest:
    out: DescribeIpv6PoolsRequest = {}  # type: ignore[typeddict-item]
    if el.find("PoolId") is not None:
        import capo_ec2.types.ipv6_pool_id_list

        out["pool_ids"] = capo_ec2.types.ipv6_pool_id_list.deserialize_ec2_query(
            el, "PoolId"
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("Filter") is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(el, "Filter")
    return out
