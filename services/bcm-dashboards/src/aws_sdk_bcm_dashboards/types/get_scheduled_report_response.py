"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#GetScheduledReportResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bcm_dashboards.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.scheduled_report


class GetScheduledReportResponse(TypedDict):
    scheduled_report: "aws_sdk_bcm_dashboards.types.scheduled_report.ScheduledReport"
    """<p>The scheduled report configuration and metadata.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetScheduledReportResponse) -> dict:
    out: dict = {}
    import aws_sdk_bcm_dashboards.types.scheduled_report

    out["scheduledReport"] = (
        aws_sdk_bcm_dashboards.types.scheduled_report.serialize_aws_json_1_0(
            value["scheduled_report"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetScheduledReportResponse:
    out: GetScheduledReportResponse = {}  # type: ignore[typeddict-item]
    if "scheduledReport" in data:
        import aws_sdk_bcm_dashboards.types.scheduled_report

        out["scheduled_report"] = (
            aws_sdk_bcm_dashboards.types.scheduled_report.deserialize_aws_json_1_0(
                data["scheduledReport"]
            )
        )
    else:
        raise DeserializationError(
            "GetScheduledReportResponse.scheduled_report required"
        )
    return out
