"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateThemeAliasRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.alias_name
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.version_number


class CreateThemeAliasRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the theme for the new theme alias.</p>"""
    theme_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>An ID for the theme alias.</p>"""
    alias_name: "aws_sdk_quicksight.types.alias_name.AliasName"
    """<p>The name that you want to give to the theme alias that you are creating. The alias name can't begin with a <code>$</code>. Alias names that start with <code>$</code> are reserved by Amazon Quick Sight. </p>"""
    theme_version_number: "aws_sdk_quicksight.types.version_number.VersionNumber"
    """<p>The version number of the theme.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateThemeAliasRequest) -> dict:
    out: dict = {}
    out["ThemeVersionNumber"] = value["theme_version_number"]
    return out


def deserialize_json(data: dict) -> CreateThemeAliasRequest:
    out: CreateThemeAliasRequest = {}  # type: ignore[typeddict-item]
    if "ThemeVersionNumber" in data:
        out["theme_version_number"] = data["ThemeVersionNumber"]
    else:
        raise DeserializationError(
            "CreateThemeAliasRequest.theme_version_number required"
        )
    return out
