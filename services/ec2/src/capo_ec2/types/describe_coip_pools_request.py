"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCoipPoolsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.coip_pool_id_set
    import capo_ec2.types.coip_pool_max_results
    import capo_ec2.types.filter_list
    import capo_ec2.types.string


class DescribeCoipPoolsRequest(TypedDict, closed=True):
    pool_ids: NotRequired["capo_ec2.types.coip_pool_id_set.CoipPoolIdSet"]
    """<p>The IDs of the address pools.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>coip-pool.local-gateway-route-table-id</code> - The ID of the local gateway route table.</p> </li> <li> <p> <code>coip-pool.pool-id</code> - The ID of the address pool.</p> </li> </ul>"""
    max_results: NotRequired["capo_ec2.types.coip_pool_max_results.CoipPoolMaxResults"]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token for the next page of results.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeCoipPoolsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "pool_ids" in value:
        import capo_ec2.types.coip_pool_id_set

        capo_ec2.types.coip_pool_id_set.serialize_ec2_query(
            value["pool_ids"], pairs, f"{key_prefix}PoolId"
        )
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DescribeCoipPoolsRequest:
    out: DescribeCoipPoolsRequest = {}  # type: ignore[typeddict-item]
    child_pool_ids = el.find("PoolId")
    if child_pool_ids is not None:
        import capo_ec2.types.coip_pool_id_set

        out["pool_ids"] = capo_ec2.types.coip_pool_id_set.deserialize_ec2_query(
            child_pool_ids
        )
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
