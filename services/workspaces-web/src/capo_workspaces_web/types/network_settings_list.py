"""Generated from Smithy shape ``com.amazonaws.workspacesweb#NetworkSettingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_web.types.network_settings_summary

NetworkSettingsList: TypeAlias = list[
    "capo_workspaces_web.types.network_settings_summary.NetworkSettingsSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkSettingsList) -> list:
    import capo_workspaces_web.types.network_settings_summary

    out: list = []
    for item in value:
        out.append(
            capo_workspaces_web.types.network_settings_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NetworkSettingsList:
    import capo_workspaces_web.types.network_settings_summary

    out: NetworkSettingsList = []
    for item in data:
        out.append(
            capo_workspaces_web.types.network_settings_summary.deserialize_json(item)
        )
    return out
