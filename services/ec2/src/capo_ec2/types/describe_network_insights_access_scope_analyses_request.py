"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeNetworkInsightsAccessScopeAnalysesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.filter_list
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.network_insights_access_scope_analysis_id_list
    import capo_ec2.types.network_insights_access_scope_id
    import capo_ec2.types.network_insights_max_results
    import capo_ec2.types.next_token


class DescribeNetworkInsightsAccessScopeAnalysesRequest(TypedDict, closed=True):
    network_insights_access_scope_analysis_ids: NotRequired[
        "capo_ec2.types.network_insights_access_scope_analysis_id_list.NetworkInsightsAccessScopeAnalysisIdList"
    ]
    """<p>The IDs of the Network Access Scope analyses.</p>"""
    network_insights_access_scope_id: NotRequired[
        "capo_ec2.types.network_insights_access_scope_id.NetworkInsightsAccessScopeId"
    ]
    """<p>The ID of the Network Access Scope.</p>"""
    analysis_start_time_begin: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>Filters the results based on the start time. The analysis must have started on or after this time.</p>"""
    analysis_start_time_end: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>Filters the results based on the start time. The analysis must have started on or before this time.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>There are no supported filters.</p>"""
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
    value: DescribeNetworkInsightsAccessScopeAnalysesRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "network_insights_access_scope_analysis_ids" in value:
        import capo_ec2.types.network_insights_access_scope_analysis_id_list

        capo_ec2.types.network_insights_access_scope_analysis_id_list.serialize_ec2_query(
            value["network_insights_access_scope_analysis_ids"],
            pairs,
            f"{key_prefix}NetworkInsightsAccessScopeAnalysisId",
        )
    if "network_insights_access_scope_id" in value:
        pairs.append(
            (
                f"{key_prefix}NetworkInsightsAccessScopeId",
                str(value["network_insights_access_scope_id"]),
            )
        )
    if "analysis_start_time_begin" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["analysis_start_time_begin"],
            pairs,
            f"{key_prefix}AnalysisStartTimeBegin",
        )
    if "analysis_start_time_end" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["analysis_start_time_end"], pairs, f"{key_prefix}AnalysisStartTimeEnd"
        )
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(
    el: Element,
) -> DescribeNetworkInsightsAccessScopeAnalysesRequest:
    out: DescribeNetworkInsightsAccessScopeAnalysesRequest = {}  # type: ignore[typeddict-item]
    child_network_insights_access_scope_analysis_ids = el.find(
        "NetworkInsightsAccessScopeAnalysisId"
    )
    if child_network_insights_access_scope_analysis_ids is not None:
        import capo_ec2.types.network_insights_access_scope_analysis_id_list

        out["network_insights_access_scope_analysis_ids"] = (
            capo_ec2.types.network_insights_access_scope_analysis_id_list.deserialize_ec2_query(
                child_network_insights_access_scope_analysis_ids
            )
        )
    child_network_insights_access_scope_id = el.find("NetworkInsightsAccessScopeId")
    if child_network_insights_access_scope_id is not None:
        out["network_insights_access_scope_id"] = str(
            child_network_insights_access_scope_id.text or ""
        )
    child_analysis_start_time_begin = el.find("AnalysisStartTimeBegin")
    if child_analysis_start_time_begin is not None:
        import capo_ec2.types.millisecond_date_time

        out["analysis_start_time_begin"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_analysis_start_time_begin
            )
        )
    child_analysis_start_time_end = el.find("AnalysisStartTimeEnd")
    if child_analysis_start_time_end is not None:
        import capo_ec2.types.millisecond_date_time

        out["analysis_start_time_end"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_analysis_start_time_end
            )
        )
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
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
