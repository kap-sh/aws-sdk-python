"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#GetScheduledReportRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bcm_dashboards.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.scheduled_report_arn


class GetScheduledReportRequest(TypedDict):
    arn: "aws_sdk_bcm_dashboards.types.scheduled_report_arn.ScheduledReportArn"
    """<p>The ARN of the scheduled report to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetScheduledReportRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetScheduledReportRequest:
    out: GetScheduledReportRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetScheduledReportRequest.arn required")
    return out
