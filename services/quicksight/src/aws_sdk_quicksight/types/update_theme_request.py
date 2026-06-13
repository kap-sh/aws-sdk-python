"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateThemeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.theme_configuration
    import aws_sdk_quicksight.types.theme_name
    import aws_sdk_quicksight.types.version_description


class UpdateThemeRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the theme that you're updating.</p>"""
    theme_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID for the theme.</p>"""
    name: NotRequired["aws_sdk_quicksight.types.theme_name.ThemeName"]
    """<p>The name for the theme.</p>"""
    base_theme_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The theme ID, defined by Amazon Quick Sight, that a custom theme inherits from. All themes initially inherit from a default Quick Sight theme.</p>"""
    version_description: NotRequired[
        "aws_sdk_quicksight.types.version_description.VersionDescription"
    ]
    """<p>A description of the theme version that you're updating Every time that you call <code>UpdateTheme</code>, you create a new version of the theme. Each version of the theme maintains a description of the version in <code>VersionDescription</code>.</p>"""
    configuration: NotRequired[
        "aws_sdk_quicksight.types.theme_configuration.ThemeConfiguration"
    ]
    """<p>The theme configuration, which contains the theme display properties.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateThemeRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    out["BaseThemeId"] = value["base_theme_id"]
    if "version_description" in value:
        out["VersionDescription"] = value["version_description"]
    if "configuration" in value:
        import aws_sdk_quicksight.types.theme_configuration

        out["Configuration"] = (
            aws_sdk_quicksight.types.theme_configuration.serialize_json(
                value["configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateThemeRequest:
    out: UpdateThemeRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "BaseThemeId" in data:
        out["base_theme_id"] = data["BaseThemeId"]
    else:
        raise DeserializationError("UpdateThemeRequest.base_theme_id required")
    if "VersionDescription" in data:
        out["version_description"] = data["VersionDescription"]
    if "Configuration" in data:
        import aws_sdk_quicksight.types.theme_configuration

        out["configuration"] = (
            aws_sdk_quicksight.types.theme_configuration.deserialize_json(
                data["Configuration"]
            )
        )
    return out
