"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#CreateScheduledReportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bcm_dashboards.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.scheduled_report_arn


class CreateScheduledReportResponse(TypedDict, closed=True):
    arn: "aws_sdk_bcm_dashboards.types.scheduled_report_arn.ScheduledReportArn"
    """<p>The ARN of the newly created scheduled report.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateScheduledReportResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateScheduledReportResponse:
    out: CreateScheduledReportResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateScheduledReportResponse.arn required")
    return out
