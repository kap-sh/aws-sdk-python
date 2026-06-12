"""Generated from Smithy shape ``com.amazonaws.workspacesweb#BrowserSettingsList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.browser_settings_summary

BrowserSettingsList: TypeAlias = list["aws_sdk_workspaces_web.types.browser_settings_summary.BrowserSettingsSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: BrowserSettingsList) -> list:
    import aws_sdk_workspaces_web.types.browser_settings_summary
    out: list = []
    for item in value:
        out.append(aws_sdk_workspaces_web.types.browser_settings_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> BrowserSettingsList:
    import aws_sdk_workspaces_web.types.browser_settings_summary
    out: BrowserSettingsList = []
    for item in data:
        out.append(aws_sdk_workspaces_web.types.browser_settings_summary.deserialize_json(item))
    return out