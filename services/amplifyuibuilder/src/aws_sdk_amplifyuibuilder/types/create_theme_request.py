"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CreateThemeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.create_theme_data


class CreateThemeRequest(TypedDict, closed=True):
    app_id: "str"
    """<p>The unique ID of the Amplify app associated with the theme.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment that is a part of the Amplify app.</p>"""
    client_token: NotRequired["str"]
    """<p>The unique client token.</p>"""
    theme_to_create: "aws_sdk_amplifyuibuilder.types.create_theme_data.CreateThemeData"
    """<p>Represents the configuration of the theme to create.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateThemeRequest) -> dict:
    out: dict = {}
    import aws_sdk_amplifyuibuilder.types.create_theme_data

    out["themeToCreate"] = (
        aws_sdk_amplifyuibuilder.types.create_theme_data.serialize_json(
            value["theme_to_create"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateThemeRequest:
    out: CreateThemeRequest = {}  # type: ignore[typeddict-item]
    if "themeToCreate" in data:
        import aws_sdk_amplifyuibuilder.types.create_theme_data

        out["theme_to_create"] = (
            aws_sdk_amplifyuibuilder.types.create_theme_data.deserialize_json(
                data["themeToCreate"]
            )
        )
    else:
        raise DeserializationError("CreateThemeRequest.theme_to_create required")
    return out
