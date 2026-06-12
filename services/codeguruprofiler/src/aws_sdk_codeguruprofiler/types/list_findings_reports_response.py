"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#ListFindingsReportsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codeguruprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.findings_report_summaries
    import aws_sdk_codeguruprofiler.types.pagination_token


class ListFindingsReportsResponse(TypedDict):
    findings_report_summaries: "aws_sdk_codeguruprofiler.types.findings_report_summaries.FindingsReportSummaries"
    """<p>The list of analysis results summaries.</p>"""
    next_token: NotRequired[
        "aws_sdk_codeguruprofiler.types.pagination_token.PaginationToken"
    ]
    """<p>The <code>nextToken</code> value to include in a future <code>ListFindingsReports</code> request. When the results of a <code>ListFindingsReports</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFindingsReportsResponse) -> dict:
    out: dict = {}
    import aws_sdk_codeguruprofiler.types.findings_report_summaries

    out["findingsReportSummaries"] = (
        aws_sdk_codeguruprofiler.types.findings_report_summaries.serialize_json(
            value["findings_report_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFindingsReportsResponse:
    out: ListFindingsReportsResponse = {}  # type: ignore[typeddict-item]
    if "findingsReportSummaries" in data:
        import aws_sdk_codeguruprofiler.types.findings_report_summaries

        out["findings_report_summaries"] = (
            aws_sdk_codeguruprofiler.types.findings_report_summaries.deserialize_json(
                data["findingsReportSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListFindingsReportsResponse.findings_report_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
