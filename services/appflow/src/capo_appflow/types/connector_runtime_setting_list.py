"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorRuntimeSettingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appflow.types.connector_runtime_setting

ConnectorRuntimeSettingList: TypeAlias = list[
    "capo_appflow.types.connector_runtime_setting.ConnectorRuntimeSetting"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorRuntimeSettingList) -> list:
    import capo_appflow.types.connector_runtime_setting

    out: list = []
    for item in value:
        out.append(capo_appflow.types.connector_runtime_setting.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConnectorRuntimeSettingList:
    import capo_appflow.types.connector_runtime_setting

    out: ConnectorRuntimeSettingList = []
    for item in data:
        out.append(capo_appflow.types.connector_runtime_setting.deserialize_json(item))
    return out
