"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateDashboardsQAConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.dashboards_qa_status


class UpdateDashboardsQAConfigurationRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the dashboard QA configuration that you want to update.</p>"""
    dashboards_qa_status: (
        "aws_sdk_quicksight.types.dashboards_qa_status.DashboardsQAStatus"
    )
    """<p>The status of dashboards QA configuration that you want to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDashboardsQAConfigurationRequest) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.dashboards_qa_status

    out["DashboardsQAStatus"] = (
        aws_sdk_quicksight.types.dashboards_qa_status.serialize_json(
            value["dashboards_qa_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateDashboardsQAConfigurationRequest:
    out: UpdateDashboardsQAConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "DashboardsQAStatus" in data:
        import aws_sdk_quicksight.types.dashboards_qa_status

        out["dashboards_qa_status"] = (
            aws_sdk_quicksight.types.dashboards_qa_status.deserialize_json(
                data["DashboardsQAStatus"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateDashboardsQAConfigurationRequest.dashboards_qa_status required"
        )
    return out
