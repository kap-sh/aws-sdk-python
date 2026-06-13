"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteTemplateAliasRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.alias_name
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.short_restrictive_resource_id


class DeleteTemplateAliasRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the item to delete.</p>"""
    template_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID for the template that the specified alias is for.</p>"""
    alias_name: "aws_sdk_quicksight.types.alias_name.AliasName"
    """<p>The name for the template alias. To delete a specific alias, you delete the version that the alias points to. You can specify the alias name, or specify the latest version of the template by providing the keyword <code>$LATEST</code> in the <code>AliasName</code> parameter. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTemplateAliasRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTemplateAliasRequest:
    out: DeleteTemplateAliasRequest = {}  # type: ignore[typeddict-item]
    return out
