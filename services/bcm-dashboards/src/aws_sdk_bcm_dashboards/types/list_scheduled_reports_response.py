"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#ListScheduledReportsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bcm_dashboards.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.next_page_token
    import aws_sdk_bcm_dashboards.types.scheduled_report_summary_list


class ListScheduledReportsResponse(TypedDict, closed=True):
    scheduled_reports: "aws_sdk_bcm_dashboards.types.scheduled_report_summary_list.ScheduledReportSummaryList"
    """<p>An array of scheduled report summaries, containing basic information about each scheduled report.</p>"""
    next_token: NotRequired[
        "aws_sdk_bcm_dashboards.types.next_page_token.NextPageToken"
    ]
    """<p>The token to use to retrieve the next page of results. Not returned if there are no more results to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListScheduledReportsResponse) -> dict:
    out: dict = {}
    import aws_sdk_bcm_dashboards.types.scheduled_report_summary_list

    out["scheduledReports"] = (
        aws_sdk_bcm_dashboards.types.scheduled_report_summary_list.serialize_aws_json_1_0(
            value["scheduled_reports"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListScheduledReportsResponse:
    out: ListScheduledReportsResponse = {}  # type: ignore[typeddict-item]
    if "scheduledReports" in data:
        import aws_sdk_bcm_dashboards.types.scheduled_report_summary_list

        out["scheduled_reports"] = (
            aws_sdk_bcm_dashboards.types.scheduled_report_summary_list.deserialize_aws_json_1_0(
                data["scheduledReports"]
            )
        )
    else:
        raise DeserializationError(
            "ListScheduledReportsResponse.scheduled_reports required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
