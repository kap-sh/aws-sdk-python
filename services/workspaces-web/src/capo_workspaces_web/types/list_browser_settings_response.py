"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ListBrowserSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.browser_settings_list
    import capo_workspaces_web.types.pagination_token


class ListBrowserSettingsResponse(TypedDict, closed=True):
    browser_settings: NotRequired[
        "capo_workspaces_web.types.browser_settings_list.BrowserSettingsList"
    ]
    """<p>The browser settings.</p>"""
    next_token: NotRequired[
        "capo_workspaces_web.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBrowserSettingsResponse) -> dict:
    out: dict = {}
    if "browser_settings" in value:
        import capo_workspaces_web.types.browser_settings_list

        out["browserSettings"] = (
            capo_workspaces_web.types.browser_settings_list.serialize_json(
                value["browser_settings"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBrowserSettingsResponse:
    out: ListBrowserSettingsResponse = {}  # type: ignore[typeddict-item]
    if "browserSettings" in data:
        import capo_workspaces_web.types.browser_settings_list

        out["browser_settings"] = (
            capo_workspaces_web.types.browser_settings_list.deserialize_json(
                data["browserSettings"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
