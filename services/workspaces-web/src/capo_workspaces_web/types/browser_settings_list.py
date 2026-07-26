"""Generated from Smithy shape ``com.amazonaws.workspacesweb#BrowserSettingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_web.types.browser_settings_summary

BrowserSettingsList: TypeAlias = list[
    "capo_workspaces_web.types.browser_settings_summary.BrowserSettingsSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: BrowserSettingsList) -> list:
    import capo_workspaces_web.types.browser_settings_summary

    out: list = []
    for item in value:
        out.append(
            capo_workspaces_web.types.browser_settings_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BrowserSettingsList:
    import capo_workspaces_web.types.browser_settings_summary

    out: BrowserSettingsList = []
    for item in data:
        out.append(
            capo_workspaces_web.types.browser_settings_summary.deserialize_json(item)
        )
    return out
