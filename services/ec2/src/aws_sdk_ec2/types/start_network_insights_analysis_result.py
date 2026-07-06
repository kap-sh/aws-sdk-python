"""Generated from Smithy shape ``com.amazonaws.ec2#StartNetworkInsightsAnalysisResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_insights_analysis


class StartNetworkInsightsAnalysisResult(TypedDict, closed=True):
    network_insights_analysis: NotRequired[
        "aws_sdk_ec2.types.network_insights_analysis.NetworkInsightsAnalysis"
    ]
    """<p>Information about the network insights analysis.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: StartNetworkInsightsAnalysisResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "network_insights_analysis" in value:
        import aws_sdk_ec2.types.network_insights_analysis

        aws_sdk_ec2.types.network_insights_analysis.serialize_ec2_query(
            value["network_insights_analysis"],
            pairs,
            f"{prefix}.NetworkInsightsAnalysis",
        )


def deserialize_ec2_query(el: Element) -> StartNetworkInsightsAnalysisResult:
    out: StartNetworkInsightsAnalysisResult = {}  # type: ignore[typeddict-item]
    child_network_insights_analysis = el.find("NetworkInsightsAnalysis")
    if child_network_insights_analysis is not None:
        import aws_sdk_ec2.types.network_insights_analysis

        out["network_insights_analysis"] = (
            aws_sdk_ec2.types.network_insights_analysis.deserialize_ec2_query(
                child_network_insights_analysis
            )
        )
    return out
