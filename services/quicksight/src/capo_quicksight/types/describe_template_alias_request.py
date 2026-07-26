"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeTemplateAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.alias_name
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.short_restrictive_resource_id


class DescribeTemplateAliasRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the template alias that you're describing.</p>"""
    template_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID for the template.</p>"""
    alias_name: "capo_quicksight.types.alias_name.AliasName"
    """<p>The name of the template alias that you want to describe. If you name a specific alias, you describe the version that the alias points to. You can specify the latest version of the template by providing the keyword <code>$LATEST</code> in the <code>AliasName</code> parameter. The keyword <code>$PUBLISHED</code> doesn't apply to templates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTemplateAliasRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeTemplateAliasRequest:
    out: DescribeTemplateAliasRequest = {}  # type: ignore[typeddict-item]
    return out
