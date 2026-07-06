"""Generated from Smithy shape ``com.amazonaws.workspacesweb#GetBrowserSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.browser_settings


class GetBrowserSettingsResponse(TypedDict, closed=True):
    browser_settings: NotRequired[
        "aws_sdk_workspaces_web.types.browser_settings.BrowserSettings"
    ]
    """<p>The browser settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBrowserSettingsResponse) -> dict:
    out: dict = {}
    if "browser_settings" in value:
        import aws_sdk_workspaces_web.types.browser_settings

        out["browserSettings"] = (
            aws_sdk_workspaces_web.types.browser_settings.serialize_json(
                value["browser_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetBrowserSettingsResponse:
    out: GetBrowserSettingsResponse = {}  # type: ignore[typeddict-item]
    if "browserSettings" in data:
        import aws_sdk_workspaces_web.types.browser_settings

        out["browser_settings"] = (
            aws_sdk_workspaces_web.types.browser_settings.deserialize_json(
                data["browserSettings"]
            )
        )
    return out
