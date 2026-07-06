"""Generated from Smithy shape ``com.amazonaws.quicksight#ThemeVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.resource_status
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.theme_configuration
    import aws_sdk_quicksight.types.theme_error_list
    import aws_sdk_quicksight.types.timestamp
    import aws_sdk_quicksight.types.version_description
    import aws_sdk_quicksight.types.version_number


class ThemeVersion(TypedDict, closed=True):
    version_number: NotRequired["aws_sdk_quicksight.types.version_number.VersionNumber"]
    """<p>The version number of the theme.</p>"""
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    description: NotRequired[
        "aws_sdk_quicksight.types.version_description.VersionDescription"
    ]
    """<p>The description of the theme.</p>"""
    base_theme_id: NotRequired[
        "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The Quick Sight-defined ID of the theme that a custom theme inherits from. All themes initially inherit from a default Quick Sight theme.</p>"""
    created_time: NotRequired["aws_sdk_quicksight.types.timestamp.Timestamp"]
    """<p>The date and time that this theme version was created.</p>"""
    configuration: NotRequired[
        "aws_sdk_quicksight.types.theme_configuration.ThemeConfiguration"
    ]
    """<p>The theme configuration, which contains all the theme display properties.</p>"""
    errors: NotRequired["aws_sdk_quicksight.types.theme_error_list.ThemeErrorList"]
    """<p>Errors associated with the theme.</p>"""
    status: NotRequired["aws_sdk_quicksight.types.resource_status.ResourceStatus"]
    """<p>The status of the theme version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThemeVersion) -> dict:
    out: dict = {}
    if "version_number" in value:
        out["VersionNumber"] = value["version_number"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "base_theme_id" in value:
        out["BaseThemeId"] = value["base_theme_id"]
    if "created_time" in value:
        import aws_sdk_quicksight.types.timestamp

        out["CreatedTime"] = aws_sdk_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "configuration" in value:
        import aws_sdk_quicksight.types.theme_configuration

        out["Configuration"] = (
            aws_sdk_quicksight.types.theme_configuration.serialize_json(
                value["configuration"]
            )
        )
    if "errors" in value:
        import aws_sdk_quicksight.types.theme_error_list

        out["Errors"] = aws_sdk_quicksight.types.theme_error_list.serialize_json(
            value["errors"]
        )
    if "status" in value:
        import aws_sdk_quicksight.types.resource_status

        out["Status"] = aws_sdk_quicksight.types.resource_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> ThemeVersion:
    out: ThemeVersion = {}  # type: ignore[typeddict-item]
    if "VersionNumber" in data:
        out["version_number"] = data["VersionNumber"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "BaseThemeId" in data:
        out["base_theme_id"] = data["BaseThemeId"]
    if "CreatedTime" in data:
        import aws_sdk_quicksight.types.timestamp

        out["created_time"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "Configuration" in data:
        import aws_sdk_quicksight.types.theme_configuration

        out["configuration"] = (
            aws_sdk_quicksight.types.theme_configuration.deserialize_json(
                data["Configuration"]
            )
        )
    if "Errors" in data:
        import aws_sdk_quicksight.types.theme_error_list

        out["errors"] = aws_sdk_quicksight.types.theme_error_list.deserialize_json(
            data["Errors"]
        )
    if "Status" in data:
        import aws_sdk_quicksight.types.resource_status

        out["status"] = aws_sdk_quicksight.types.resource_status.deserialize_json(
            data["Status"]
        )
    return out
