"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetConsolidatedReportInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.get_consolidated_report_max_results
    import capo_wellarchitected.types.include_shared_resources
    import capo_wellarchitected.types.next_token
    import capo_wellarchitected.types.report_format


class GetConsolidatedReportInput(TypedDict, closed=True):
    format: NotRequired["capo_wellarchitected.types.report_format.ReportFormat"]
    """<p>The format of the consolidated report.</p> <p>For <code>PDF</code>, <code>Base64String</code> is returned. For <code>JSON</code>, <code>Metrics</code> is returned.</p>"""
    include_shared_resources: NotRequired[
        "capo_wellarchitected.types.include_shared_resources.IncludeSharedResources"
    ]
    """<p>Set to <code>true</code> to have shared resources included in the report.</p>"""
    next_token: NotRequired["capo_wellarchitected.types.next_token.NextToken"]
    max_results: NotRequired[
        "capo_wellarchitected.types.get_consolidated_report_max_results.GetConsolidatedReportMaxResults"
    ]
    """<p>The maximum number of results to return for this request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConsolidatedReportInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConsolidatedReportInput:
    out: GetConsolidatedReportInput = {}  # type: ignore[typeddict-item]
    return out
