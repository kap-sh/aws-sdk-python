"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateDashboardsQAConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dashboards_qa_status
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class UpdateDashboardsQAConfigurationResponse(TypedDict):
    dashboards_qa_status: NotRequired[
        "aws_sdk_quicksight.types.dashboards_qa_status.DashboardsQAStatus"
    ]
    """<p>A value that indicates whether the dashboard QA configuration is enabled or not.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDashboardsQAConfigurationResponse) -> dict:
    out: dict = {}
    if "dashboards_qa_status" in value:
        import aws_sdk_quicksight.types.dashboards_qa_status

        out["DashboardsQAStatus"] = (
            aws_sdk_quicksight.types.dashboards_qa_status.serialize_json(
                value["dashboards_qa_status"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UpdateDashboardsQAConfigurationResponse:
    out: UpdateDashboardsQAConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "DashboardsQAStatus" in data:
        import aws_sdk_quicksight.types.dashboards_qa_status

        out["dashboards_qa_status"] = (
            aws_sdk_quicksight.types.dashboards_qa_status.deserialize_json(
                data["DashboardsQAStatus"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
