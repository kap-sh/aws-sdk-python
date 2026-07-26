"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeThemeAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.alias_name
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.short_restrictive_resource_id


class DescribeThemeAliasRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the theme alias that you're describing.</p>"""
    theme_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID for the theme.</p>"""
    alias_name: "capo_quicksight.types.alias_name.AliasName"
    """<p>The name of the theme alias that you want to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeThemeAliasRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeThemeAliasRequest:
    out: DescribeThemeAliasRequest = {}  # type: ignore[typeddict-item]
    return out
