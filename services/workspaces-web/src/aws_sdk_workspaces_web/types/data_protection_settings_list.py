"""Generated from Smithy shape ``com.amazonaws.workspacesweb#DataProtectionSettingsList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.data_protection_settings_summary

DataProtectionSettingsList: TypeAlias = list["aws_sdk_workspaces_web.types.data_protection_settings_summary.DataProtectionSettingsSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: DataProtectionSettingsList) -> list:
    import aws_sdk_workspaces_web.types.data_protection_settings_summary
    out: list = []
    for item in value:
        out.append(aws_sdk_workspaces_web.types.data_protection_settings_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataProtectionSettingsList:
    import aws_sdk_workspaces_web.types.data_protection_settings_summary
    out: DataProtectionSettingsList = []
    for item in data:
        out.append(aws_sdk_workspaces_web.types.data_protection_settings_summary.deserialize_json(item))
    return out