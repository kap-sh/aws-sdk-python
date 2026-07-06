"""Generated from Smithy shape ``com.amazonaws.applicationcostprofiler#DeleteReportDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_applicationcostprofiler.types.report_id


class DeleteReportDefinitionRequest(TypedDict, closed=True):
    report_id: "aws_sdk_applicationcostprofiler.types.report_id.ReportId"
    """<p>Required. ID of the report to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteReportDefinitionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteReportDefinitionRequest:
    out: DeleteReportDefinitionRequest = {}  # type: ignore[typeddict-item]
    return out
