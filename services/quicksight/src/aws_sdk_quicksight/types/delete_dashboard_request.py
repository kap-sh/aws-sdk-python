"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteDashboardRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.version_number


class DeleteDashboardRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the dashboard that you're deleting.</p>"""
    dashboard_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID for the dashboard.</p>"""
    version_number: NotRequired["aws_sdk_quicksight.types.version_number.VersionNumber"]
    """<p>The version number of the dashboard. If the version number property is provided, only the specified version of the dashboard is deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDashboardRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDashboardRequest:
    out: DeleteDashboardRequest = {}  # type: ignore[typeddict-item]
    return out
