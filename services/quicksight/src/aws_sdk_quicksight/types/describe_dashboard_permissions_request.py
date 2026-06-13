"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeDashboardPermissionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.short_restrictive_resource_id


class DescribeDashboardPermissionsRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the dashboard that you're describing permissions for.</p>"""
    dashboard_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID for the dashboard, also added to the IAM policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDashboardPermissionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDashboardPermissionsRequest:
    out: DescribeDashboardPermissionsRequest = {}  # type: ignore[typeddict-item]
    return out
