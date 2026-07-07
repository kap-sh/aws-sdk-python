"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#UpdateThemeData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.theme_name
    import aws_sdk_amplifyuibuilder.types.theme_values_list
    import aws_sdk_amplifyuibuilder.types.uuid


class UpdateThemeData(TypedDict, closed=True):
    id: NotRequired["aws_sdk_amplifyuibuilder.types.uuid.Uuid"]
    """<p>The unique ID of the theme to update.</p>"""
    name: NotRequired["aws_sdk_amplifyuibuilder.types.theme_name.ThemeName"]
    """<p>The name of the theme to update.</p>"""
    values: "aws_sdk_amplifyuibuilder.types.theme_values_list.ThemeValuesList"
    """<p>A list of key-value pairs that define the theme's properties.</p>"""
    overrides: NotRequired[
        "aws_sdk_amplifyuibuilder.types.theme_values_list.ThemeValuesList"
    ]
    """<p>Describes the properties that can be overriden to customize the theme.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateThemeData) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    import aws_sdk_amplifyuibuilder.types.theme_values_list

    out["values"] = aws_sdk_amplifyuibuilder.types.theme_values_list.serialize_json(
        value["values"]
    )
    if "overrides" in value:
        import aws_sdk_amplifyuibuilder.types.theme_values_list

        out["overrides"] = (
            aws_sdk_amplifyuibuilder.types.theme_values_list.serialize_json(
                value["overrides"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateThemeData:
    out: UpdateThemeData = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "values" in data:
        import aws_sdk_amplifyuibuilder.types.theme_values_list

        out["values"] = (
            aws_sdk_amplifyuibuilder.types.theme_values_list.deserialize_json(
                data["values"]
            )
        )
    else:
        raise DeserializationError("UpdateThemeData.values required")
    if "overrides" in data:
        import aws_sdk_amplifyuibuilder.types.theme_values_list

        out["overrides"] = (
            aws_sdk_amplifyuibuilder.types.theme_values_list.deserialize_json(
                data["overrides"]
            )
        )
    return out
