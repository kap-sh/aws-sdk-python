"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#DeleteReportDefinitionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cost_and_usage_report_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_and_usage_report_service.types.report_name


class DeleteReportDefinitionRequest(TypedDict):
    report_name: "aws_sdk_cost_and_usage_report_service.types.report_name.ReportName"
    """<p>The name of the report that you want to delete. The name must be unique, is case sensitive, and can't include spaces.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteReportDefinitionRequest) -> dict:
    out: dict = {}
    out["ReportName"] = value["report_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteReportDefinitionRequest:
    out: DeleteReportDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "ReportName" in data:
        out["report_name"] = data["ReportName"]
    else:
        raise DeserializationError("DeleteReportDefinitionRequest.report_name required")
    return out
