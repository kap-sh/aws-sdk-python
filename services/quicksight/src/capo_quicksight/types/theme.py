"""Generated from Smithy shape ``com.amazonaws.quicksight#Theme``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.theme_name
    import capo_quicksight.types.theme_type
    import capo_quicksight.types.theme_version
    import capo_quicksight.types.timestamp


class Theme(TypedDict, closed=True):
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the theme.</p>"""
    name: NotRequired["capo_quicksight.types.theme_name.ThemeName"]
    """<p>The name that the user gives to the theme.</p>"""
    theme_id: NotRequired[
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The identifier that the user gives to the theme.</p>"""
    version: NotRequired["capo_quicksight.types.theme_version.ThemeVersion"]
    created_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The date and time that the theme was created.</p>"""
    last_updated_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The date and time that the theme was last updated.</p>"""
    type: NotRequired["capo_quicksight.types.theme_type.ThemeType"]
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
        import capo_quicksight.types.theme_version

        out["Version"] = capo_quicksight.types.theme_version.serialize_json(
            value["version"]
        )
    if "created_time" in value:
        import capo_quicksight.types.timestamp

        out["CreatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "last_updated_time" in value:
        import capo_quicksight.types.timestamp

        out["LastUpdatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    if "type" in value:
        import capo_quicksight.types.theme_type

        out["Type"] = capo_quicksight.types.theme_type.serialize_json(value["type"])
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
        import capo_quicksight.types.theme_version

        out["version"] = capo_quicksight.types.theme_version.deserialize_json(
            data["Version"]
        )
    if "CreatedTime" in data:
        import capo_quicksight.types.timestamp

        out["created_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "LastUpdatedTime" in data:
        import capo_quicksight.types.timestamp

        out["last_updated_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    if "Type" in data:
        import capo_quicksight.types.theme_type

        out["type"] = capo_quicksight.types.theme_type.deserialize_json(data["Type"])
    return out
