"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeThemePermissionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.short_restrictive_resource_id


class DescribeThemePermissionsRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the theme that you're describing.</p>"""
    theme_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID for the theme that you want to describe permissions for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeThemePermissionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeThemePermissionsRequest:
    out: DescribeThemePermissionsRequest = {}  # type: ignore[typeddict-item]
    return out
