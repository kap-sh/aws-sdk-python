"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateThemeAliasRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.alias_name
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.version_number


class UpdateThemeAliasRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the theme alias that you're updating.</p>"""
    theme_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID for the theme.</p>"""
    alias_name: "aws_sdk_quicksight.types.alias_name.AliasName"
    """<p>The name of the theme alias that you want to update.</p>"""
    theme_version_number: "aws_sdk_quicksight.types.version_number.VersionNumber"
    """<p>The version number of the theme that the alias should reference.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateThemeAliasRequest) -> dict:
    out: dict = {}
    out["ThemeVersionNumber"] = value["theme_version_number"]
    return out


def deserialize_json(data: dict) -> UpdateThemeAliasRequest:
    out: UpdateThemeAliasRequest = {}  # type: ignore[typeddict-item]
    if "ThemeVersionNumber" in data:
        out["theme_version_number"] = data["ThemeVersionNumber"]
    else:
        raise DeserializationError(
            "UpdateThemeAliasRequest.theme_version_number required"
        )
    return out
