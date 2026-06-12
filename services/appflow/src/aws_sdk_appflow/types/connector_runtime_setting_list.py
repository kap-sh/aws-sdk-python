"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorRuntimeSettingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appflow.types.connector_runtime_setting

ConnectorRuntimeSettingList: TypeAlias = list[
    "aws_sdk_appflow.types.connector_runtime_setting.ConnectorRuntimeSetting"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorRuntimeSettingList) -> list:
    import aws_sdk_appflow.types.connector_runtime_setting

    out: list = []
    for item in value:
        out.append(aws_sdk_appflow.types.connector_runtime_setting.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConnectorRuntimeSettingList:
    import aws_sdk_appflow.types.connector_runtime_setting

    out: ConnectorRuntimeSettingList = []
    for item in data:
        out.append(
            aws_sdk_appflow.types.connector_runtime_setting.deserialize_json(item)
        )
    return out
