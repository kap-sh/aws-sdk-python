"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.alias_name
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.version_number


class DescribeTemplateRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the template that you're describing.</p>"""
    template_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID for the template.</p>"""
    version_number: NotRequired["aws_sdk_quicksight.types.version_number.VersionNumber"]
    """<p>(Optional) The number for the version to describe. If a <code>VersionNumber</code> parameter value isn't provided, the latest version of the template is described.</p>"""
    alias_name: NotRequired["aws_sdk_quicksight.types.alias_name.AliasName"]
    """<p>The alias of the template that you want to describe. If you name a specific alias, you describe the version that the alias points to. You can specify the latest version of the template by providing the keyword <code>$LATEST</code> in the <code>AliasName</code> parameter. The keyword <code>$PUBLISHED</code> doesn't apply to templates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeTemplateRequest:
    out: DescribeTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
