"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeDashboardRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.alias_name
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.version_number


class DescribeDashboardRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the dashboard that you're describing.</p>"""
    dashboard_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID for the dashboard.</p>"""
    version_number: NotRequired["aws_sdk_quicksight.types.version_number.VersionNumber"]
    """<p>The version number for the dashboard. If a version number isn't passed, the latest published dashboard version is described. </p>"""
    alias_name: NotRequired["aws_sdk_quicksight.types.alias_name.AliasName"]
    """<p>The alias name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDashboardRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDashboardRequest:
    out: DescribeDashboardRequest = {}  # type: ignore[typeddict-item]
    return out
