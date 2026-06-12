"""Generated from Smithy shape ``com.amazonaws.applicationcostprofiler#GetReportDefinitionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_applicationcostprofiler.types.report_id


class GetReportDefinitionRequest(TypedDict):
    report_id: "aws_sdk_applicationcostprofiler.types.report_id.ReportId"
    """<p>ID of the report to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReportDefinitionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetReportDefinitionRequest:
    out: GetReportDefinitionRequest = {}  # type: ignore[typeddict-item]
    return out
