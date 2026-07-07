"""Generated from Smithy shape ``com.amazonaws.workspacesweb#UpdateBrowserSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.browser_settings


class UpdateBrowserSettingsResponse(TypedDict, closed=True):
    browser_settings: "aws_sdk_workspaces_web.types.browser_settings.BrowserSettings"
    """<p>The browser settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBrowserSettingsResponse) -> dict:
    out: dict = {}
    import aws_sdk_workspaces_web.types.browser_settings

    out["browserSettings"] = (
        aws_sdk_workspaces_web.types.browser_settings.serialize_json(
            value["browser_settings"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateBrowserSettingsResponse:
    out: UpdateBrowserSettingsResponse = {}  # type: ignore[typeddict-item]
    if "browserSettings" in data:
        import aws_sdk_workspaces_web.types.browser_settings

        out["browser_settings"] = (
            aws_sdk_workspaces_web.types.browser_settings.deserialize_json(
                data["browserSettings"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateBrowserSettingsResponse.browser_settings required"
        )
    return out
