"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeNetworkInsightsPathsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.filter_list
    import capo_ec2.types.network_insights_max_results
    import capo_ec2.types.network_insights_path_id_list
    import capo_ec2.types.next_token


class DescribeNetworkInsightsPathsRequest(TypedDict, closed=True):
    network_insights_path_ids: NotRequired[
        "capo_ec2.types.network_insights_path_id_list.NetworkInsightsPathIdList"
    ]
    """<p>The IDs of the paths.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>The filters. The following are the possible values:</p> <ul> <li> <p>destination - The ID of the resource.</p> </li> <li> <p>filter-at-source.source-address - The source IPv4 address at the source.</p> </li> <li> <p>filter-at-source.source-port-range - The source port range at the source.</p> </li> <li> <p>filter-at-source.destination-address - The destination IPv4 address at the source.</p> </li> <li> <p>filter-at-source.destination-port-range - The destination port range at the source.</p> </li> <li> <p>filter-at-destination.source-address - The source IPv4 address at the destination.</p> </li> <li> <p>filter-at-destination.source-port-range - The source port range at the destination.</p> </li> <li> <p>filter-at-destination.destination-address - The destination IPv4 address at the destination.</p> </li> <li> <p>filter-at-destination.destination-port-range - The destination port range at the destination.</p> </li> <li> <p>protocol - The protocol.</p> </li> <li> <p>source - The ID of the resource.</p> </li> </ul>"""
    max_results: NotRequired[
        "capo_ec2.types.network_insights_max_results.NetworkInsightsMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeNetworkInsightsPathsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "network_insights_path_ids" in value:
        import capo_ec2.types.network_insights_path_id_list

        capo_ec2.types.network_insights_path_id_list.serialize_ec2_query(
            value["network_insights_path_ids"],
            pairs,
            f"{prefix}.NetworkInsightsPathIds",
        )
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeNetworkInsightsPathsRequest:
    out: DescribeNetworkInsightsPathsRequest = {}  # type: ignore[typeddict-item]
    if el.find("NetworkInsightsPathIds") is not None:
        import capo_ec2.types.network_insights_path_id_list

        out["network_insights_path_ids"] = (
            capo_ec2.types.network_insights_path_id_list.deserialize_ec2_query(
                el, "NetworkInsightsPathIds"
            )
        )
    if el.find("Filters") is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(el, "Filters")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
