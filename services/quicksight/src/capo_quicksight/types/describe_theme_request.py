"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeThemeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.alias_name
    import capo_quicksight.types.aws_and_account_id
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.version_number


class DescribeThemeRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_and_account_id.AwsAndAccountId"
    """<p>The ID of the Amazon Web Services account that contains the theme that you're describing.</p>"""
    theme_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID for the theme.</p>"""
    version_number: NotRequired["capo_quicksight.types.version_number.VersionNumber"]
    """<p>The version number for the version to describe. If a <code>VersionNumber</code> parameter value isn't provided, the latest version of the theme is described.</p>"""
    alias_name: NotRequired["capo_quicksight.types.alias_name.AliasName"]
    """<p>The alias of the theme that you want to describe. If you name a specific alias, you describe the version that the alias points to. You can specify the latest version of the theme by providing the keyword <code>$LATEST</code> in the <code>AliasName</code> parameter. The keyword <code>$PUBLISHED</code> doesn't apply to themes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeThemeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeThemeRequest:
    out: DescribeThemeRequest = {}  # type: ignore[typeddict-item]
    return out
