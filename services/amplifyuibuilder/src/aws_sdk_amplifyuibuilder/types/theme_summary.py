"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ThemeSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.theme_name
    import aws_sdk_amplifyuibuilder.types.uuid


class ThemeSummary(TypedDict):
    app_id: "str"
    """<p>The unique ID for the app associated with the theme summary.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment that is part of the Amplify app.</p>"""
    id: "aws_sdk_amplifyuibuilder.types.uuid.Uuid"
    """<p>The ID of the theme.</p>"""
    name: "aws_sdk_amplifyuibuilder.types.theme_name.ThemeName"
    """<p>The name of the theme.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThemeSummary) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    out["environmentName"] = value["environment_name"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> ThemeSummary:
    out: ThemeSummary = {}  # type: ignore[typeddict-item]
    if "appId" in data:
        out["app_id"] = data["appId"]
    else:
        raise DeserializationError("ThemeSummary.app_id required")
    if "environmentName" in data:
        out["environment_name"] = data["environmentName"]
    else:
        raise DeserializationError("ThemeSummary.environment_name required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ThemeSummary.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ThemeSummary.name required")
    return out
