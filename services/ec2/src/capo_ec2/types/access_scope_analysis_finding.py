"""Generated from Smithy shape ``com.amazonaws.ec2#AccessScopeAnalysisFinding``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.network_insights_access_scope_analysis_id
    import capo_ec2.types.network_insights_access_scope_id
    import capo_ec2.types.path_component_list
    import capo_ec2.types.string


class AccessScopeAnalysisFinding(TypedDict, closed=True):
    network_insights_access_scope_analysis_id: NotRequired[
        "capo_ec2.types.network_insights_access_scope_analysis_id.NetworkInsightsAccessScopeAnalysisId"
    ]
    """<p>The ID of the Network Access Scope analysis.</p>"""
    network_insights_access_scope_id: NotRequired[
        "capo_ec2.types.network_insights_access_scope_id.NetworkInsightsAccessScopeId"
    ]
    """<p>The ID of the Network Access Scope.</p>"""
    finding_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the finding.</p>"""
    finding_components: NotRequired[
        "capo_ec2.types.path_component_list.PathComponentList"
    ]
    """<p>The finding components.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AccessScopeAnalysisFinding, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "network_insights_access_scope_analysis_id" in value:
        pairs.append(
            (
                f"{key_prefix}NetworkInsightsAccessScopeAnalysisId",
                str(value["network_insights_access_scope_analysis_id"]),
            )
        )
    if "network_insights_access_scope_id" in value:
        pairs.append(
            (
                f"{key_prefix}NetworkInsightsAccessScopeId",
                str(value["network_insights_access_scope_id"]),
            )
        )
    if "finding_id" in value:
        pairs.append((f"{key_prefix}FindingId", str(value["finding_id"])))
    if "finding_components" in value:
        import capo_ec2.types.path_component_list

        capo_ec2.types.path_component_list.serialize_ec2_query(
            value["finding_components"], pairs, f"{key_prefix}FindingComponentSet"
        )


def deserialize_ec2_query(el: Element) -> AccessScopeAnalysisFinding:
    out: AccessScopeAnalysisFinding = {}  # type: ignore[typeddict-item]
    child_network_insights_access_scope_analysis_id = el.find(
        "networkInsightsAccessScopeAnalysisId"
    )
    if child_network_insights_access_scope_analysis_id is not None:
        out["network_insights_access_scope_analysis_id"] = str(
            child_network_insights_access_scope_analysis_id.text or ""
        )
    child_network_insights_access_scope_id = el.find("networkInsightsAccessScopeId")
    if child_network_insights_access_scope_id is not None:
        out["network_insights_access_scope_id"] = str(
            child_network_insights_access_scope_id.text or ""
        )
    child_finding_id = el.find("findingId")
    if child_finding_id is not None:
        out["finding_id"] = str(child_finding_id.text or "")
    child_finding_components = el.find("findingComponentSet")
    if child_finding_components is not None:
        import capo_ec2.types.path_component_list

        out["finding_components"] = (
            capo_ec2.types.path_component_list.deserialize_ec2_query(
                child_finding_components
            )
        )
    return out
