"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeThemeAliasRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.alias_name
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.short_restrictive_resource_id


class DescribeThemeAliasRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the theme alias that you're describing.</p>"""
    theme_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID for the theme.</p>"""
    alias_name: "aws_sdk_quicksight.types.alias_name.AliasName"
    """<p>The name of the theme alias that you want to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeThemeAliasRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeThemeAliasRequest:
    out: DescribeThemeAliasRequest = {}  # type: ignore[typeddict-item]
    return out
