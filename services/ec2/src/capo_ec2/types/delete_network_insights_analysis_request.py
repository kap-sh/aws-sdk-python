"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteNetworkInsightsAnalysisRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.network_insights_analysis_id


class DeleteNetworkInsightsAnalysisRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    network_insights_analysis_id: NotRequired[
        "capo_ec2.types.network_insights_analysis_id.NetworkInsightsAnalysisId"
    ]
    """<p>The ID of the network insights analysis.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteNetworkInsightsAnalysisRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "network_insights_analysis_id" in value:
        pairs.append(
            (
                f"{prefix}.NetworkInsightsAnalysisId",
                str(value["network_insights_analysis_id"]),
            )
        )


def deserialize_ec2_query(el: Element) -> DeleteNetworkInsightsAnalysisRequest:
    out: DeleteNetworkInsightsAnalysisRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_network_insights_analysis_id = el.find("NetworkInsightsAnalysisId")
    if child_network_insights_analysis_id is not None:
        out["network_insights_analysis_id"] = str(
            child_network_insights_analysis_id.text or ""
        )
    return out
