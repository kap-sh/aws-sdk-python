"""Generated from Smithy shape ``com.amazonaws.ec2#GetNetworkInsightsAccessScopeAnalysisFindingsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.access_scope_analysis_finding_list
    import capo_ec2.types.analysis_status
    import capo_ec2.types.network_insights_access_scope_analysis_id
    import capo_ec2.types.string


class GetNetworkInsightsAccessScopeAnalysisFindingsResult(TypedDict, closed=True):
    network_insights_access_scope_analysis_id: NotRequired[
        "capo_ec2.types.network_insights_access_scope_analysis_id.NetworkInsightsAccessScopeAnalysisId"
    ]
    """<p>The ID of the Network Access Scope analysis.</p>"""
    analysis_status: NotRequired["capo_ec2.types.analysis_status.AnalysisStatus"]
    """<p>The status of Network Access Scope Analysis.</p>"""
    analysis_findings: NotRequired[
        "capo_ec2.types.access_scope_analysis_finding_list.AccessScopeAnalysisFindingList"
    ]
    """<p>The findings associated with Network Access Scope Analysis.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetNetworkInsightsAccessScopeAnalysisFindingsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "network_insights_access_scope_analysis_id" in value:
        pairs.append(
            (
                f"{key_prefix}NetworkInsightsAccessScopeAnalysisId",
                str(value["network_insights_access_scope_analysis_id"]),
            )
        )
    if "analysis_status" in value:
        import capo_ec2.types.analysis_status

        capo_ec2.types.analysis_status.serialize_ec2_query(
            value["analysis_status"], pairs, f"{key_prefix}AnalysisStatus"
        )
    if "analysis_findings" in value:
        import capo_ec2.types.access_scope_analysis_finding_list

        capo_ec2.types.access_scope_analysis_finding_list.serialize_ec2_query(
            value["analysis_findings"], pairs, f"{key_prefix}AnalysisFindingSet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(
    el: Element,
) -> GetNetworkInsightsAccessScopeAnalysisFindingsResult:
    out: GetNetworkInsightsAccessScopeAnalysisFindingsResult = {}  # type: ignore[typeddict-item]
    child_network_insights_access_scope_analysis_id = el.find(
        "NetworkInsightsAccessScopeAnalysisId"
    )
    if child_network_insights_access_scope_analysis_id is not None:
        out["network_insights_access_scope_analysis_id"] = str(
            child_network_insights_access_scope_analysis_id.text or ""
        )
    child_analysis_status = el.find("AnalysisStatus")
    if child_analysis_status is not None:
        import capo_ec2.types.analysis_status

        out["analysis_status"] = capo_ec2.types.analysis_status.deserialize_ec2_query(
            child_analysis_status
        )
    if el.find("AnalysisFindingSet") is not None:
        import capo_ec2.types.access_scope_analysis_finding_list

        out["analysis_findings"] = (
            capo_ec2.types.access_scope_analysis_finding_list.deserialize_ec2_query(
                el, "AnalysisFindingSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
