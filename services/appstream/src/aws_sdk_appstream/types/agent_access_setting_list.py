"""Generated from Smithy shape ``com.amazonaws.appstream#AgentAccessSettingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appstream.types.agent_access_setting

AgentAccessSettingList: TypeAlias = list[
    "aws_sdk_appstream.types.agent_access_setting.AgentAccessSetting"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentAccessSettingList) -> list:
    import aws_sdk_appstream.types.agent_access_setting

    out: list = []
    for item in value:
        out.append(
            aws_sdk_appstream.types.agent_access_setting.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AgentAccessSettingList:
    import aws_sdk_appstream.types.agent_access_setting

    out: AgentAccessSettingList = []
    for item in data:
        out.append(
            aws_sdk_appstream.types.agent_access_setting.deserialize_aws_json_1_1(item)
        )
    return out
