"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#CreateScheduledReportRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bcm_dashboards.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.client_token
    import aws_sdk_bcm_dashboards.types.resource_tag_list
    import aws_sdk_bcm_dashboards.types.scheduled_report_input


class CreateScheduledReportRequest(TypedDict):
    scheduled_report: (
        "aws_sdk_bcm_dashboards.types.scheduled_report_input.ScheduledReportInput"
    )
    """<p>The configuration for the scheduled report, including the dashboard to report on, the schedule, and the execution role that the service will use to generate the dashboard snapshot.</p>"""
    resource_tags: NotRequired[
        "aws_sdk_bcm_dashboards.types.resource_tag_list.ResourceTagList"
    ]
    """<p>The tags to apply to the scheduled report resource for organization and management.</p>"""
    client_token: NotRequired["aws_sdk_bcm_dashboards.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateScheduledReportRequest) -> dict:
    out: dict = {}
    import aws_sdk_bcm_dashboards.types.scheduled_report_input

    out["scheduledReport"] = (
        aws_sdk_bcm_dashboards.types.scheduled_report_input.serialize_aws_json_1_0(
            value["scheduled_report"]
        )
    )
    if "resource_tags" in value:
        import aws_sdk_bcm_dashboards.types.resource_tag_list

        out["resourceTags"] = (
            aws_sdk_bcm_dashboards.types.resource_tag_list.serialize_aws_json_1_0(
                value["resource_tags"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateScheduledReportRequest:
    out: CreateScheduledReportRequest = {}  # type: ignore[typeddict-item]
    if "scheduledReport" in data:
        import aws_sdk_bcm_dashboards.types.scheduled_report_input

        out["scheduled_report"] = (
            aws_sdk_bcm_dashboards.types.scheduled_report_input.deserialize_aws_json_1_0(
                data["scheduledReport"]
            )
        )
    else:
        raise DeserializationError(
            "CreateScheduledReportRequest.scheduled_report required"
        )
    if "resourceTags" in data:
        import aws_sdk_bcm_dashboards.types.resource_tag_list

        out["resource_tags"] = (
            aws_sdk_bcm_dashboards.types.resource_tag_list.deserialize_aws_json_1_0(
                data["resourceTags"]
            )
        )
    return out
