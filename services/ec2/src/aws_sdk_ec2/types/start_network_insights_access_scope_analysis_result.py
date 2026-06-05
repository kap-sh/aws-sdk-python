"""Generated from Smithy shape ``com.amazonaws.ec2#StartNetworkInsightsAccessScopeAnalysisResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_insights_access_scope_analysis


class StartNetworkInsightsAccessScopeAnalysisResult(TypedDict):
    network_insights_access_scope_analysis: NotRequired[
        "aws_sdk_ec2.types.network_insights_access_scope_analysis.NetworkInsightsAccessScopeAnalysis"
    ]
    """<p>The Network Access Scope analysis.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: StartNetworkInsightsAccessScopeAnalysisResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "network_insights_access_scope_analysis" in value:
        import aws_sdk_ec2.types.network_insights_access_scope_analysis

        aws_sdk_ec2.types.network_insights_access_scope_analysis.serialize_ec2_query(
            value["network_insights_access_scope_analysis"],
            pairs,
            f"{prefix}.NetworkInsightsAccessScopeAnalysis",
        )


def deserialize_ec2_query(el: Element) -> StartNetworkInsightsAccessScopeAnalysisResult:
    out: StartNetworkInsightsAccessScopeAnalysisResult = {}  # type: ignore[typeddict-item]
    child_network_insights_access_scope_analysis = el.find(
        "NetworkInsightsAccessScopeAnalysis"
    )
    if child_network_insights_access_scope_analysis is not None:
        import aws_sdk_ec2.types.network_insights_access_scope_analysis

        out["network_insights_access_scope_analysis"] = (
            aws_sdk_ec2.types.network_insights_access_scope_analysis.deserialize_ec2_query(
                child_network_insights_access_scope_analysis
            )
        )
    return out
