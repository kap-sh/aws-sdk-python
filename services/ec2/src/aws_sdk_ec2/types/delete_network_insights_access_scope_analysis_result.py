"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteNetworkInsightsAccessScopeAnalysisResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_insights_access_scope_analysis_id


class DeleteNetworkInsightsAccessScopeAnalysisResult(TypedDict, closed=True):
    network_insights_access_scope_analysis_id: NotRequired[
        "aws_sdk_ec2.types.network_insights_access_scope_analysis_id.NetworkInsightsAccessScopeAnalysisId"
    ]
    """<p>The ID of the Network Access Scope analysis.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteNetworkInsightsAccessScopeAnalysisResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "network_insights_access_scope_analysis_id" in value:
        pairs.append(
            (
                f"{prefix}.NetworkInsightsAccessScopeAnalysisId",
                str(value["network_insights_access_scope_analysis_id"]),
            )
        )


def deserialize_ec2_query(
    el: Element,
) -> DeleteNetworkInsightsAccessScopeAnalysisResult:
    out: DeleteNetworkInsightsAccessScopeAnalysisResult = {}  # type: ignore[typeddict-item]
    child_network_insights_access_scope_analysis_id = el.find(
        "NetworkInsightsAccessScopeAnalysisId"
    )
    if child_network_insights_access_scope_analysis_id is not None:
        out["network_insights_access_scope_analysis_id"] = str(
            child_network_insights_access_scope_analysis_id.text or ""
        )
    return out
