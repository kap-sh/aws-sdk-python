"""Generated from Smithy shape ``com.amazonaws.workspaces#UserSettings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.user_setting

UserSettings: TypeAlias = list["aws_sdk_workspaces.types.user_setting.UserSetting"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserSettings) -> list:
    import aws_sdk_workspaces.types.user_setting

    out: list = []
    for item in value:
        out.append(aws_sdk_workspaces.types.user_setting.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> UserSettings:
    import aws_sdk_workspaces.types.user_setting

    out: UserSettings = []
    for item in data:
        out.append(aws_sdk_workspaces.types.user_setting.deserialize_aws_json_1_1(item))
    return out
