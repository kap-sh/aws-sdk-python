"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetConsolidatedReportInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.get_consolidated_report_max_results
    import aws_sdk_wellarchitected.types.include_shared_resources
    import aws_sdk_wellarchitected.types.next_token
    import aws_sdk_wellarchitected.types.report_format


class GetConsolidatedReportInput(TypedDict):
    format: NotRequired["aws_sdk_wellarchitected.types.report_format.ReportFormat"]
    """<p>The format of the consolidated report.</p> <p>For <code>PDF</code>, <code>Base64String</code> is returned. For <code>JSON</code>, <code>Metrics</code> is returned.</p>"""
    include_shared_resources: NotRequired[
        "aws_sdk_wellarchitected.types.include_shared_resources.IncludeSharedResources"
    ]
    """<p>Set to <code>true</code> to have shared resources included in the report.</p>"""
    next_token: NotRequired["aws_sdk_wellarchitected.types.next_token.NextToken"]
    max_results: NotRequired[
        "aws_sdk_wellarchitected.types.get_consolidated_report_max_results.GetConsolidatedReportMaxResults"
    ]
    """<p>The maximum number of results to return for this request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConsolidatedReportInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConsolidatedReportInput:
    out: GetConsolidatedReportInput = {}  # type: ignore[typeddict-item]
    return out
