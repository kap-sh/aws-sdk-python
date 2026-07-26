"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetConsolidatedReportOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.base64_string
    import capo_wellarchitected.types.consolidated_report_metrics
    import capo_wellarchitected.types.next_token


class GetConsolidatedReportOutput(TypedDict, closed=True):
    metrics: NotRequired[
        "capo_wellarchitected.types.consolidated_report_metrics.ConsolidatedReportMetrics"
    ]
    """<p>The metrics that make up the consolidated report.</p> <p>Only returned when <code>JSON</code> format is requested.</p>"""
    next_token: NotRequired["capo_wellarchitected.types.next_token.NextToken"]
    base64_string: NotRequired["capo_wellarchitected.types.base64_string.Base64String"]


# --- restJson1 ser/de ---
def serialize_json(value: GetConsolidatedReportOutput) -> dict:
    out: dict = {}
    if "metrics" in value:
        import capo_wellarchitected.types.consolidated_report_metrics

        out["Metrics"] = (
            capo_wellarchitected.types.consolidated_report_metrics.serialize_json(
                value["metrics"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "base64_string" in value:
        out["Base64String"] = value["base64_string"]
    return out


def deserialize_json(data: dict) -> GetConsolidatedReportOutput:
    out: GetConsolidatedReportOutput = {}  # type: ignore[typeddict-item]
    if "Metrics" in data:
        import capo_wellarchitected.types.consolidated_report_metrics

        out["metrics"] = (
            capo_wellarchitected.types.consolidated_report_metrics.deserialize_json(
                data["Metrics"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Base64String" in data:
        out["base64_string"] = data["Base64String"]
    return out
