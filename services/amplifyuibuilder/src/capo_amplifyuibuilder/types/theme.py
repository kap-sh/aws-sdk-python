"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#Theme``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_amplifyuibuilder.types.tags
    import capo_amplifyuibuilder.types.theme_name
    import capo_amplifyuibuilder.types.theme_values_list
    import capo_amplifyuibuilder.types.uuid


class Theme(TypedDict, closed=True):
    app_id: "str"
    """<p>The unique ID for the Amplify app associated with the theme.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment that is a part of the Amplify app.</p>"""
    id: "capo_amplifyuibuilder.types.uuid.Uuid"
    """<p>The ID for the theme.</p>"""
    name: "capo_amplifyuibuilder.types.theme_name.ThemeName"
    """<p>The name of the theme.</p>"""
    created_at: "datetime.datetime"
    """<p>The time that the theme was created.</p>"""
    modified_at: NotRequired["datetime.datetime"]
    """<p>The time that the theme was modified.</p>"""
    values: "capo_amplifyuibuilder.types.theme_values_list.ThemeValuesList"
    """<p>A list of key-value pairs that defines the properties of the theme.</p>"""
    overrides: NotRequired[
        "capo_amplifyuibuilder.types.theme_values_list.ThemeValuesList"
    ]
    """<p>Describes the properties that can be overriden to customize a theme.</p>"""
    tags: NotRequired["capo_amplifyuibuilder.types.tags.Tags"]
    """<p>One or more key-value pairs to use when tagging the theme.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Theme) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    out["environmentName"] = value["environment_name"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    import capo_amplifyuibuilder.types._prelude.timestamp

    out["createdAt"] = capo_amplifyuibuilder.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    if "modified_at" in value:
        import capo_amplifyuibuilder.types._prelude.timestamp

        out["modifiedAt"] = (
            capo_amplifyuibuilder.types._prelude.timestamp.serialize_json(
                value["modified_at"]
            )
        )
    import capo_amplifyuibuilder.types.theme_values_list

    out["values"] = capo_amplifyuibuilder.types.theme_values_list.serialize_json(
        value["values"]
    )
    if "overrides" in value:
        import capo_amplifyuibuilder.types.theme_values_list

        out["overrides"] = capo_amplifyuibuilder.types.theme_values_list.serialize_json(
            value["overrides"]
        )
    if "tags" in value:
        import capo_amplifyuibuilder.types.tags

        out["tags"] = capo_amplifyuibuilder.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> Theme:
    out: Theme = {}  # type: ignore[typeddict-item]
    if "appId" in data:
        out["app_id"] = data["appId"]
    else:
        raise DeserializationError("Theme.app_id required")
    if "environmentName" in data:
        out["environment_name"] = data["environmentName"]
    else:
        raise DeserializationError("Theme.environment_name required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("Theme.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Theme.name required")
    if "createdAt" in data:
        import capo_amplifyuibuilder.types._prelude.timestamp

        out["created_at"] = (
            capo_amplifyuibuilder.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("Theme.created_at required")
    if "modifiedAt" in data:
        import capo_amplifyuibuilder.types._prelude.timestamp

        out["modified_at"] = (
            capo_amplifyuibuilder.types._prelude.timestamp.deserialize_json(
                data["modifiedAt"]
            )
        )
    if "values" in data:
        import capo_amplifyuibuilder.types.theme_values_list

        out["values"] = capo_amplifyuibuilder.types.theme_values_list.deserialize_json(
            data["values"]
        )
    else:
        raise DeserializationError("Theme.values required")
    if "overrides" in data:
        import capo_amplifyuibuilder.types.theme_values_list

        out["overrides"] = (
            capo_amplifyuibuilder.types.theme_values_list.deserialize_json(
                data["overrides"]
            )
        )
    if "tags" in data:
        import capo_amplifyuibuilder.types.tags

        out["tags"] = capo_amplifyuibuilder.types.tags.deserialize_json(data["tags"])
    return out
