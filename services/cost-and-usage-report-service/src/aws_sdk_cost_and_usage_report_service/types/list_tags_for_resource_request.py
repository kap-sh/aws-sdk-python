"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cost_and_usage_report_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_and_usage_report_service.types.report_name


class ListTagsForResourceRequest(TypedDict):
    report_name: "aws_sdk_cost_and_usage_report_service.types.report_name.ReportName"
    """<p>The report name of the report definition that tags are to be returned for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    out["ReportName"] = value["report_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if "ReportName" in data:
        out["report_name"] = data["ReportName"]
    else:
        raise DeserializationError("ListTagsForResourceRequest.report_name required")
    return out
