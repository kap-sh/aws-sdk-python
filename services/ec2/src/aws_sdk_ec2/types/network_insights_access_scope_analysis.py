"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInsightsAccessScopeAnalysis``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.analysis_status
    import aws_sdk_ec2.types.findings_found
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.network_insights_access_scope_analysis_id
    import aws_sdk_ec2.types.network_insights_access_scope_id
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class NetworkInsightsAccessScopeAnalysis(TypedDict, closed=True):
    network_insights_access_scope_analysis_id: NotRequired[
        "aws_sdk_ec2.types.network_insights_access_scope_analysis_id.NetworkInsightsAccessScopeAnalysisId"
    ]
    """<p>The ID of the Network Access Scope analysis.</p>"""
    network_insights_access_scope_analysis_arn: NotRequired[
        "aws_sdk_ec2.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Network Access Scope analysis.</p>"""
    network_insights_access_scope_id: NotRequired[
        "aws_sdk_ec2.types.network_insights_access_scope_id.NetworkInsightsAccessScopeId"
    ]
    """<p>The ID of the Network Access Scope.</p>"""
    status: NotRequired["aws_sdk_ec2.types.analysis_status.AnalysisStatus"]
    """<p>The status.</p>"""
    status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status message.</p>"""
    warning_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The warning message.</p>"""
    start_date: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The analysis start date.</p>"""
    end_date: NotRequired["aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The analysis end date.</p>"""
    findings_found: NotRequired["aws_sdk_ec2.types.findings_found.FindingsFound"]
    """<p>Indicates whether there are findings.</p>"""
    analyzed_eni_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of network interfaces analyzed.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NetworkInsightsAccessScopeAnalysis, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "network_insights_access_scope_analysis_id" in value:
        pairs.append(
            (
                f"{prefix}.NetworkInsightsAccessScopeAnalysisId",
                str(value["network_insights_access_scope_analysis_id"]),
            )
        )
    if "network_insights_access_scope_analysis_arn" in value:
        pairs.append(
            (
                f"{prefix}.NetworkInsightsAccessScopeAnalysisArn",
                str(value["network_insights_access_scope_analysis_arn"]),
            )
        )
    if "network_insights_access_scope_id" in value:
        pairs.append(
            (
                f"{prefix}.NetworkInsightsAccessScopeId",
                str(value["network_insights_access_scope_id"]),
            )
        )
    if "status" in value:
        import aws_sdk_ec2.types.analysis_status

        aws_sdk_ec2.types.analysis_status.serialize_ec2_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "status_message" in value:
        pairs.append((f"{prefix}.StatusMessage", str(value["status_message"])))
    if "warning_message" in value:
        pairs.append((f"{prefix}.WarningMessage", str(value["warning_message"])))
    if "start_date" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["start_date"], pairs, f"{prefix}.StartDate"
        )
    if "end_date" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["end_date"], pairs, f"{prefix}.EndDate"
        )
    if "findings_found" in value:
        import aws_sdk_ec2.types.findings_found

        aws_sdk_ec2.types.findings_found.serialize_ec2_query(
            value["findings_found"], pairs, f"{prefix}.FindingsFound"
        )
    if "analyzed_eni_count" in value:
        pairs.append((f"{prefix}.AnalyzedEniCount", str(value["analyzed_eni_count"])))
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> NetworkInsightsAccessScopeAnalysis:
    out: NetworkInsightsAccessScopeAnalysis = {}  # type: ignore[typeddict-item]
    child_network_insights_access_scope_analysis_id = el.find(
        "NetworkInsightsAccessScopeAnalysisId"
    )
    if child_network_insights_access_scope_analysis_id is not None:
        out["network_insights_access_scope_analysis_id"] = str(
            child_network_insights_access_scope_analysis_id.text or ""
        )
    child_network_insights_access_scope_analysis_arn = el.find(
        "NetworkInsightsAccessScopeAnalysisArn"
    )
    if child_network_insights_access_scope_analysis_arn is not None:
        out["network_insights_access_scope_analysis_arn"] = str(
            child_network_insights_access_scope_analysis_arn.text or ""
        )
    child_network_insights_access_scope_id = el.find("NetworkInsightsAccessScopeId")
    if child_network_insights_access_scope_id is not None:
        out["network_insights_access_scope_id"] = str(
            child_network_insights_access_scope_id.text or ""
        )
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_ec2.types.analysis_status

        out["status"] = aws_sdk_ec2.types.analysis_status.deserialize_ec2_query(
            child_status
        )
    child_status_message = el.find("StatusMessage")
    if child_status_message is not None:
        out["status_message"] = str(child_status_message.text or "")
    child_warning_message = el.find("WarningMessage")
    if child_warning_message is not None:
        out["warning_message"] = str(child_warning_message.text or "")
    child_start_date = el.find("StartDate")
    if child_start_date is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["start_date"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_start_date
            )
        )
    child_end_date = el.find("EndDate")
    if child_end_date is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["end_date"] = aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_end_date
        )
    child_findings_found = el.find("FindingsFound")
    if child_findings_found is not None:
        import aws_sdk_ec2.types.findings_found

        out["findings_found"] = aws_sdk_ec2.types.findings_found.deserialize_ec2_query(
            child_findings_found
        )
    child_analyzed_eni_count = el.find("AnalyzedEniCount")
    if child_analyzed_eni_count is not None:
        out["analyzed_eni_count"] = int(child_analyzed_eni_count.text or "")
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
