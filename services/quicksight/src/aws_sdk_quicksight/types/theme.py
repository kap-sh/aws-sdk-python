"""Generated from Smithy shape ``com.amazonaws.quicksight#Theme``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.theme_name
    import aws_sdk_quicksight.types.theme_type
    import aws_sdk_quicksight.types.theme_version
    import aws_sdk_quicksight.types.timestamp


class Theme(TypedDict):
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the theme.</p>"""
    name: NotRequired["aws_sdk_quicksight.types.theme_name.ThemeName"]
    """<p>The name that the user gives to the theme.</p>"""
    theme_id: NotRequired[
        "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The identifier that the user gives to the theme.</p>"""
    version: NotRequired["aws_sdk_quicksight.types.theme_version.ThemeVersion"]
    created_time: NotRequired["aws_sdk_quicksight.types.timestamp.Timestamp"]
    """<p>The date and time that the theme was created.</p>"""
    last_updated_time: NotRequired["aws_sdk_quicksight.types.timestamp.Timestamp"]
    """<p>The date and time that the theme was last updated.</p>"""
    type: NotRequired["aws_sdk_quicksight.types.theme_type.ThemeType"]
    """<p>The type of theme, based on how it was created. Valid values include: <code>QUICKSIGHT</code> and <code>CUSTOM</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Theme) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "theme_id" in value:
        out["ThemeId"] = value["theme_id"]
    if "version" in value:
        import aws_sdk_quicksight.types.theme_version

        out["Version"] = aws_sdk_quicksight.types.theme_version.serialize_json(
            value["version"]
        )
    if "created_time" in value:
        import aws_sdk_quicksight.types.timestamp

        out["CreatedTime"] = aws_sdk_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "last_updated_time" in value:
        import aws_sdk_quicksight.types.timestamp

        out["LastUpdatedTime"] = aws_sdk_quicksight.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    if "type" in value:
        import aws_sdk_quicksight.types.theme_type

        out["Type"] = aws_sdk_quicksight.types.theme_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> Theme:
    out: Theme = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ThemeId" in data:
        out["theme_id"] = data["ThemeId"]
    if "Version" in data:
        import aws_sdk_quicksight.types.theme_version

        out["version"] = aws_sdk_quicksight.types.theme_version.deserialize_json(
            data["Version"]
        )
    if "CreatedTime" in data:
        import aws_sdk_quicksight.types.timestamp

        out["created_time"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "LastUpdatedTime" in data:
        import aws_sdk_quicksight.types.timestamp

        out["last_updated_time"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    if "Type" in data:
        import aws_sdk_quicksight.types.theme_type

        out["type"] = aws_sdk_quicksight.types.theme_type.deserialize_json(data["Type"])
    return out
