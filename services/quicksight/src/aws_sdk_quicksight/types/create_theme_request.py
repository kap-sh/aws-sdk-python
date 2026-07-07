"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateThemeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.resource_permission_list
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.tag_list
    import aws_sdk_quicksight.types.theme_configuration
    import aws_sdk_quicksight.types.theme_name
    import aws_sdk_quicksight.types.version_description


class CreateThemeRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account where you want to store the new theme. </p>"""
    theme_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>An ID for the theme that you want to create. The theme ID is unique per Amazon Web Services Region in each Amazon Web Services account.</p>"""
    name: "aws_sdk_quicksight.types.theme_name.ThemeName"
    """<p>A display name for the theme.</p>"""
    base_theme_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID of the theme that a custom theme will inherit from. All themes inherit from one of the starting themes defined by Amazon Quick Sight. For a list of the starting themes, use <code>ListThemes</code> or choose <b>Themes</b> from within an analysis. </p>"""
    version_description: NotRequired[
        "aws_sdk_quicksight.types.version_description.VersionDescription"
    ]
    """<p>A description of the first version of the theme that you're creating. Every time <code>UpdateTheme</code> is called, a new version is created. Each version of the theme has a description of the version in the <code>VersionDescription</code> field.</p>"""
    configuration: "aws_sdk_quicksight.types.theme_configuration.ThemeConfiguration"
    """<p>The theme configuration, which contains the theme display properties.</p>"""
    permissions: NotRequired[
        "aws_sdk_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>A valid grouping of resource permissions to apply to the new theme. </p>"""
    tags: NotRequired["aws_sdk_quicksight.types.tag_list.TagList"]
    """<p>A map of the key-value pairs for the resource tag or tags that you want to add to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateThemeRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["BaseThemeId"] = value["base_theme_id"]
    if "version_description" in value:
        out["VersionDescription"] = value["version_description"]
    import aws_sdk_quicksight.types.theme_configuration

    out["Configuration"] = aws_sdk_quicksight.types.theme_configuration.serialize_json(
        value["configuration"]
    )
    if "permissions" in value:
        import aws_sdk_quicksight.types.resource_permission_list

        out["Permissions"] = (
            aws_sdk_quicksight.types.resource_permission_list.serialize_json(
                value["permissions"]
            )
        )
    if "tags" in value:
        import aws_sdk_quicksight.types.tag_list

        out["Tags"] = aws_sdk_quicksight.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateThemeRequest:
    out: CreateThemeRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateThemeRequest.name required")
    if "BaseThemeId" in data:
        out["base_theme_id"] = data["BaseThemeId"]
    else:
        raise DeserializationError("CreateThemeRequest.base_theme_id required")
    if "VersionDescription" in data:
        out["version_description"] = data["VersionDescription"]
    if "Configuration" in data:
        import aws_sdk_quicksight.types.theme_configuration

        out["configuration"] = (
            aws_sdk_quicksight.types.theme_configuration.deserialize_json(
                data["Configuration"]
            )
        )
    else:
        raise DeserializationError("CreateThemeRequest.configuration required")
    if "Permissions" in data:
        import aws_sdk_quicksight.types.resource_permission_list

        out["permissions"] = (
            aws_sdk_quicksight.types.resource_permission_list.deserialize_json(
                data["Permissions"]
            )
        )
    if "Tags" in data:
        import aws_sdk_quicksight.types.tag_list

        out["tags"] = aws_sdk_quicksight.types.tag_list.deserialize_json(data["Tags"])
    return out
