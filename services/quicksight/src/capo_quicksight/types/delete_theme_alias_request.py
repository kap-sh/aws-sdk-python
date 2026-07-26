"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteThemeAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.alias_name
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.short_restrictive_resource_id


class DeleteThemeAliasRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the theme alias to delete.</p>"""
    theme_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID for the theme that the specified alias is for.</p>"""
    alias_name: "capo_quicksight.types.alias_name.AliasName"
    """<p>The unique name for the theme alias to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteThemeAliasRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteThemeAliasRequest:
    out: DeleteThemeAliasRequest = {}  # type: ignore[typeddict-item]
    return out
