"""Generated from Smithy shape ``com.amazonaws.inspector2#GetFindingsReportStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.destination
    import capo_inspector2.types.error_message
    import capo_inspector2.types.external_report_status
    import capo_inspector2.types.filter_criteria
    import capo_inspector2.types.report_id
    import capo_inspector2.types.reporting_error_code


class GetFindingsReportStatusResponse(TypedDict, closed=True):
    report_id: NotRequired["capo_inspector2.types.report_id.ReportId"]
    """<p>The ID of the report.</p>"""
    status: NotRequired[
        "capo_inspector2.types.external_report_status.ExternalReportStatus"
    ]
    """<p>The status of the report.</p>"""
    error_code: NotRequired[
        "capo_inspector2.types.reporting_error_code.ReportingErrorCode"
    ]
    """<p>The error code of the report.</p>"""
    error_message: NotRequired["capo_inspector2.types.error_message.ErrorMessage"]
    """<p>The error message of the report.</p>"""
    destination: NotRequired["capo_inspector2.types.destination.Destination"]
    """<p>The destination of the report.</p>"""
    filter_criteria: NotRequired["capo_inspector2.types.filter_criteria.FilterCriteria"]
    """<p>The filter criteria associated with the report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingsReportStatusResponse) -> dict:
    out: dict = {}
    if "report_id" in value:
        out["reportId"] = value["report_id"]
    if "status" in value:
        out["status"] = value["status"]
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "destination" in value:
        import capo_inspector2.types.destination

        out["destination"] = capo_inspector2.types.destination.serialize_json(
            value["destination"]
        )
    if "filter_criteria" in value:
        import capo_inspector2.types.filter_criteria

        out["filterCriteria"] = capo_inspector2.types.filter_criteria.serialize_json(
            value["filter_criteria"]
        )
    return out


def deserialize_json(data: dict) -> GetFindingsReportStatusResponse:
    out: GetFindingsReportStatusResponse = {}  # type: ignore[typeddict-item]
    if "reportId" in data:
        out["report_id"] = data["reportId"]
    if "status" in data:
        out["status"] = data["status"]
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    if "destination" in data:
        import capo_inspector2.types.destination

        out["destination"] = capo_inspector2.types.destination.deserialize_json(
            data["destination"]
        )
    if "filterCriteria" in data:
        import capo_inspector2.types.filter_criteria

        out["filter_criteria"] = capo_inspector2.types.filter_criteria.deserialize_json(
            data["filterCriteria"]
        )
    return out
