"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeNetworkInsightsAnalysesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.filter_list
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.network_insights_analysis_id_list
    import capo_ec2.types.network_insights_max_results
    import capo_ec2.types.network_insights_path_id
    import capo_ec2.types.next_token


class DescribeNetworkInsightsAnalysesRequest(TypedDict, closed=True):
    network_insights_analysis_ids: NotRequired[
        "capo_ec2.types.network_insights_analysis_id_list.NetworkInsightsAnalysisIdList"
    ]
    """<p>The ID of the network insights analyses. You must specify either analysis IDs or a path ID.</p>"""
    network_insights_path_id: NotRequired[
        "capo_ec2.types.network_insights_path_id.NetworkInsightsPathId"
    ]
    """<p>The ID of the path. You must specify either a path ID or analysis IDs.</p>"""
    analysis_start_time: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time when the network insights analyses started.</p>"""
    analysis_end_time: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time when the network insights analyses ended.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>The filters. The following are the possible values:</p> <ul> <li> <p>path-found - A Boolean value that indicates whether a feasible path is found.</p> </li> <li> <p>status - The status of the analysis (running | succeeded | failed).</p> </li> </ul>"""
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
    value: DescribeNetworkInsightsAnalysesRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "network_insights_analysis_ids" in value:
        import capo_ec2.types.network_insights_analysis_id_list

        capo_ec2.types.network_insights_analysis_id_list.serialize_ec2_query(
            value["network_insights_analysis_ids"],
            pairs,
            f"{prefix}.NetworkInsightsAnalysisIds",
        )
    if "network_insights_path_id" in value:
        pairs.append(
            (f"{prefix}.NetworkInsightsPathId", str(value["network_insights_path_id"]))
        )
    if "analysis_start_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["analysis_start_time"], pairs, f"{prefix}.AnalysisStartTime"
        )
    if "analysis_end_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["analysis_end_time"], pairs, f"{prefix}.AnalysisEndTime"
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


def deserialize_ec2_query(el: Element) -> DescribeNetworkInsightsAnalysesRequest:
    out: DescribeNetworkInsightsAnalysesRequest = {}  # type: ignore[typeddict-item]
    if el.find("NetworkInsightsAnalysisIds") is not None:
        import capo_ec2.types.network_insights_analysis_id_list

        out["network_insights_analysis_ids"] = (
            capo_ec2.types.network_insights_analysis_id_list.deserialize_ec2_query(
                el, "NetworkInsightsAnalysisIds"
            )
        )
    child_network_insights_path_id = el.find("NetworkInsightsPathId")
    if child_network_insights_path_id is not None:
        out["network_insights_path_id"] = str(child_network_insights_path_id.text or "")
    child_analysis_start_time = el.find("AnalysisStartTime")
    if child_analysis_start_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["analysis_start_time"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_analysis_start_time
            )
        )
    child_analysis_end_time = el.find("AnalysisEndTime")
    if child_analysis_end_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["analysis_end_time"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_analysis_end_time
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
