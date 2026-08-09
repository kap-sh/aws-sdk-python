"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInsightsAccessScopeAnalysis``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.analysis_status
    import capo_ec2.types.findings_found
    import capo_ec2.types.integer
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.network_insights_access_scope_analysis_id
    import capo_ec2.types.network_insights_access_scope_id
    import capo_ec2.types.resource_arn
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class NetworkInsightsAccessScopeAnalysis(TypedDict, closed=True):
    network_insights_access_scope_analysis_id: NotRequired[
        "capo_ec2.types.network_insights_access_scope_analysis_id.NetworkInsightsAccessScopeAnalysisId"
    ]
    """<p>The ID of the Network Access Scope analysis.</p>"""
    network_insights_access_scope_analysis_arn: NotRequired[
        "capo_ec2.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Network Access Scope analysis.</p>"""
    network_insights_access_scope_id: NotRequired[
        "capo_ec2.types.network_insights_access_scope_id.NetworkInsightsAccessScopeId"
    ]
    """<p>The ID of the Network Access Scope.</p>"""
    status: NotRequired["capo_ec2.types.analysis_status.AnalysisStatus"]
    """<p>The status.</p>"""
    status_message: NotRequired["capo_ec2.types.string.String"]
    """<p>The status message.</p>"""
    warning_message: NotRequired["capo_ec2.types.string.String"]
    """<p>The warning message.</p>"""
    start_date: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The analysis start date.</p>"""
    end_date: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The analysis end date.</p>"""
    findings_found: NotRequired["capo_ec2.types.findings_found.FindingsFound"]
    """<p>Indicates whether there are findings.</p>"""
    analyzed_eni_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of network interfaces analyzed.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NetworkInsightsAccessScopeAnalysis, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "network_insights_access_scope_analysis_id" in value:
        pairs.append(
            (
                f"{key_prefix}NetworkInsightsAccessScopeAnalysisId",
                str(value["network_insights_access_scope_analysis_id"]),
            )
        )
    if "network_insights_access_scope_analysis_arn" in value:
        pairs.append(
            (
                f"{key_prefix}NetworkInsightsAccessScopeAnalysisArn",
                str(value["network_insights_access_scope_analysis_arn"]),
            )
        )
    if "network_insights_access_scope_id" in value:
        pairs.append(
            (
                f"{key_prefix}NetworkInsightsAccessScopeId",
                str(value["network_insights_access_scope_id"]),
            )
        )
    if "status" in value:
        import capo_ec2.types.analysis_status

        capo_ec2.types.analysis_status.serialize_ec2_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "status_message" in value:
        pairs.append((f"{key_prefix}StatusMessage", str(value["status_message"])))
    if "warning_message" in value:
        pairs.append((f"{key_prefix}WarningMessage", str(value["warning_message"])))
    if "start_date" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["start_date"], pairs, f"{key_prefix}StartDate"
        )
    if "end_date" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["end_date"], pairs, f"{key_prefix}EndDate"
        )
    if "findings_found" in value:
        import capo_ec2.types.findings_found

        capo_ec2.types.findings_found.serialize_ec2_query(
            value["findings_found"], pairs, f"{key_prefix}FindingsFound"
        )
    if "analyzed_eni_count" in value:
        pairs.append(
            (f"{key_prefix}AnalyzedEniCount", str(value["analyzed_eni_count"]))
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(el: Element) -> NetworkInsightsAccessScopeAnalysis:
    out: NetworkInsightsAccessScopeAnalysis = {}  # type: ignore[typeddict-item]
    child_network_insights_access_scope_analysis_id = el.find(
        "networkInsightsAccessScopeAnalysisId"
    )
    if child_network_insights_access_scope_analysis_id is not None:
        out["network_insights_access_scope_analysis_id"] = str(
            child_network_insights_access_scope_analysis_id.text or ""
        )
    child_network_insights_access_scope_analysis_arn = el.find(
        "networkInsightsAccessScopeAnalysisArn"
    )
    if child_network_insights_access_scope_analysis_arn is not None:
        out["network_insights_access_scope_analysis_arn"] = str(
            child_network_insights_access_scope_analysis_arn.text or ""
        )
    child_network_insights_access_scope_id = el.find("networkInsightsAccessScopeId")
    if child_network_insights_access_scope_id is not None:
        out["network_insights_access_scope_id"] = str(
            child_network_insights_access_scope_id.text or ""
        )
    child_status = el.find("status")
    if child_status is not None:
        import capo_ec2.types.analysis_status

        out["status"] = capo_ec2.types.analysis_status.deserialize_ec2_query(
            child_status
        )
    child_status_message = el.find("statusMessage")
    if child_status_message is not None:
        out["status_message"] = str(child_status_message.text or "")
    child_warning_message = el.find("warningMessage")
    if child_warning_message is not None:
        out["warning_message"] = str(child_warning_message.text or "")
    child_start_date = el.find("startDate")
    if child_start_date is not None:
        import capo_ec2.types.millisecond_date_time

        out["start_date"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_start_date
        )
    child_end_date = el.find("endDate")
    if child_end_date is not None:
        import capo_ec2.types.millisecond_date_time

        out["end_date"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_end_date
        )
    child_findings_found = el.find("findingsFound")
    if child_findings_found is not None:
        import capo_ec2.types.findings_found

        out["findings_found"] = capo_ec2.types.findings_found.deserialize_ec2_query(
            child_findings_found
        )
    child_analyzed_eni_count = el.find("analyzedEniCount")
    if child_analyzed_eni_count is not None:
        out["analyzed_eni_count"] = int(child_analyzed_eni_count.text or "")
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    return out
