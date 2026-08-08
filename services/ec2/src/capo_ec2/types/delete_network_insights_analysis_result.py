"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteNetworkInsightsAnalysisResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.network_insights_analysis_id


class DeleteNetworkInsightsAnalysisResult(TypedDict, closed=True):
    network_insights_analysis_id: NotRequired[
        "capo_ec2.types.network_insights_analysis_id.NetworkInsightsAnalysisId"
    ]
    """<p>The ID of the network insights analysis.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteNetworkInsightsAnalysisResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "network_insights_analysis_id" in value:
        pairs.append(
            (
                f"{key_prefix}NetworkInsightsAnalysisId",
                str(value["network_insights_analysis_id"]),
            )
        )


def deserialize_ec2_query(el: Element) -> DeleteNetworkInsightsAnalysisResult:
    out: DeleteNetworkInsightsAnalysisResult = {}  # type: ignore[typeddict-item]
    child_network_insights_analysis_id = el.find("networkInsightsAnalysisId")
    if child_network_insights_analysis_id is not None:
        out["network_insights_analysis_id"] = str(
            child_network_insights_analysis_id.text or ""
        )
    return out
