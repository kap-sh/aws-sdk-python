"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateDashboardPublishedVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.version_number


class UpdateDashboardPublishedVersionRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the dashboard that you're updating.</p>"""
    dashboard_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID for the dashboard.</p>"""
    version_number: "aws_sdk_quicksight.types.version_number.VersionNumber"
    """<p>The version number of the dashboard.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDashboardPublishedVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UpdateDashboardPublishedVersionRequest:
    out: UpdateDashboardPublishedVersionRequest = {}  # type: ignore[typeddict-item]
    return out
