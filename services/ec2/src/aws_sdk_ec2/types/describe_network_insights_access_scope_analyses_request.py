"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeNetworkInsightsAccessScopeAnalysesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.network_insights_access_scope_analysis_id_list
    import aws_sdk_ec2.types.network_insights_access_scope_id
    import aws_sdk_ec2.types.network_insights_max_results
    import aws_sdk_ec2.types.next_token


class DescribeNetworkInsightsAccessScopeAnalysesRequest(TypedDict):
    network_insights_access_scope_analysis_ids: NotRequired[
        "aws_sdk_ec2.types.network_insights_access_scope_analysis_id_list.NetworkInsightsAccessScopeAnalysisIdList"
    ]
    """<p>The IDs of the Network Access Scope analyses.</p>"""
    network_insights_access_scope_id: NotRequired[
        "aws_sdk_ec2.types.network_insights_access_scope_id.NetworkInsightsAccessScopeId"
    ]
    """<p>The ID of the Network Access Scope.</p>"""
    analysis_start_time_begin: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>Filters the results based on the start time. The analysis must have started on or after this time.</p>"""
    analysis_start_time_end: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>Filters the results based on the start time. The analysis must have started on or before this time.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>There are no supported filters.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.network_insights_max_results.NetworkInsightsMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeNetworkInsightsAccessScopeAnalysesRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "network_insights_access_scope_analysis_ids" in value:
        import aws_sdk_ec2.types.network_insights_access_scope_analysis_id_list

        aws_sdk_ec2.types.network_insights_access_scope_analysis_id_list.serialize_ec2_query(
            value["network_insights_access_scope_analysis_ids"],
            pairs,
            f"{prefix}.NetworkInsightsAccessScopeAnalysisIds",
        )
    if "network_insights_access_scope_id" in value:
        pairs.append(
            (
                f"{prefix}.NetworkInsightsAccessScopeId",
                str(value["network_insights_access_scope_id"]),
            )
        )
    if "analysis_start_time_begin" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["analysis_start_time_begin"],
            pairs,
            f"{prefix}.AnalysisStartTimeBegin",
        )
    if "analysis_start_time_end" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["analysis_start_time_end"], pairs, f"{prefix}.AnalysisStartTimeEnd"
        )
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(
    el: Element,
) -> DescribeNetworkInsightsAccessScopeAnalysesRequest:
    out: DescribeNetworkInsightsAccessScopeAnalysesRequest = {}  # type: ignore[typeddict-item]
    if el.find("NetworkInsightsAccessScopeAnalysisIds") is not None:
        import aws_sdk_ec2.types.network_insights_access_scope_analysis_id_list

        out["network_insights_access_scope_analysis_ids"] = (
            aws_sdk_ec2.types.network_insights_access_scope_analysis_id_list.deserialize_ec2_query(
                el, "NetworkInsightsAccessScopeAnalysisIds"
            )
        )
    child_network_insights_access_scope_id = el.find("NetworkInsightsAccessScopeId")
    if child_network_insights_access_scope_id is not None:
        out["network_insights_access_scope_id"] = str(
            child_network_insights_access_scope_id.text or ""
        )
    child_analysis_start_time_begin = el.find("AnalysisStartTimeBegin")
    if child_analysis_start_time_begin is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["analysis_start_time_begin"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_analysis_start_time_begin
            )
        )
    child_analysis_start_time_end = el.find("AnalysisStartTimeEnd")
    if child_analysis_start_time_end is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["analysis_start_time_end"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_analysis_start_time_end
            )
        )
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
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
