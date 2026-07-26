"""Generated from Smithy shape ``com.amazonaws.workspacesweb#UserAccessLoggingSettingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_web.types.user_access_logging_settings_summary

UserAccessLoggingSettingsList: TypeAlias = list[
    "capo_workspaces_web.types.user_access_logging_settings_summary.UserAccessLoggingSettingsSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: UserAccessLoggingSettingsList) -> list:
    import capo_workspaces_web.types.user_access_logging_settings_summary

    out: list = []
    for item in value:
        out.append(
            capo_workspaces_web.types.user_access_logging_settings_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> UserAccessLoggingSettingsList:
    import capo_workspaces_web.types.user_access_logging_settings_summary

    out: UserAccessLoggingSettingsList = []
    for item in data:
        out.append(
            capo_workspaces_web.types.user_access_logging_settings_summary.deserialize_json(
                item
            )
        )
    return out
